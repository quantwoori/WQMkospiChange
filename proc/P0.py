from dbm.DBquant import PyQuantiwise
from settings.Sask import *

import pandas as pd

from datetime import datetime
import time


class DataUpdate:
    def __init__(self, quarter:str):
        assert quarter in {'q1', 'q2', 'Q1', 'Q2'}
        print(P0_UPDATE_WARNING1)

    def __select_date(self):
        
        ...

    def get_original(self):
        ...

    def _original_k200(self):
        ...

    def _original_k(self):
        ...

    def update_data(self):
        ...
