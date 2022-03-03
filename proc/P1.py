from settings.Sask import *
from settings.Sexc import Exclude
import pandas as pd

from typing import Iterable, List


class KCP1:
    __name__ = "KCP P1"

    def __init__(self, tval:pd.DataFrame, tvol:pd.DataFrame, mont:pd.DataFrame,
                 fltg:pd.DataFrame, parachute:Iterable=None):
        # IMMUTABLE CLASS CONSTANT
        self.PARACHUTE = parachute
        self.TVAL = tval
        self.TVOL = tvol
        self.MONT = mont
        self.FLTG = fltg

    def exclude_monitoring(self) -> List:
        """
        if value == 1 -> is monitoring True
        """
        d = self.MONT.transpose()
        return d.loc[d[d.columns[0]] == 1].index.tolist()

    def exclude_floating(self) -> List:
        """
        if value < 10 -> floating condition not met
        """
        d = self.FLTG.transpose()
        return d.loc[d[d.columns[0]] < 10].index.tolist()

    def exclude_age(self) -> List:
        """
        if age is not matured(6 months) -> it will be eliminated
        """
        d = self.TVAL.dropna(axis=1)
        survived = set(d.columns.tolist())
        return [stks for stks in self.TVAL.columns if stks not in survived]

    def main(self) -> (pd.DataFrame, pd.DataFrame):
        """
        Extract Candidate for KOSPI200 UNIVERSE
        """
        no0 = set(self.exclude_monitoring())
        print(P1_MAIN_PROC0.format(self.__name__))
        no1 = set(self.exclude_floating())
        print(P1_MAIN_PROC1.format(self.__name__))
        no2 = set(self.exclude_age())
        print(P1_MAIN_PROC2.format(self.__name__))
        no3 = Exclude.EC.keys()
        print(P1_MAIN_PROC3.format(self.__name__))

        # Make One Long set()
        no0.update(no1)
        no0.update(no2)
        no0.update(no3)

        candidate = [stk for stk in self.TVAL.columns if stk not in no0]
        if self.PARACHUTE is not None:
            print(P1_MAIN_SUBPROC0.format(self.__name__))
            candidate.extend(self.PARACHUTE)
        return self.TVAL[candidate], self.TVOL[candidate]







