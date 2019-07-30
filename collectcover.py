from pprint import pprint
from decouple import config
import requests, csv, time

BASE_URL = 'https://openapi.naver.com/v1/search/book_adv'
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
HEADER = {
    'X-Naver-Client-Id': NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
} 

with open('book_list_gil_160.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    bookcovers_list = []

    for row in reader:
        bookcovers_list.append([row['image URL'], row['isbn']])

for bookcover in bookcovers_list:

    with open(f'bookcovers_160/{bookcover[1]}.jpg', 'wb') as f:
        response = requests.get(bookcover[0])
        f.write(response.content)
