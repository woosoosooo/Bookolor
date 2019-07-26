from pprint import pprint
from decouple import config
import requests, csv, time

BASE_URL = 'https://openapi.naver.com/v1/search/book_adv'
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
HEADER = {
    'X-Naver-Client-Id': NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
}  # header : 요청에 대한 정보가 담긴다 

display = 100   # 검색 결과 출력 건수 지정 default = 10 / 10 ~ 100
start = 1       # 검색 시작 위치 default = 1 / 1 ~ 1000 : 검색 시작 위치는 책 순서임, 페이지 순서가 아님.
                # 따라서 한 검색 옵션에서 가져올수 있는 최대 책은 1099권 
                # 출판사 검색어 '길벗' 기준으로 4345건이 나와서 다 가져올수가 없음.
sort ='sim'     # 정렬 옵션 default = sim(유사도순), date(출간일순), count(판매량순)
titl = ''       # 책 제목 검색 ''면 무시됨 
auth = ''       # 저자명 검색
cont = ''       # 목차 검색
isbn = ''       # isbn 검색
publ = '길벗'   # 출판사 검색 
dafr = ''       # 출간 시작일 ex.20000203
dato = ''       # 출간 종료일
catg = ''       # 책 검색 카테고리 / 카테고리 목록은 네이버 개발자 사이트 가서 확인하세요.

with open ('book_list_gil.csv', 'w', newline='', encoding='utf-8') as f:

    fieldnames = ('isbn', 'title', 'image URL', 'description')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  

    for start_num in range(0, 10):

        start = (start_num*100) + 1
    
        API_URL = f'{BASE_URL}?display={display}&start={start}&sort={sort}&d_titl={titl}&d_auth={auth}&d_cont={cont}&d_isbn={isbn}&d_publ={publ}&d_dafr={dafr}&d_dato={dato}&d_catg={catg}'
        books = requests.get(API_URL, headers=HEADER).json()
        books_list = books.get('items')

        time.sleep(1)

        for i in range(len(books_list)):
            book_dict = {
                'isbn': books_list[i].get('isbn'),
                'title': books_list[i].get('title'),
                'image URL': books_list[i].get('image'),
                'description': books_list[i].get('description'),
                }
            writer.writerow(book_dict)
