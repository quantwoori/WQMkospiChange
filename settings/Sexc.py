class Exclude:
    """
    EXCLUDE
    SPAC,
    ETFs,
    REITs,
    Ship Investment Companies,
    """
    EC = {
        "088980": "맥쿼리인프라",
        "088260": "이리츠코크렙",
        "140910": "에이리츠",
        "145270": "케이탑리츠",
        "204210": "모두투어리츠",
        "293940": "신한알파리츠",
        "330590": "롯데리츠",
        "334890": "이지스밸류리츠",
        "338100": "NH프라임리츠",
        "348950": "제이알글로벌리츠",
        "350520": "이지스레지던스리츠",
        "357120": "코람코에너지리츠",
        "357250": "미래에셋맵스리츠",
        "365550": "ESR켄달스퀘어리츠",
        "377190": "디앤디플랫폼리츠",
        "395400": "SK리츠",
        "396690": "미래에셋글로벌리츠",
        "400760": "NH올원리츠",
        "404990": "신한서부티엔디리츠",
        "323280": "신영스팩5호",
        "328380": "미래에셋대우스팩3호",
        "329560": "상상인이안제2호스팩",
        "330990": "케이비제19호스팩",
        "331520": "교보9호스팩",
        "332290": "대신밸런스제7호스팩",
        "332710": "하나금융14호스팩",
        "333050": "신한제6호스팩",
        "335870": "IBKS제12호스팩",
        "336060": "유안타제5호스팩",
        "336570": "대신밸런스제8호스팩",
        "337450": "SK5호스팩",
        "340120": "하이제5호스팩",
        "340350": "SK6호스팩",
        "341160": "하나금융15호스팩",
        "342550": "케이비제20호스팩",
        "343510": "하나금융16호스팩",
        "344050": "신영스팩6호",
        "347140": "케이프이에스제4호",
        "349720": "이베스트스팩5호",
        "351340": "IBKS제13호스팩",
        "353060": "에이치엠씨제5호스팩",
        "353070": "에이치엠씨제4호스팩",
        "353490": "미래에셋대우스팩 5호",
        "355150": "교보10호스팩",
        "363260": "하나금융17호스팩",
        "365590": "엔에이치스팩18호",
        "366330": "신한제7호스팩",
        "367340": "DB금융스팩8호",
        "367360": "DB금융스팩9호",
        "367460": "유안타제7호스팩",
        "367480": "유안타제8호스팩",
        "368770": "한국9호스팩",
        "372290": "하나머스트7호스팩",
        "373340": "유진스팩6호",
        "377400": "하이제6호스팩",
        "377630": "삼성스팩4호",
        "380320": "삼성머스트스팩5호",
        "380440": "엔에이치스팩19호",
        "386580": "한화플러스제2호스팩",
        "387310": "대신밸런스제10호스팩",
        "388220": "하나금융19호스팩",
        "388790": "IBKS제16호스팩",
        "388800": "유진스팩7호",
        "391060": "엔에이치스팩20호",
        "391710": "엔에이치스팩21호",
        "393360": "신한제8호스팩",
        "396770": "엔에이치스팩22호",
        "397500": "대신밸런스제11호스팩",
        "397880": "교보11호스팩",
        "400560": "하나금융20호스팩",
        "400840": "하이제7호스팩",
        "404950": "DB금융스팩10호",
        "405350": "IBKS제17호스팩",
        "406760": "하나금융21호스팩",
        "409570": "한국제10호스팩",
        "094800": "맵스리얼티1",
        "096300": "베트남개발1",
        "152550": "한국ANKOR유전",
        "168490": "한국패러랠",
        "069500": "KODEX 200",
        "069660": "KOSEF 200",
        "091160": "KODEX 반도체",
        "091170": "KODEX 은행",
        "091180": "KODEX 자동차",
        "091220": "TIGER 은행",
        "091230": "TIGER 반도체",
        "098560": "TIGER 방송통신",
        "099140": "KODEX 차이나H",
        "100910": "KOSEF KRX100",
        "101280": "KODEX 일본TOPIX100",
        "102110": "TIGER 200",
        "102780": "KODEX 삼성그룹",
        "102960": "KODEX 기계장비",
        "102970": "KODEX 증권",
        "104520": "KOSEF 블루칩",
        "104530": "KOSEF 고배당",
        "105010": "TIGER 라틴35",
        "105190": "KINDEX 200",
        "105780": "KBSTAR 5대그룹주",
        "108450": "KINDEX 삼성그룹섹터가중",
        "108590": "TREX 200",
        "114100": "KBSTAR 국고채3년",
        "114260": "KODEX 국고채3년",
        "114460": "KINDEX 국고채3년",
        "114470": "KOSEF 국고채3년",
        "114800": "KODEX 인버스",
        "114820": "TIGER 국채3년",
        "117460": "KODEX 에너지화학",
        "117680": "KODEX 철강",
        "117690": "TIGER 차이나항셍25",
        "117700": "KODEX 건설",
        "122090": "ARIRANG 코스피50",
        "122260": "KOSEF 통안채1년",
        "122630": "KODEX 레버리지",
        "123310": "TIGER 인버스",
        "123320": "TIGER 레버리지",
        "130680": "TIGER 원유선물Enhanced(H)",
        "130730": "KOSEF 단기자금",
        "131890": "KINDEX 삼성그룹동일가중",
        "132030": "KODEX 골드선물(H)",
        "133690": "TIGER 미국나스닥100",
        "136340": "KBSTAR 중기우량회사채",
        "137610": "TIGER 농산물선물Enhanced(H)",
        "137930": "마이다스 200커버드콜5%OTM",
        "138230": "KOSEF 미국달러선물",
        "138520": "TIGER 삼성그룹펀더멘털",
        "138530": "TIGER LG그룹+펀더멘털",
        "138540": "TIGER 현대차그룹+펀더멘털",
        "138910": "KODEX 구리선물(H)",
        "138920": "KODEX 콩선물(H)",
        "139220": "TIGER 200 건설",
        "139230": "TIGER 200 중공업",
        "139240": "TIGER 200 철강소재",
        "139250": "TIGER 200 에너지화학",
        "139260": "TIGER 200 IT",
        "139270": "TIGER 200 금융",
        "139280": "TIGER 경기방어",
        "139290": "TIGER 200 경기소비재",
        "139310": "TIGER 금속선물(H)",
        "139320": "TIGER 금은선물(H)",
        "139660": "KOSEF 미국달러선물인버스",
        "140570": "KBSTAR 수출주",
        "140580": "KBSTAR 우량업종",
        "140700": "KODEX 보험",
        "140710": "KODEX 운송",
        "140950": "파워 코스피100",
        "143460": "KINDEX 밸류대형",
        "143850": "TIGER 미국S&P500선물(H)",
        "143860": "TIGER 헬스케어",
        "144600": "KODEX 은선물(H)",
        "145670": "KINDEX 인버스",
        "145850": "TREX 펀더멘탈 200",
        "147970": "TIGER 모멘텀",
        "148020": "KBSTAR 200",
        "148070": "KOSEF 국고채10년",
        "150460": "TIGER 중국소비테마",
        "152100": "ARIRANG 200",
        "152380": "KODEX 국채선물10년",
        "152500": "KINDEX 레버리지",
        "152870": "파워 200",
        "153130": "KODEX 단기채권",
        "153270": "KOSEF 코스피100",
        "156080": "KODEX MSCI Korea",
        "157450": "TIGER 단기통안채",
        "157490": "TIGER 소프트웨어",
        "157500": "TIGER 증권",
        "159800": "마이티 코스피100",
        "160580": "TIGER 구리실물",
        "161510": "ARIRANG 고배당주",
        "166400": "TIGER 200커버드콜5%OTM",
        "167860": "KOSEF 국고채10년레버리지",
        "168300": "KTOP 코스피50",
        "168580": "KINDEX 중국본토CSI300",
        "169950": "KODEX 차이나A50",
        "174350": "TIGER 로우볼",
        "174360": "KBSTAR 중국본토대형주CSI100",
        "176710": "파워 중기국고채",
        "176950": "KODEX 국채선물10년인버스",
        "181480": "KINDEX 미국다우존스리츠(합성 H)",
        "182480": "TIGER 미국MSCI리츠(합성 H)",
        "182490": "TIGER 단기선진하이일드(합성 H)",
        "183700": "KBSTAR 채권혼합",
        "183710": "KBSTAR 주식혼합",
        "185680": "KODEX 미국S&P바이오(합성)",
        "189400": "ARIRANG 글로벌MSCI(합성 H)",
        "190620": "KINDEX 단기통안채",
        "192090": "TIGER 차이나CSI300",
        "192720": "파워 고배당저변동성",
        "195920": "TIGER 일본TOPIX(합성 H)",
        "195930": "TIGER 유로스탁스50(합성 H)",
        "195970": "ARIRANG 선진국MSCI(합성 H)",
        "195980": "ARIRANG 신흥국MSCI(합성 H)",
        "196030": "KINDEX 일본TOPIX레버리지(H)",
        "196230": "KBSTAR 단기통안채",
        "200030": "KODEX 미국S&P산업재(합성)",
        "200250": "KOSEF 인도Nifty50(합성)",
        "203780": "TIGER 미국나스닥바이오",
        "204450": "KODEX 차이나H레버리지(H)",
        "204480": "TIGER 차이나CSI300레버리지(합성)",
        "205720": "KINDEX 일본TOPIX인버스(합성 H)",
        "208470": "SOL 선진국MSCI World(합성 H)",
        "210780": "TIGER 코스피고배당",
        "211560": "TIGER 배당성장",
        "211900": "KODEX 배당성장",
        "213610": "KODEX 삼성그룹밸류",
        "213630": "ARIRANG 미국다우존스고배당주(합성 H)",
        "214980": "KODEX 단기채권PLUS",
        "215620": "HK S&P코리아로우볼",
        "217770": "TIGER 원유선물인버스(H)",
        "217780": "TIGER 차이나CSI300인버스(합성)",
        "217790": "TIGER 가격조정",
        "218420": "KODEX 미국S&P에너지(합성)",
        "219390": "KBSTAR 미국S&P원유생산기업(합성 H)",
        "219480": "KODEX 미국S&P500선물(H)",
        "219900": "KINDEX 중국본토CSI300레버리지(합성)",
        "220130": "SOL 중국본토 중소형 CSI500(합성 H)",
        "223190": "KODEX 200가치저변동",
        "225030": "TIGER 미국S&P500선물인버스(H)",
        "225040": "TIGER 미국S&P500레버리지(합성 H)",
        "225050": "TIGER 유로스탁스레버리지(합성 H)",
        "225060": "TIGER 이머징마켓MSCI레버리지(합성 H)",
        "225130": "KINDEX 골드선물 레버리지(합성 H)",
        "225800": "KOSEF 미국달러선물레버리지",
        "226380": "KINDEX Fn성장소비주도주",
        "226490": "KODEX 코스피",
        "226980": "KODEX 200 중소형",
        "227540": "TIGER 200 헬스케어",
        "227550": "TIGER 200 산업재",
        "227560": "TIGER 200 생활소비재",
        "227570": "TIGER 우량가치",
        "227830": "ARIRANG 코스피",
        "228790": "TIGER 화장품",
        "228800": "TIGER 여행레저",
        "228810": "TIGER 미디어컨텐츠",
        "228820": "TIGER KTOP30",
        "229200": "KODEX 코스닥 150",
        "229720": "KODEX KTOP30",
        "230480": "KOSEF 미국달러선물인버스2X",
        "232080": "TIGER 코스닥150",
        "233160": "TIGER 코스닥150 레버리지",
        "233740": "KODEX 코스닥150 레버리지",
        "234310": "KBSTAR V&S셀렉트밸류",
        "236350": "TIGER 인도니프티50레버리지(합성)",
        "237350": "KODEX 코스피100",
        "237370": "KODEX 배당성장채권혼합",
        "237440": "TIGER 경기방어채권혼합",
        "238670": "ARIRANG 스마트베타Quality채권혼합",
        "238720": "KINDEX 일본Nikkei225(H)",
        "239660": "ARIRANG 우량회사채50 1년",
        "241180": "TIGER 일본니케이225",
        "241390": "KBSTAR V&S셀렉트밸류채권혼합",
        "243880": "TIGER 200IT레버리지",
        "243890": "TIGER 200에너지화학레버리지",
        "244580": "KODEX 바이오",
        "244620": "KODEX 모멘텀Plus",
        "244660": "KODEX 퀄리티Plus",
        "244670": "KODEX 밸류Plus",
        "245340": "TIGER 미국다우존스30",
        "245350": "TIGER 유로스탁스배당30",
        "245360": "TIGER 차이나HSCEI",
        "245710": "KINDEX 베트남VN30(합성)",
        "248260": "TIGER 일본TOPIX헬스케어(합성)",
        "248270": "TIGER S&P글로벌헬스케어(합성)",
        "250730": "KBSTAR 차이나HSCEI(H)",
        "250780": "TIGER 코스닥150선물인버스",
        "251340": "KODEX 코스닥150선물인버스",
        "251350": "KODEX 선진국MSCI World",
        "251590": "ARIRANG 고배당저변동50",
        "251600": "ARIRANG 고배당주채권혼합",
        "251890": "KINDEX 코스닥(합성)",
        "252000": "TIGER 200동일가중",
        "252400": "KBSTAR 200선물레버리지",
        "252410": "KBSTAR 200선물인버스",
        "252420": "KBSTAR 200선물인버스2X",
        "252650": "KODEX 200동일가중",
        "252670": "KODEX 200선물인버스2X",
        "252710": "TIGER 200선물인버스2X",
        "252720": "KBSTAR 모멘텀밸류",
        "252730": "KBSTAR 모멘텀로우볼",
        "253150": "ARIRANG 200선물레버리지",
        "253160": "ARIRANG 200선물인버스2X",
        "253230": "KOSEF 200선물인버스2X",
        "253240": "KOSEF 200선물인버스",
        "253250": "KOSEF 200선물레버리지",
        "253280": "KBSTAR 헬스케어",
        "253290": "KBSTAR 헬스케어채권혼합",
        "256440": "KINDEX 인도네시아MSCI(합성)",
        "256450": "ARIRANG 심천차이넥스트(합성)",
        "256750": "KODEX 차이나심천ChiNext(합성)",
        "261060": "TIGER 코스닥150IT",
        "261070": "TIGER 코스닥150바이오테크",
        "261110": "TIGER 미국달러선물레버리지",
        "261120": "TIGER 미국달러선물인버스2X",
        "261140": "TIGER 우선주",
        "261220": "KODEX WTI원유선물(H)",
        "261240": "KODEX 미국달러선물",
        "261250": "KODEX 미국달러선물레버리지",
        "261260": "KODEX 미국달러선물인버스2X",
        "261270": "KODEX 미국달러선물인버스",
        "261920": "KINDEX 필리핀MSCI(합성)",
        "265690": "KINDEX 러시아MSCI(합성)",
        "266160": "KBSTAR 고배당",
        "266360": "KODEX 미디어&엔터테인먼트",
        "266370": "KODEX IT",
        "266390": "KODEX 경기소비재",
        "266410": "KODEX 필수소비재",
        "266420": "KODEX 헬스케어",
        "266550": "ARIRANG 중형주저변동50",
        "267440": "KBSTAR 미국장기국채선물(H)",
        "267450": "KBSTAR 미국장기국채선물인버스(H)",
        "267490": "KBSTAR 미국장기국채선물레버리지(합성 H)",
        "267500": "KBSTAR 미국장기국채선물인버스2X(합성 H)",
        "267770": "TIGER 200선물레버리지",
        "269370": "TIGER S&P글로벌인프라(합성)",
        "269420": "KODEX S&P글로벌인프라(합성)",
        "269530": "ARIRANG S&P글로벌인프라",
        "269540": "ARIRANG 미국S&P500(H)",
        "270800": "KBSTAR KQ고배당",
        "270810": "KBSTAR 코스닥150",
        "271050": "KODEX WTI원유선물인버스(H)",
        "271060": "KODEX 3대농산물선물(H)",
        "272220": "KINDEX 스마트모멘텀",
        "272230": "KINDEX 스마트밸류",
        "272560": "KBSTAR 단기국공채액티브",
        "272570": "KBSTAR 중장기국공채액티브",
        "272580": "TIGER 단기채권액티브",
        "272910": "KINDEX 중장기국공채액티브",
        "273130": "KODEX 종합채권(AA-이상)액티브",
        "273140": "KODEX 단기변동금리부채권액티브",
        "275280": "KODEX MSCI모멘텀",
        "275290": "KODEX MSCI밸류",
        "275300": "KODEX MSCI퀄리티",
        "275750": "KBSTAR 코스닥150선물인버스",
        "275980": "TIGER 글로벌4차산업혁신기술(합성 H)",
        "276000": "TIGER 글로벌자원생산기업(합성 H)",
        "276650": "KBSTAR 글로벌4차산업IT(합성 H)",
        "276970": "KODEX 미국S&P고배당커버드콜(합성 H)",
        "276990": "KODEX 글로벌4차산업로보틱스(합성)",
        "277540": "KINDEX S&P아시아TOP50",
        "277630": "TIGER 코스피",
        "277640": "TIGER 코스피대형주",
        "277650": "TIGER 코스피중형주",
        "278240": "KBSTAR 코스닥150선물레버리지",
        "278420": "ARIRANG ESG우수기업",
        "278530": "KODEX 200TR",
        "278540": "KODEX MSCI Korea TR",
        "278620": "ARIRANG 단기채권액티브",
        "279530": "KODEX 고배당",
        "279540": "KODEX 최소변동성",
        "280320": "KINDEX 미국IT인터넷S&P(합성 H)",
        "280920": "ARIRANG 주도업종",
        "280930": "KODEX 미국러셀2000(H)",
        "280940": "KODEX 골드선물인버스(H)",
        "281990": "KBSTAR 중소형고배당",
        "282000": "KBSTAR 국고채3년선물인버스",
        "283580": "KODEX 차이나CSI300",
        "284430": "KODEX 200미국채혼합",
        "284980": "KBSTAR 200금융",
        "284990": "KBSTAR 200에너지화학",
        "285000": "KBSTAR 200IT",
        "285010": "KBSTAR 200중공업",
        "285020": "KBSTAR 200철강소재",
        "285690": "FOCUS ESG리더스",
        "287180": "ARIRANG 미국나스닥테크",
        "287300": "KBSTAR 200건설",
        "287310": "KBSTAR 200경기소비재",
        "287320": "KBSTAR 200산업재",
        "287330": "KBSTAR 200생활소비재",
        "289040": "KODEX MSCI KOREA ESG유니버설",
        "289250": "TIGER MSCI KOREA ESG유니버설",
        "289260": "TIGER MSCI KOREA ESG리더스",
        "289480": "TIGER 200커버드콜ATM",
        "289670": "ARIRANG 국채선물10년",
        "290080": "KBSTAR 200고배당커버드콜ATM",
        "290130": "KBSTAR ESG사회책임투자",
        "291130": "KINDEX 멕시코MSCI(합성)",
        "291620": "KOSEF 코스닥150선물인버스",
        "291630": "KOSEF 코스닥150선물레버리지",
        "291680": "KBSTAR 차이나H선물인버스(H)",
        "291890": "KODEX MSCI EM선물(H)",
        "292050": "KBSTAR KRX300",
        "292150": "TIGER TOP10",
        "292160": "TIGER KRX300",
        "292190": "KODEX KRX300",
        "292340": "마이티 200커버드콜ATM레버리지",
        "292500": "SOL KRX300",
        "292560": "TIGER 일본엔선물",
        "292730": "FOCUS KRX300",
        "292750": "ARIRANG KRX300",
        "292770": "KODEX 국채선물3년인버스",
        "293180": "HANARO 200",
        "294400": "KOSEF 200TR",
        "295000": "KBSTAR 국채선물10년",
        "295020": "KBSTAR 국채선물10년인버스",
        "295040": "SOL 200TR",
        "295820": "ARIRANG 200동일가중",
        "298340": "ARIRANG 국채선물3년",
        "298770": "KODEX 한국대만IT프리미어",
        "299070": "KINDEX 국채선물10년인버스",
        "299080": "KINDEX 국채선물3년인버스",
        "300610": "TIGER K게임",
        "300640": "KBSTAR 게임테마",
        "300950": "KODEX 게임산업",
        "301400": "ARIRANG 코스닥150",
        "301410": "ARIRANG 코스닥150선물인버스",
        "301440": "ARIRANG 코스피중형주",
        "302190": "TIGER 중장기국채",
        "302450": "KBSTAR 코스피",
        "304660": "KODEX 미국채울트라30년선물(H)",
        "304670": "KODEX 미국채울트라30년선물인버스(H)",
        "304760": "HANARO KRX300",
        "304770": "HANARO 코스닥150",
        "304780": "HANARO 200선물레버리지",
        "304940": "KODEX 미국나스닥100선물(H)",
        "305050": "KINDEX 코스피",
        "305080": "TIGER 미국채10년선물",
        "305540": "TIGER 2차전지테마",
        "305720": "KODEX 2차전지산업",
        "306520": "HANARO 200선물인버스",
        "306530": "HANARO 코스닥150선물레버리지",
        "306950": "KODEX KRX300레버리지",
        "307010": "KBSTAR KRX300레버리지",
        "307510": "TIGER 의료기기",
        "307520": "TIGER 지주회사",
        "308620": "KODEX 미국채10년선물",
        "309210": "ARIRANG KRX300헬스케어",
        "309230": "KINDEX 미국WideMoat가치주",
        "310080": "KBSTAR 중국MSCI China(H)",
        "310960": "TIGER 200TR",
        "310970": "TIGER MSCI Korea TR",
        "314250": "KODEX 미국FANG플러스(H)",
        "314700": "HANARO 농업융복합산업",
        "315270": "TIGER 200커뮤니케이션서비스",
        "315480": "KBSTAR 200커뮤니케이션서비스",
        "315930": "KODEX Top5PlusTR",
        "315960": "KBSTAR 대형고배당10TR",
        "316300": "KINDEX 싱가포르리츠",
        "316670": "KOSEF 코스닥150",
        "319640": "TIGER 골드선물(H)",
        "319870": "KBSTAR KRX300미국달러선물혼합",
        "321410": "KODEX 멀티에셋하이인컴(H)",
        "322120": "KINDEX 스마트퀄리티",
        "322130": "KINDEX 스마트로우볼",
        "322150": "KINDEX 스마트하이베타",
        "322400": "HANARO e커머스",
        "322410": "HANARO 고배당",
        "325010": "KODEX Fn성장",
        "325020": "KODEX 배당가치",
        "326230": "KBSTAR 내수주플러스",
        "326240": "KBSTAR IT플러스",
        "328370": "ARIRANG 코스피TR",
        "329200": "TIGER 부동산인프라고배당",
        "329650": "KODEX TRF3070",
        "329660": "KODEX TRF5050",
        "329670": "KODEX TRF7030",
        "329750": "TIGER 미국달러단기채권액티브",
        "331910": "KOSEF Fn중소형",
        "332500": "KINDEX 200TR",
        "332610": "ARIRANG 미국단기우량회사채",
        "332620": "ARIRANG 미국장기우량회사채",
        "332930": "HANARO 200TR",
        "332940": "HANARO MSCI Korea TR",
        "333940": "ARIRANG KS로우볼가중TR",
        "333950": "ARIRANG KS로우사이즈가중TR",
        "333960": "ARIRANG KS모멘텀가중TR",
        "333970": "ARIRANG KS밸류가중TR",
        "333980": "ARIRANG KS퀄리티가중TR",
        "334690": "KBSTAR 팔라듐선물(H)",
        "334700": "KBSTAR 팔라듐선물인버스(H)",
        "336160": "KBSTAR 금융채액티브",
        "337120": "KODEX Fn멀티팩터",
        "337140": "KODEX 코스피대형주",
        "337150": "KODEX 200exTOP",
        "337160": "KODEX 200ESG",
        "341850": "TIGER KIS부동산인프라채권TR",
        "342140": "KINDEX 모닝스타싱가포르리츠채권혼합",
        "346000": "HANARO KAP초장기국고채",
        "352540": "KODEX TSE일본리츠(H)",
        "352560": "KODEX 다우존스미국리츠(H)",
        "354240": "KBSTAR 미국고정배당우선증권ICE TR",
        "354350": "HANARO 글로벌럭셔리S&P(합성)",
        "354500": "KINDEX 코스닥150",
        "356540": "KINDEX KIS종합채권(AA-이상)액티브",
        "357870": "TIGER CD금리투자KIS(합성)",
        "359210": "KODEX 코스피TR",
        "360140": "KODEX 200롱코스닥150숏선물",
        "360150": "KODEX 코스닥150롱코스피200숏선물",
        "360200": "KINDEX 미국S&P500",
        "360750": "TIGER 미국S&P500",
        "361580": "KBSTAR 200TR",
        "361590": "KBSTAR 코스피ex200",
        "363510": "SOL KIS단기통안채",
        "363570": "KODEX 장기종합채권(AA-이상)액티브KAP",
        "363580": "KODEX 200IT TR",
        "364690": "KODEX 혁신기술테마액티브",
        "364960": "TIGER KRX BBIG K-뉴딜",
        "364970": "TIGER KRX바이오K-뉴딜",
        "364980": "TIGER KRX2차전지K-뉴딜",
        "364990": "TIGER KRX게임K-뉴딜",
        "365000": "TIGER KRX인터넷K-뉴딜",
        "365040": "TIGER AI코리아그로스액티브",
        "365780": "KINDEX 국고채10년",
        "367380": "KINDEX 미국나스닥100",
        "367740": "HANARO Fn5G산업",
        "367760": "KBSTAR Fn5G테크",
        "367770": "KBSTAR Fn수소경제테마",
        "368190": "HANARO Fn K-뉴딜디지털플러스",
        "368200": "KBSTAR Fn K-뉴딜디지털플러스",
        "368470": "KINDEX Fn K-뉴딜디지털플러스",
        "368590": "KBSTAR 미국나스닥100",
        "368680": "KODEX Fn K-뉴딜디지털플러스",
        "371130": "KINDEX 블룸버그베트남VN30선물레버리지(H)",
        "371150": "KBSTAR 차이나항셍테크",
        "371160": "TIGER 차이나항셍테크",
        "371450": "TIGER 글로벌클라우드컴퓨팅INDXX",
        "371460": "TIGER 차이나전기차SOLACTIVE",
        "371470": "TIGER 차이나바이오테크SOLACTIVE",
        "371870": "KINDEX 차이나항셍테크",
        "372330": "KODEX 차이나항셍테크",
        "373490": "KODEX K-이노베이션액티브",
        "373530": "ARIRANG 신흥국MSCI인버스(합성 H)",
        "373790": "KOSEF 미국방어배당성장나스닥",
        "375270": "KBSTAR 글로벌데이터센터리츠나스닥(합성)",
        "375760": "HANARO 탄소효율그린뉴딜",
        "375770": "KODEX 탄소효율그린뉴딜",
        "376250": "ARIRANG 탄소효율그린뉴딜",
        "376410": "TIGER 탄소효율그린뉴딜",
        "377990": "TIGER Fn신재생에너지",
        "379780": "KBSTAR 미국S&P500",
        "379790": "KBSTAR 유로스탁스50(H)",
        "379800": "KODEX 미국S&P500TR",
        "379810": "KODEX 미국나스닥100TR",
        "380340": "KINDEX Fn5G플러스",
        "381170": "TIGER 미국테크TOP10 INDXX",
        "381180": "TIGER 미국필라델피아반도체나스닥",
        "381560": "HANARO Fn전기&수소차",
        "381570": "HANARO Fn친환경에너지",
        "385510": "KODEX K-신재생에너지액티브",
        "385520": "KODEX K-미래차액티브",
        "385540": "KBSTAR KIS종합채권(A-이상)액티브",
        "385550": "KBSTAR KIS단기종합채권(AA-이상)액티브",
        "385560": "KBSTAR KIS국고채30년Enhanced",
        "385590": "네비게이터 ESG액티브",
        "385600": "네비게이터 친환경자동차밸류체인액티브",
        "385710": "TIMEFOLIO BBIG액티브",
        "385720": "TIMEFOLIO Kstock액티브",
        "387270": "TIGER 글로벌BBIG액티브",
        "387280": "TIGER 퓨처모빌리티액티브",
        "388280": "KBSTAR Fn컨택트대표",
        "388420": "KBSTAR 비메모리반도체액티브",
        "390390": "KODEX 미국반도체MV",
        "390400": "KODEX 미국스마트모빌리티S&P",
        "390950": "HANARO 단기채권액티브",
        "391590": "KINDEX 미국스팩&IPO INDXX",
        "391600": "KINDEX 미국친환경그린테마INDXX",
        "391670": "HK 베스트일레븐액티브",
        "391680": "HK 하이볼액티브",
        "394340": "KOSEF 릭소글로벌디지털경제MSCI",
        "394350": "KOSEF 릭소글로벌퓨처모빌리티MSCI",
        "394660": "TIGER 글로벌자율주행&전기차SOLACTIVE",
        "394670": "TIGER 글로벌리튬&2차전지SOLACTIVE(합성)",
        "395150": "KODEX Fn웹툰&드라마",
        "395160": "KODEX Fn시스템반도체",
        "395170": "KODEX Fn Top10동일가중",
        "395270": "HANARO Fn K-반도체",
        "395280": "HANARO Fn K-게임",
        "395290": "HANARO Fn K-POP&미디어",
        "395750": "ARIRANG ESG가치주액티브",
        "395760": "ARIRANG ESG성장주액티브",
        "396500": "TIGER Fn반도체TOP10",
        "396510": "TIGER 차이나클린에너지SOLACTIVE",
        "396520": "TIGER 차이나반도체FACTSET",
        "397410": "KBSTAR 국채선물5년추종인버스",
        "397420": "KBSTAR 국채선물5년추종",
        "399110": "SOL 미국S&P500ESG",
        "399580": "KBSTAR 글로벌클린에너지S&P",
        "400570": "KODEX 유럽탄소배출권선물ICE(H)",
        "400580": "SOL 유럽탄소배출권선물S&P(H)",
        "400590": "SOL 글로벌탄소배출권선물IHS(합성)",
        "400970": "TIGER Fn메타버스",
        "401170": "KBSTAR iSelect메타버스",
        "401470": "KODEX K-메타버스액티브",
        "401590": "HANARO 글로벌탄소배출권선물ICE(합성)",
        "402460": "HANARO Fn K-메타버스MZ",
        "402520": "FOCUS 혁신기업액티브",
        "402970": "KINDEX 미국고배당S&P",
        "403790": "마이다스 KoreaStock액티브",
        "403990": "KBSTAR KRX기후변화솔루션",
        "404120": "TIMEFOLIO 탄소중립액티브",
        "404260": "KODEX KRX기후변화솔루션",
        "404470": "HANARO KRX기후변화솔루션",
        "404540": "TIGER KRX기후변화솔루션",
        "404650": "SOL KRX기후변화솔루션",
        "407160": "MASTER 테크미디어텔레콤액티브",
        "407170": "MASTER 스마트커머스액티브",
        "407300": "HANARO Fn골프테마",
        "407310": "HANARO 200 TOP10",
        "407820": "에셋플러스 코리아플랫폼액티브",
        "407830": "에셋플러스 글로벌플랫폼액티브",
        "409810": "KODEX 미국나스닥100선물인버스(H)",
        "409820": "KODEX 미국나스닥100레버리지(합성 H)",
        "410870": "TIMEFOLIO K컬처액티브",
        "411050": "네비게이터 글로벌메타버스테크액티브",
        "411060": "KINDEX KRX금현물",
        "411420": "KODEX 미국메타버스나스닥액티브",
        "411540": "SOL 200 TOP10",
        "411720": "KBSTAR 글로벌메타버스Moorgate",
        "411860": "KOSEF 독일DAX",
        "412560": "TIGER KRX BBIG K-뉴딜레버리지",
        "412570": "TIGER KRX2차전지K-뉴딜레버리지",
        "412770": "TIGER 글로벌메타버스액티브",
        "413220": "SOL 차이나태양광CSI(합성)",
        "413930": "WOORI AI ESG액티브",
        "414270": "KINDEX G2전기차&자율주행액티브",
        "414780": "TIGER 차이나과창판STAR50(합성)",
        "415340": "KODEX 차이나과창판STAR50(합성)",
        "415760": "SOL 차이나육성산업액티브(합성)",
        "415920": "ARIRANG 글로벌희토류전략자원기업MV",
        "416090": "KINDEX 중국과창판STAR50",
        "417450": "KBSTAR 글로벌수소경제Indxx",
        "417630": "TIGER KEDI혁신기업ESG30",
        "418660": "TIGER 미국나스닥100레버리지(합성)",
        "418670": "TIGER 글로벌사이버보안INDXX",
        "419170": "HANARO 미국메타버스iSelect",
        "419650": "ARIRANG 글로벌수소&차세대연료전지MV",
        "153360": "하이골드3호",
        "155900": "바다로19호",
    }