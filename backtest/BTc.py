from dbm.DBmssql import MSSQL
import pandas as pd


def stk_codes(val, prefix:str='A', std:int=6):
    if len(str(val)) == std:
        return f"{prefix}{val}"
    else:
        return f"{prefix}{'0' * (std - len(str(val)))}{val}"


# Get Tested Data
d = pd.read_csv("../result.csv", index_col=0)
d = d.applymap(stk_codes)

# Get Comparison Data
server = MSSQL.instance()
server.login(id='wsol1', pw='wsol1')
e = server.select_db(
    database='WSOL',
    schema='dbo',
    table='indcomp',
    column=['*'],
    condition="year = 2022 and chg_no = 3 and ind_ = 'ks200'"
)
e = ['A' + info[3] for info in e]

# Compare

for cols in d.columns:
    new = [n for n in d[cols] if n not in e]
    out = [o for o in e if o not in d[cols].to_numpy().tolist()]

