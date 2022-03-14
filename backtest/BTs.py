from dbm.DBquant import PyQuantiwise
from dbm.DBmssql import MSSQL

import pandas as pd

from typing import Tuple, List

import calendar
from datetime import datetime, timedelta



class IndexChange:
    MONTH_1Q_BEF = 6
    MONTH_1Q_AFT = (7, 0)  # Month, Year_Add

    MONTH_2Q_BEF = 12
    MONTH_2Q_AFT = (1, 1)  # Month, Year_Add


class IndexChangeM:
    def __init__(self):
        self.data = PyQuantiwise()
        self.server = MSSQL.instance()
        self.server.login(id='wsol2', pw='wsol2')

    @staticmethod
    def month_info(q:str) -> (int, Tuple):
        assert q in {'1q', 'q1', '2q', 'q2'}
        param = IndexChange()
        if q in {'1q', 'q1'}:
            return param.MONTH_1Q_BEF, param.MONTH_1Q_AFT
        else:
            return param.MONTH_2Q_BEF, param.MONTH_2Q_AFT

    def index_change(self, year:int, quarter:str) -> ([Tuple], [Tuple]):
        col = ['year', 'chg_no', 'code', 'stk_no', 'ind_']

        m0, (m1, y1) = self.month_info(q=quarter)
        cdn_bef = f"year = {year} and chg_no = {m0} and ind_='ks200'"
        cdn_aft = f"year = {year + y1} and chg_no = {m1} and ind_='ks200'"
        bef = self.server.select_db(
            database="WSOL",
            schema="dbo",
            table="indcomp",
            column=col,
            condition=cdn_bef
        )
        aft = self.server.select_db(
            database="WSOL",
            schema="dbo",
            table="indcomp",
            column=col,
            condition=cdn_aft
        )
        return bef, aft

    @staticmethod
    def index_added(before:[tuple], after:[tuple]) -> List:
        """
        Find out Added stks from KOSPI200
        """
        b = set([stk[3] for stk in before])
        a = set([stk[3] for stk in after])

        return [stk for stk in a if stk not in b]

    @staticmethod
    def index_subed(before:[tuple], after:[tuple]) -> List:
        """
        Find out subtracted stks from KOSPI200
        """
        b = set([stk[3] for stk in before])
        a = set([stk[3] for stk in after])

        return [stk for stk in b if stk not in a]

    def change(self, year, quarter) -> (List, List):
        b, a = self.index_change(year=year, quarter=quarter)
        added = self.index_added(before=b, after=a)
        excluded = self.index_subed(before=b, after=a)

        return added, excluded

    @staticmethod
    def change_date(year, quarter, dfmt='%Y%m%d') -> (datetime, datetime):
        """
        Return day just before the index change

        Index changing occurs at June, December's second Thursday

        return -> June, December's second Wednesday
        """
        assert quarter in {'1q', 'q1', '2q', 'q2'}
        if quarter in {'1q', 'q1'}:
            tgt = 6
        else:
            tgt = 12

        c = calendar.Calendar(firstweekday=calendar.SUNDAY)
        monthcal = c.monthdatescalendar(year, tgt)
        try:
            weds = list()
            for week in monthcal:
                for day in week:
                    cond0 = (day.weekday() == calendar.WEDNESDAY)
                    cond1 = day.month == tgt
                    if cond0 and cond1:
                        weds.append(day)
            return datetime(year=year, month=tgt, day=1), weds[1]
        except IndexError:
            print("No Wednesday Found?")
            return None

    def match_price(self, *args, **kwargs):
        pass

    @staticmethod
    def calc_return(df:pd.DataFrame):
        """
        Total return of the period
        :param df:
        :return:
        """
        tmp = pd.DataFrame(
            [df.to_numpy()[0], df.to_numpy()[-1]],
            columns=df.columns
        )
        tmp = tmp.pct_change().dropna()
        result = {k: v for k, v in zip(tmp.columns, tmp.to_numpy()[0])}
        return result


class Proactive(IndexChangeM):
    def __init__(self):
        super().__init__()

        # TIMEFRAME
        self.time_start = -2  # 6월 이면 4월부터 매매

    def match_price(self, year:int, quarter:str, dfmt='%Y%m%d'):
        from_date, until_date = self.change_date(year, quarter)
        plus, minus = self.change(year, quarter)

        from_date = from_date - timedelta(days=30 * abs(self.time_start))

        # Added Stocks
        d = self.data.stk_data_multi(
            stock_code_ls=plus,
            start_date=from_date.strftime(dfmt),
            end_date=until_date.strftime(dfmt),
            item='수정주가',
        )
        d.VAL = d.VAL.astype('float32')
        dp = d.pivot_table(values='VAL', index='TRD_DT', columns='STK_CD')
        return dp.dropna(axis=1)


class Reactive(IndexChangeM):
    def __init__(self):
        super().__init__()

        # TIMEFRAME
        self.time_start = -1  # 6월이면 5월부터 매매

    def match_price(self, year:int, quarter:str, dfmt='%Y%m%d'):
        from_date, until_date = self.change_date(year, quarter)
        plus, minus = self.change(year, quarter)

        from_date = from_date - timedelta(days=30 * abs(self.time_start))

        # Added Stocks
        d = self.data.stk_data_multi(
            stock_code_ls=plus,
            start_date=from_date.strftime(dfmt),
            end_date=until_date.strftime(dfmt),
            item='수정주가',
        )
        d.VAL = d.VAL.astype('float32')
        dp = d.pivot_table(values='VAL', index='TRD_DT', columns='STK_CD')
        return dp.dropna(axis=1)


