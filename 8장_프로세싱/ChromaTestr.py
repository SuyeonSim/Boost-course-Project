from PIL import Image
import cs1media
import math

def dist(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

def chroma(img, key, threshold):
    w, h = img.size()
    # 이미지의 크기를 .size를 이용하여 얻어옴
    for y in range(h):
        for x in range(w):
            p = img.get(x, y)
            # get 함수란 ?
            if dist(p, key) < threshold:
                img.set(x, y, cs1media.Color.yellow)

def chroma_paste(canvas, img, x1, y1, key):
    # canvas = 풍경 사진, img = 따올 이미지(여기서는 노란색 배경색으로 바꿔준 장영실 사진), key = 배경색(노란색), x1 = 이미지를 따올 x 좌표의 위치, y1 = 이미지를 따올 y 좌표의 위치
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            p = img.get(x, y)
            if p != key: # 만약 p가 yellow가 아니라면,
                canvas.set(x1 + x, y1 + y, p) # (x1, y1, p)로만 했을 때는 아예 paste가 되지 않았음! 오우 쓌 방금 깨달았다. 왼쪽에 보이는 것처럼 해버리면 한 점(x1, y1)에만 paste가 됨. 그래서 x와 y를 더해줘야 하는 거였다.


def hide_picture(canvas, img, bwing): # bwing = 로봇 설계도
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1:
                r = r - 1
                # 만약에 r이 홀수면 r - 1을 하여 짝수로 만든다.
                img.set(x, y, (r, g, b))

    black = (0, 0, 0)
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if bwing.get(x, y) == black:
                r = r + 1
                canvas.set(x, y, (r, g, b))
                # 정보 은닉 완료.


black = (0, 0, 0)
white = (255, 255, 255)

def restore_picture(canvas, img):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            # canvas의 rgb 값을 확인하여 그 값이 홀수이면 black으로, 짝수이면 그냥 둔다.
            if r % 2 == 1:
                canvas.set(x, y, black)
            else:
                canvas.set(x, y, white)

img = cs1media.load_picture("C:/Users/수연/Desktop/파이썬_부스트코스/photos/statue1.jpg")
canvas = cs1media.load_picture("C:/Users/수연/Desktop/파이썬_부스트코스/photos/trees1.jpg")
robotimg = cs1media.load_picture("C:/Users/수연/Desktop/파이썬_부스트코스/8장_로봇설계도.jpg")
chroma(img, (41, 75, 146), 70)
img.show()
# 장영실 이미지의 배경색이 노란색으로 변함
chroma_paste(canvas, img, 200, 50, cs1media.Color.yellow)
hide_picture(canvas, img, robotimg)
canvas.show()
restore_picture(canvas, img)
canvas.show()