from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote
from decouple import config  # shell 에서 pip install python-decouple
import json, pprint

NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')

base_url = 'https://openapi.naver.com/v1/search/book_adv'
display = 10    # 검색 결과 출력 건수 지정 default = 10 / 10 ~ 100
start = 1       # 검색 시작 위치 default = 1 / 1 ~ 1000
sort ='sim'     # 정렬 옵션 default = sim(유사도순), date(출간일순), count(판매량순)
titl = ''       # 책 제목 검색 ''면 무시됨 
auth = ''       # 저자명 검색
cont = ''       # 목차 검색
isbn = ''       # isbn 검색
publ = '길벗'   # 출판사 검색 
dafr = ''       # 출간 시작일 ex.20000203
dato = ''       # 출간 종료일
catg = ''       # 책 검색 카테고리 / 카테고리 목록은 네이버 개발자 사이트 가서 확인하세요.

request = Request(f'{base_url}?display={display}&start={start}&sort={quote(sort)}&d_titl={quote(titl)}&d_auth={quote(auth)}&d_cont={quote(cont)}&d_isbn={quote(isbn)}&d_publ={quote(publ)}&d_dafr={quote(dafr)}&d_dato={quote(dato)}&d_catg={quote(catg)}')
request.add_header('X-Naver-Client-Id', NAVER_CLIENT_ID)
request.add_header('X-Naver-Client-Secret', NAVER_CLIENT_SECRET)

response = urlopen(request).read().decode('utf-8')
search_result = json.loads(response)

pprint.pprint(search_result)
