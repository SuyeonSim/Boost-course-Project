import cs1media
from PIL import Image

def hide_picture(img, bwimg): # bwing = 로봇 설계도
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1:
                r = r - 1
                # 만약에 r이 홀수면 r - 1을 하여 짝수로 만든다.
            img.set(x, y, (r, g, b))

    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if bwimg.get(x, y) == black:
                r = r + 1
            img.set(x, y, (r, g, b))
            # 정보 은닉 완료.
# 로봇 이미지에서 black에 해당하는 곳을 img(x, y)에서 r 값을 짝수로 만들어줌
# 지금 설계도는 img에 숨겨져 있음

black = (0, 0, 0)
white = (255, 255, 255)

def restore_picture(img):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            # canvas의 rgb 값을 확인하여 그 값이 홀수이면 black으로, 짝수이면 white로 변경.
            if r % 2 == 1:
                img.set(x, y, black)

img = cs1media.load_picture("C:/Users/수연/Desktop/파이썬_부스트코스/photos/statue1.jpg")
robotimg = cs1media.load_picture("C:/Users/수연/Desktop/파이썬_부스트코스/8장_로봇설계도.jpg")


print(robotimg.size(), img.size())
hide_picture(img, robotimg)
img.show()
restore_picture(img)
img.show()
