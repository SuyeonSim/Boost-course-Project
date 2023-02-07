import cs1graphics
import time

canvas = cs1graphics.Canvas(400, 300)
# 폭 400, 너비 300의 직사각형을 만들어낸다.
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

car = cs1graphics.Layer()

tire1 = cs1graphics.Circle(10, cs1graphics.Point(30, 120))
tire1.setFillColor('black')
car.add(tire1)

tire2 = cs1graphics.Circle(10, cs1graphics.Point(70, 120))
tire2.setFillColor('black')
car.add(tire2)

body = cs1graphics.Rectangle(70, 30, cs1graphics.Point(50, 100))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)

canvas.add(car)


for i in range(30):
    car.move(2, 0)
    time.sleep(0.1)
for i in range(22):
    car.rotate(1)
    time.sleep(0.1)
for i in range(30):
    car.move(2, 1)
    time.sleep(0.1)
for i in range(22):
    car.rotate(-1)
    time.sleep(0.1)
for i in range(30):
    car.move(2, 0)
    time.sleep(0.1)
for i in range(30):
    car.scale(1.05)
    time.sleep(0.1)