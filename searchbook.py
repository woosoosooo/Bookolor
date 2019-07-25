from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote
from decouple import config  # shell 에서 pip install python-decouple
import json, pprint

NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')


# 출판사 기준 검색, 옵션은 추가 예정 
def search_publ(publ):

    request = Request('https://openapi.naver.com/v1/search/book_adv?d_publ='+quote(publ))
    request.add_header('X-Naver-Client-Id', NAVER_CLIENT_ID)
    request.add_header('X-Naver-Client-Secret', NAVER_CLIENT_SECRET)

    response = urlopen(request).read().decode('utf-8')
    search_result = json.loads(response)

    return search_result

if __name__ == '__main__':

    pprint.pprint(search_publ('길벗'))


# 도서명 기준 검색 
def search_book(book):
    
    request = Request('https://openapi.naver.com/v1/search/book?query='+quote(book))
    request.add_header('X-Naver-Client-Id', NAVER_CLIENT_ID)
    request.add_header('X-Naver-Client-Secret', NAVER_CLIENT_SECRET)

    response = urlopen(request).read().decode('utf-8')
    search_result = json.loads(response)

    return search_result

if __name__ == "__main__":

    pprint.pprint(search_book('라플라스의 마녀'))
