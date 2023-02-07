import cs1graphics
import time

canvas = cs1graphics.Canvas(400, 300)
# 폭 400, 너비 300의 직사각형을 만들어낸다.
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

sq = cs1graphics.Square(100)
# 너비 100의 정사각형을 생성한다.
canvas.add(sq)
# 생성해서 canvas 직사각형에 sq를 add 해줌.
# add도 cs1graphics의 함수인가보넹.

sq.setFillColor("blue")
sq.setBorderColor("red")
sq.setBorderWidth(5)
sq.moveTo(200, 200)
# sq 정사각형을 이렇게 저렇게 꾸며준 후, x좌표: 200 - y좌표: 200으로 옮겨줌.

# for i in range(100):
#     sq.move(1, 0)
#
#     time.sleep(0.1)

r = cs1graphics.Rectangle(150, 75)
canvas.add(r)
# canvas에 r이라는 직사각형을 하나 더해준다.

r.setFillColor("yellow")
r.setBorderColor("black")
r.moveTo(280, 150)

sq.setDepth(10)
r.setDepth(20)
# 나중에 넣어준 r 직사각형을 뒤로 들어가게 하기 위해 Depth를 줌.
#
for i in range(80):
    sq.scale(0.95)
    # 폭이 5%씩 작아짐. 100->95->...
    time.sleep(0.1)
canvas.remove(sq)
# 영화에서 자주 쓰이는 Fade-out 효과