from dbm.DBmssql import MSSQL
import pandas as pd


def stk_codes(val, prefix:str='A', std:int=6):
    if len(str(val)) == std:
        return f"{prefix}{val}"
    else:
        return f"{prefix}{'0' * (std - len(str(val)))}{val}"


# Get Tested Data
d = pd.read_csv("../result13.csv", index_col=0)
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
comp_in = dict()
comp_out = dict()
for cols in d.columns:
    new = [n for n in d[cols] if n not in e]
    out = [o for o in e if o not in d[cols].to_numpy().tolist()]

    for stk in new:
        if stk in comp_in.keys():
            comp_in[stk] += 1
        else:
            comp_in[stk] = 1

    for stk in out:
        if stk in comp_out.keys():
            comp_out[stk] += 1
        else:
            comp_out[stk] = 1


