from pprint import pprint
import csv, cv2

with open('book_list_gil_160.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    booknames_list = []

    for row in reader:
        if '부동산' in row['title']:
            booknames_list.append([row['title'], row['isbn']])

# for i in booknames_list:
#     globals()['img{}'.format(i[1])] = cv2.imread(f'bookcovers_160/{i[1]}.jpg')

img = cv2.imread('bookcovers_160/1160500843 9791160500844.jpg')
# cv2.imshow('original', img)
# cv2.waitKey(0)

print(img.shape)
print(img)
