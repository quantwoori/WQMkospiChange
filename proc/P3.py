from dbm.DBmssql import MSSQL

import pandas as pd
import numpy as np

from typing import Iterable, List


class KCP3:
    """
    모든 것을 종합하는
    지수변경 예측 파이프라인의 끝.
    """
    __name__ = 'KCP3'

    def __init__(self, candidate_tvol:pd.DataFrame, candidate_tval:pd.DataFrame, sector_sep:dict):
        """
        :param candidate_tvol: KCP1 main() 함수의 결과물
        :param candidate_tval: KCP1 main() 함수의 결과물

        :param sector_sep: KCP2 get_sector_sep() 합수의 결과물
        """
        # CLASS LOCAL MODULE
        self.server = MSSQL.instance()
        self.server.login(id='wsol2', pw='wsol2')

        # IMMUTABLE CLASS LOCAL DATA
        self.DATA_TVOL = candidate_tvol
        self.DATA_TVAL = candidate_tval
        self.SECTOR_INFO = sector_sep  # Dict

        self.DATA_MVOL = self.DATA_TVOL.mean()
        self.DATA_MVAL = self.DATA_TVAL.mean()

    def selection(self):
        mean_vol, mean_val = self.DATA_TVOL.mean(), self.DATA_TVAL.mean()
        for sector_num, stks in self.SECTOR_INFO.items():
            _in, _out = stks
            # STEP 1
            pick1, nopick1 = self._sector_wise_selection(
                sector_in=_in, sector_out=_out,
            )
            # STEP 2

    def _sector_wise_selection(self, sector_in:list, sector_out:list, value_standard:float=0.85,
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

        # 거래대금 기준
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
        return success, fail

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
