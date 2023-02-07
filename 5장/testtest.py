import cs1graphics
import time

canvas = cs1graphics.Canvas(400, 300)
# 폭 400, 너비 300의 직사각형을 만들어낸다.
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

car = cs1graphics.Layer()

sq = cs1graphics.Rectangle(70, 30, cs1graphics.Point(100,100))
sq.setFillColor("blue")
sq.setBorderColor("black")
sq.setBorderWidth(1)
# sq.move(50, 50)
# 오른쪽으로 50pixel, 아래쪽으로 50pixel 옮겨감.
car.add(sq)
# car 레이어에 추가

tire1 = cs1graphics.Circle(10, cs1graphics.Point(-20, -10))

canvas.add(car)