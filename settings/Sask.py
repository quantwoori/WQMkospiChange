# P0 REQUEST UPDATE MESSAGE
P0_UPDATE_WARNING1 = ...
P0_UPDATE_WARNING2 = ...

P0_UPDATE_GETIND0 = "[{}] >>> Retrieve index: KOSPI"
P0_UPDATE_GETIND1 = "[{}] >>> Retrieve index: KOSPI200"

P0_MAIN_PROC0 = "[{}] >>> Update TOTALVALUE(시가총액)"
P0_MAIN_PROC1 = "[{}] >>> Update TRADEVALUE(거래대금)"
P0_MAIN_PROC2 = "[{}] >>> Update WARNINGS(관리감리)"
P0_MAIN_PROC3 = "[{}] >>> Update FLOATING(유동주식)"

# P1 CANDIDATE CLEANUP
P1_MAIN_PROC0 = "[{}] >>> Excluding WARNINGS(관리감리)"
P1_MAIN_PROC1 = "[{}] >>> Excluding FLOATING(유동주식) below 10%"
P1_MAIN_PROC2 = "[{}] >>> Excluding SHORTS(거래기간) below 6m"
P1_MAIN_PROC3 = "[{}] >>> Excluding NON INCLUDABLEs(SPAC, ETFs)"
P1_MAIN_SUBPROC0 = "[{}] >>> Including PARACHUTE. KRX-wise"
