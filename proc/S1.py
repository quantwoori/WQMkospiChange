from dbm.DBquant import PyQuantiwise
from proc.S0 import BrownianMotion
from datetime import datetime, timedelta
from typing import Iterable, Dict

import pandas as pd


class GeneratePrice:
    def __init__(self, stocks:Iterable, start_date:datetime, end_date:datetime,
                 target_date:datetime, holidays:int=0):
        self.data = PyQuantiwise()

        # IMMUTABLE CLASS OBJ
        self.STKS = stocks
        self.STARTDT = start_date
        self.ENDDT = end_date
        self.TARGETDT = target_date
        self.HOLIDAY = holidays

    def stat_price(self, dfmt='%Y%m%d') -> (Dict, Dict, Dict):
        d = self.data.stk_data_multi(
            stock_code_ls=self.STKS,
            start_date=self.STARTDT.strftime(dfmt),
            end_date=self.ENDDT.strftime(dfmt),
            item='수정주가'
        )
        d.VAL = d.VAL.astype('float32')
        d = d.pivot_table(values='VAL', index='TRD_DT', columns='STK_CD')

        dpct = d.pct_change()[1:]
        # MEAN
        dmean = {k: v for k, v in dpct.mean().reset_index().to_numpy()}
        dstd = {k: v for k, v in dpct.std().reset_index().to_numpy()}
        dprc = {k: v for k, v in d[-1:].transpose().reset_index().to_numpy()}  # last price
        return dmean, dstd, dprc

    def stks_num(self, dfmt='%Y%m%d') -> Dict:
        d = self.data.stk_data_multi(
            stock_code_ls=self.STKS,
            start_date=self.STARTDT.strftime(dfmt),
            end_date=self.ENDDT.strftime(dfmt),
            item='상장주식수'
        )
        d.VAL = d.VAL.astype('float32')
        d = d.pivot_table(values='VAL', index='TRD_DT', columns='STK_CD')
        res = {k: v for k, v in d[-1:].transpose().reset_index().to_numpy()}
        return res

    @staticmethod
    def days_to_date(start_date:datetime, target_date:datetime, holidays:int) -> int:
        d = start_date
        dcount = 0
        while d < target_date:
            # 오늘 포함 시작
            if d.weekday() < 5:
                dcount += 1
            d += timedelta(days=1)

        return dcount - holidays

    def gen_path(self, stk:str, start_value_info:dict, mean_info:dict, std_info:dict, step_size:int) -> pd.DataFrame:
        bm = BrownianMotion(start_value_info[stk])
        gen = pd.DataFrame(
            bm.gen_scaled_brownian(
                mean_info[stk],
                std_info[stk],
                step_size
            )
        )
        return gen

    def gen_brownian(self):
        rtn_mean_info, rtn_std_info, last_price = self.stat_price()
        total_stocks = self.stks_num()
        steps = self.days_to_date(self.ENDDT, self.TARGETDT, self.HOLIDAY)

        df = pd.DataFrame(None)
        for stk in self.STKS:

            d = self.gen_path(stk, last_price, rtn_mean_info, rtn_std_info, steps)
            d = d * total_stocks[stk]
            d.columns = [stk]
            df = pd.concat([df, d], axis=1)
        return df
