from dbm.DBmssql import MSSQL

import pandas as pd

from datetime import datetime
from typing import Iterable, Dict, Set


class KCP2:
    """
    코스피 200 은 각 섹터 안에서 등수를 지정하기 때문에
    섹터 안에서 나누는 것 작업 수행
        1) 섹터 안에서 나누고
        2) 현재 섹터 안에서 Kospi200 에 이미 있는지, 아닌지를 설정함.
    """
    __name__ = "KCP2"
    sector_encoding = {
        'Energy': 1,
        'Materials': 2,
        'Industrials': 3,
        'Consumer Discretionary': 4,
        'Consumer Staples': 5,
        'Health Care': 6,
        'Financials': 7,
        'Information Technology': 8,
        'Communication Services': 9,
        'Utilities': 10,
        'Real Estate': 7,  # 금융 및 부동산으로 묶임
    }
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

    def __init__(self, kospi_tval:pd.DataFrame, kospi_tvol:pd.DataFrame, designate:datetime=None):
        # Test
        self.DESIGNATE = designate

        # CLASS MODULES
        self.server = MSSQL.instance()
        self.server.login(id='wsol2', pw='wsol2')

        # IMMUTABLE CLASS LOCAL VARIABLE
        self.DATA_TVOL = kospi_tval
        self.DATA_TVAL = kospi_tvol
        self.DATA_CANDIDATE = set(kospi_tval.columns)

    def get_sector_info(self) -> Dict:
        print("[KCP P2] >>> Retrieve Sector Information")
        col = ['stk_no', 'cls', 'standard']
        cnd = f"standard = 'gics'"
        cls = self.server.select_db(
            database="WSOL",
            schema="dbo",
            table="bbggics",
            column=col,
            condition=cnd
        )

        # FILTER SECTORS FOR CANDIDATE ONLY
        cls = [val for val in cls if val[0] in self.DATA_CANDIDATE]
        return self.__hashmap(cls)

    @classmethod
    def __hashmap(cls, data:[Iterable]) -> Dict:
        mapping = dict()
        for r in data:
            if cls.sector_encoding[r[1]] not in mapping.keys():
                mapping[cls.sector_encoding[r[1]]] = [r[0]]
            else:
                mapping[cls.sector_encoding[r[1]]].append(r[0])
        return mapping

    def get_current_k200(self) -> Set:
        print("[KCP P2] >>> Retrieve index: KOSPI200")
        if self.DESIGNATE is not None:
            t = self.DESIGNATE
        else:
            t = datetime.today()
        col = ['year', 'chg_no', 'code', 'stk_no', 'ind_']
        cnd = f"year = {t.year} and chg_no = {t.month} and ind_='ks200'"
        d = self.server.select_db(
            database='WSOL',
            schema='dbo',
            table='indcomp',
            column=col,
            condition=cnd
        )
        return set([stk[3] for stk in d])

    def get_sector_sep(self) -> Dict:
        # GET KOSPI CANDIDATE
        candidate = self.get_sector_info()
        # GET KOSPI 200
        current_k200 = self.get_current_k200()

        # DIVIDE {SECTOR : ([INSIDE K200], [OUTSIDE K200])}
        print("[KCP P2] >>> Divide into {sector : ([inside K200], [outside K200])}")
        result = dict()
        for sector_num, sector_stk_ls in candidate.items():
            result[sector_num] = (
                [
                    stk for stk in sector_stk_ls
                    if stk in current_k200  # currently in kospi200
                ],
                [
                    stk for stk in sector_stk_ls
                    if stk not in current_k200  # currently --NOT-- kospi200
                ]
            )
        return result
