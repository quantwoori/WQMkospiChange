from dbm.DBmssql import MSSQL

import pandas as pd
import numpy as np

from typing import Iterable, List, Dict


class KCP3:
    """
    모든 것을 종합하는
    지수변경 예측 파이프라인의 끝.
    """
    __name__ = 'KCP3'
    sector_encoding_rev = {
        1: 'Energy',
        2: 'Materials',
        3: 'Industrials',
        4: 'Consumer Discretionary',
        5: 'Consumer Staples',
        6: 'Health Care',
        7: 'Financials and Real Estate',  # 금융 및 부동산으로 묶임
        8: 'Information Technology',
        9: 'Communication Services',
        10: 'Utilities',
    }

    def __init__(self, candidate_tval:pd.DataFrame, candidate_tvol:pd.DataFrame, sector_sep:dict):
        """
        :param candidate_tvol: KCP1 main() 함수의 결과물
        :param candidate_tval: KCP1 main() 함수의 결과물

        :param sector_sep: KCP2 get_sector_sep() 합수의 결과물
        """
        # CLASS LOCAL MODULE
        print("[KCP P3] >>> Overall selection process")
        self.server = MSSQL.instance()
        self.server.login(id='wsol2', pw='wsol2')

        # IMMUTABLE CLASS LOCAL DATA
        self.DATA_TVOL = candidate_tvol
        self.DATA_TVAL = candidate_tval
        self.SECTOR_INFO = sector_sep  # Dict

        print("[KCP P3] >>> Calculating Daily mean volume and mean value")
        self.DATA_MVOL = self.DATA_TVOL.mean()
        self.DATA_MVAL = self.DATA_TVAL.mean()

    def selection(self) -> Dict:
        result_sector = dict()
        for sector_num, stks in self.SECTOR_INFO.items():
            print(f"[KCP P3] >>> Calculating Sector >> {self.sector_encoding_rev[sector_num]}")
            _in, _out = stks
            # STEP 1
            pick1, nopick1, liq_standard = self._selection_step_1(
                sector_in=_in, sector_out=_out,
            )
            # STEP 2
            pick2, nopick2 = self._selection_step_2(
                new=pick1, liquidity_std=liq_standard, sector_in=_in, sector_out=_out
            )
            assert len(pick2 + nopick1 + nopick2) <= len(_in + _out), "Something is wrong"
            result_sector[sector_num] = (pick2, nopick1 + nopick2)
        return result_sector

    def _selection_step_1(self, sector_in:list, sector_out:list, value_standard:float=0.85,
                          volume_standard:float=0.85) -> (List, List):
        """
        시가 총액 기준, 거래 대금 기준(순위) 에 따라서 편입, 섹터 내 편출 종목 산정.
        """
        # 시가총액 기준
        sector_value = self.DATA_MVAL.loc[sector_in + sector_out]
        sector_value = sector_value.sort_values(ascending=False)
        # 섹터 내 비중의 몇 퍼센트
        sector_value = sector_value.div(sector_value.sum())
        sector_value = sector_value.cumsum()
        # 일평균 시가총액 85% 이내
        in_value, _ = (
            sector_value.loc[sector_value < value_standard].index.to_list(),
            sector_value.loc[sector_value >= value_standard].index.to_list()
        )

        # 거래대금 기준(유동성 기준)
        sector_volume = self.DATA_MVOL.loc[sector_in + sector_out]
        sector_volume = sector_volume.sort_values(ascending=False)
        # 일평균 거래대금 "순위"가 85% 이내
        in_volume, _ = (
            sector_volume[:int(np.floor(len(sector_volume) * volume_standard))].index.to_list(),
            sector_volume[int(np.floor(len(sector_volume) * volume_standard)):].index.to_list(),
        )
        success, fail = self._sector_wise_merge_standard(
            standard1=in_value,
            standard2=in_volume,
            in_and_out=(sector_in + sector_out)
        )
        return success, fail, in_volume

    @staticmethod
    def _sector_wise_merge_standard(standard1:Iterable, standard2:Iterable,
                                    in_and_out:Iterable) -> (List, List):
        s1, s2 = set(standard1), set(standard2)

        pick, no_pick = list(), list()
        for stk in in_and_out:
            cond1 = stk in s1
            cond2 = stk in s2
            if cond1 and cond2:
                pick.append(stk)
            else:
                no_pick.append(stk)
        return pick, no_pick

    def _selection_step_2(self, new:Iterable, liquidity_std:Iterable, sector_in:Iterable, sector_out:Iterable, new_standard:float=0.9,
                          not_new_standard:float=1.1):
        """
        섹터 내에서
            신규 KOSPI200 종목
                - 시가 총액 순위의 90% 이내에 들어야함
                - "신규 종목이면서 new_set에 있으면 통과!"
            기존 KOSPI200 종목
                - 시가 총액 순위의 110% 이내에 들어야함
                _ not_new_set
        """
        # 시가 총액 자료
        sector_value = self.DATA_MVAL.loc[sector_in + sector_out]

        # 시가 총액 순위 자료
        not_new_set = set(
            sector_value[:int(np.floor(len(sector_in) * not_new_standard))].index
        )
        new_set = set(
            sector_value[:int(np.floor(len(sector_in) * new_standard))].index
        )

        # 신규 및 기존 종목
        sector_new = [stk for stk in new if stk not in sector_in]  # 신규 진입 종목
        sector_not_new = [stk for stk in new if stk in sector_in]  # 기존 섹터 내 KOSPI200

        pick, no_pick = list(), list()
        for stk in sector_new:
            if stk in new_set:
                pick.append(stk)
            else:
                no_pick.append(stk)

        for stk in sector_not_new:
            cnd_notnewset = stk in not_new_set
            cnd_newset = stk in liquidity_std
            if cnd_newset and cnd_notnewset:
                pick.append(stk)
            else:
                no_pick.append(stk)

        return pick, no_pick

    def amend_selection(self, selection:dict):
        """
        self.selection() 함수 수행 이후
            1) 200 종목이 충족되는지 확인해야함.
        """
        # 200 종목 이상, 이하가 뽑혔는지 확인
        count = 0
        for sector, picks in selection.items():
            selected, _ = picks
            count += len(selected)

        if count < 200:
            self._pick200under()

        elif count > 200:
            self._pick200over()

        else:  # count == 200
            self._pick200(result=selection)

    @staticmethod
    def _pick200(result:dict):
        res = list()
        for sector, picks in result.items():
            selected, _ = picks
            res.append(selected)

        return sum(res, []), list()

    def _pick200under(self):
        # 기존 KOSPI200종목

        # 유동성 기준 만족

        # 잔여종목 중 충족 현황
        ...

    @staticmethod
    def _pick200over():
        raise NotImplementedError