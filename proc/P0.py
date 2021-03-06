from dbm.DBquant import PyQuantiwise
from dbm.DBmssql import MSSQL
from settings.Sask import *

import pandas as pd

from typing import Tuple
from datetime import datetime, timedelta


class KCP0:
    """
    기초 정보 모으기.

    현재 코스피 종목들의
        1) 시가총액 테이블
        2) 거래대금 테이블
        3) 관리종목 테이블
        4) 유통주식 테이블
    를 리턴함.
    """
    __name__ = 'KCP P0'

    def __init__(self, quarter:str, designate:datetime=None, serveruse:bool=True):
        # ASSERTIONS
        assert quarter in {'q1', 'q2', 'Q1', 'Q2'}

        # If NOT None -> historical testing
        self.DESIGNATE = designate
        self.SERVERUSE = serveruse

        # CLASS MODULES
        self.qt = PyQuantiwise()
        self.db = MSSQL.instance()
        self.db.login(id='wsol2', pw='wsol2')

        # IMMUTABLE INIT LOCAL CONSTANT
        YR, MT = self.__select_date()

        # IMMUTABLE CLASS CONSTANT
        self.STARTDATE, self.ENDDATE = self.__judging_date(q=quarter)
        self.KOSPI, self.KOSPI200 = self.get_original(year=YR, month=MT)
        print(self.STARTDATE, self.ENDDATE, YR, MT)

    def __judging_date(self, q:str) -> (str, str):
        """
        KOSPI 200 change judging period.
        1) May 1st ~ Oct 31st
        2) Nov 1st ~ Apr 30th
        """
        y = datetime.today().year
        if self.DESIGNATE is not None:
            y = self.DESIGNATE.year

        if q.upper() == 'Q2':
            start_date, end_date = f"{y}0501", f"{y}1031"
        else:
            start_date, end_date = f"{y - 1}1101", f"{y}0430"
        return start_date, end_date

    def __select_date(self) -> (int, int):
        if self.DESIGNATE is None:
            d = datetime.today() - timedelta(days=2)
        else:
            d = self.DESIGNATE
        return d.year, d.month

    def get_original(self, year:int, month:int) -> ([Tuple], [Tuple]):
        kospi = self._original_k(y=year, m=month)
        ks200 = self._original_k200(y=year, m=month)
        return kospi, ks200

    def _original_k200(self, y:int, m:int, idx:str='ks200') -> Tuple:
        """
        Original KOSPI200
        :param y: year
        :param m: month
        :param idx: index name
        :return:
        """
        col = ['year', 'chg_no', 'stk_no', 'ind_']
        condition = " and ".join([
            f"year={y}",
            f"chg_no={m}",
            f"ind_='{idx}'"
        ])
        d = self.db.select_db(
            database='WSOL',
            schema='dbo',
            table='indcomp',
            column=col,
            condition=condition
        )
        print(P0_UPDATE_GETIND0.format(self.__name__))
        return d

    def _original_k(self, y:int, m:int, idx:str='kospi') -> [Tuple]:
        """
        Original KOSPI
        :param y: year
        :param m: month
        :param idx: index name
        """
        col = ['year', 'chg_no', 'stk_no', 'ind_']
        condition = " and ".join([
            f"year={y}",
            f"chg_no={m}",
            f"ind_='{idx}'"
        ])
        d = self.db.select_db(
            database='WSOL',
            schema='dbo',
            table='indcomp',
            column=col,
            condition=condition
        )
        print(P0_UPDATE_GETIND1.format(self.__name__))
        return d

    def update_time_data_csv(self, items:str) -> pd.DataFrame:
        print("[KCP P0] >>> KOREAN financial institute data... so dumb.. so outdated..")
        print("[KCP P0] >>> Converting files from .CSV")
        assert items in {'시가총액'}
        if items == '시가총액':
            floc = r"C:/Users/wooriam/PycharmProjects/kospiChange/proc/YUDONG.csv"
        else:
            raise RuntimeError("No File")

        d = pd.read_csv(floc, index_col=0)
        d.columns = [_.replace('A', '') for _ in d.columns]
        d.index = [_.replace('-', '') for _ in d.index]
        print('[KCP P0] >>> Check data dates manually!')
        print("======")
        print(f"Data Dates: {d.index[0]} from {d.index[-1]}")
        print(f"Objective Dates {self.STARTDATE} ~ {self.ENDDATE}")
        return d

    def update_time_data(self, items:str) -> pd.DataFrame:
        """
        Update Time Series data
        시가총액이나, 거래대금과 같은 시계열 데이터를 업데이트 함
        """
        assert items in {'시가총액', '거래대금'}

        k = [stk for _, _, stk, _ in self.KOSPI]
        d = self.qt.stk_data_multi(
            stock_code_ls=k,
            start_date=self.STARTDATE,
            end_date=self.ENDDATE,
            item=items
        )
        d.VAL = d.VAL.astype('int64')
        d = d.pivot_table(
            index=d.TRD_DT,
            columns=d.STK_CD
        )
        d.columns = [name for _, name in d.columns]
        return d

    def update_cross_data(self, items:str, recent_date:int) -> pd.DataFrame:
        """
        Update crosssectional data
        관리종목 여부나, 정리종목 여부, 유동주식비율 등을 업데이트 함.
        """
        assert items in {'관리감리구분', '유통주식비율'}

        k = [stk for _, _, stk, _ in self.KOSPI]
        d = self.qt.stk_data_multi(
            stock_code_ls=k,
            start_date=str(recent_date),
            end_date=str(recent_date),
            item=items
        )
        d.VAL = d.VAL.astype('float32')
        d = d.pivot_table(
            index=d.TRD_DT,
            columns=d.STK_CD
        )
        d.columns = [name for _, name in d.columns]
        return d

    def main(self, date:int) -> (pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame):
        """
        Return
        시가총액 테이블
        거래대금 테이블
        관리종목 테이블
        유통주식 테이블
        (Tuple 안에 데이터프레임 4개)
        """
        d0 = self.update_time_data("시가총액")
        print(P0_MAIN_PROC0.format(self.__name__))
        d1 = self.update_time_data("거래대금")
        print(P0_MAIN_PROC1.format(self.__name__))
        d2 = self.update_cross_data("관리감리구분", date)
        print(P0_MAIN_PROC2.format(self.__name__))
        d3 = self.update_cross_data("유통주식비율", date)
        print(P0_MAIN_PROC3.format(self.__name__))
        return d0, d1, d2, d3
