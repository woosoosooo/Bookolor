from pprint import pprint
from sklearn.cluster import KMeans
import csv, cv2
import numpy as np 
import matplotlib.pyplot as plt 

with open('book_list_gil_160.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    booknames_list = []

    for row in reader:
        if '부동산' in row['title']:
            booknames_list.append([row['title'], row['isbn']])

# 이미지 리스트 딕트화, 실제로 쓸 때는 위 코드랑 합쳐서 간소화할 예정 
# img_dict = {}
# for i in booknames_list:
#     img_dict.update({i[1]: cv2.imread(f'bookcovers_160/{i[1]}.jpg')})

img = cv2.imread('bookcovers_160/8975604810 9788975604812.jpg')

# 이미지 보는 법
# cv2.imshow('original', img)
# cv2.waitKey(0)

# 이미지 정보 확인 (height, width, channel) / 행렬
# print(img.shape)
# print(img)

# 이미지 정보 RGB로 바꾼후 픽셀 한줄로 만들기 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.reshape((img.shape[0] * img.shape[1], 3))
# print(img.shape)


# 색 5개 추출 / 너무 많거나 적으면 결과값이 안 좋음 일단은 5-7개가 적당한듯..
k = 5
clt = KMeans(n_clusters=k)
clt.fit(img)

for center in clt.cluster_centers_:
    print(center)


# 추출된 색의 비율 확인  함수 
def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype('float')
    hist /= hist.sum()

    return hist


hist = centroid_histogram(clt)
print(hist)


# 색을 차트로 확인 
def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype='uint8')
    startX = 0

    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype('uint8').tolist(), -1)

    return bar


bar = plot_colors(hist, clt.cluster_centers_)

plt.figure()
plt.axis('off')
plt.imshow(bar)
plt.show()
