from proc.P0 import KCP0
from proc.P1 import KCP1
from proc.P2 import KCP2
from proc.P3 import KCP3

from datetime import datetime


def reactive(test=True, **kwargs):
    """
    <BACKTESTING>
    Pipeline
    KCP0 -> KCP1 -> KCP2 -> KCP3
    """
    # Setup kwargs
    if test is True:
        d = kwargs['date']
        dint = int(d.strftime('%Y%m%d'))
    else:
        d = datetime.today()
        dint = int(d.strftime('%Y%m%d'))


    if 'parachute' in kwargs.keys():
        pr = kwargs['parachute']
    else:
        pr = None

    ####################################################
    # PROCESS 1
    p0 = KCP0('q2', designate=d)
    p0_0, p0_1, p0_2, p0_3 = p0.main(dint)
    ####################################################
    # PROCESS 2
    p1 = KCP1(p0_0, p0_1, p0_2, p0_3, pr)
    p1_0, p1_1 = p1.main()  # 후보군 시가총액, 후보 거래대금
    ####################################################
    # PROCESS 3
    p2 = KCP2(p1_0, p1_1, designate=d)
    p2_0 = p2.get_sector_sep()
    ####################################################
    # PROCESS 4
    p3 = KCP3(p1_0, p1_1, p2_0)
    p3_0 = p3.selection()
    p3_1 = p3.amend_selection(p3_0)
    ####################################################
    return p3_1


def proactive(**kwargs):
    d = kwargs['date']
    dint = d.strftime('%Y%m%d')
    # Setup kwargs
    ####################################################
    # PROCESS 1
    p0 = KCP0('q1', designate=d)
    p0_0, p0_1, p0_2, p0_3 = p0.main(dint)
    ####################################################
    ...
    return p0_0, p0_1, p0_2, p0_3


if __name__ == "__main__":
    # REACTIVE
    dt = datetime(2021, 10, 29)
    pa = ['007700', '259960', '323410', '361610', '383800']
    """
    [
    '007700', '383800' : 분할상장 이슈
    '259960', '323410', '361610' : 특별 편입 
    ]
    """
    reactive_result = reactive(test=True, date=dt, parachute=pa)

    # PROACTIVE
    dt = datetime(2022, 3, 14)
    pa = ['373220']
    """
    '373220' : 특별 편입
    """
    proactive_temp = proactive(date=dt)