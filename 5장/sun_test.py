import math
import time
from cs1graphics import *


def interpolate_colors(t, color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (int((1 - t) * r1 + t * r2),
            int((1 - t) * g1 + t * g2),
            int((1 - t) * b1 + t * b2))


def color_value(color):
    return Color(color).getColorValue()


def animate_sunrise(sun, morning_sun, noon_sun, morning_sky, noon_sky):
    morning_color = color_value(morning_sun)
    noon_color = color_value(noon_sun)
    dark_sky = color_value(morning_sky)  # 새벽녘을 표현한 것이라고 생각하면 될듯. 아침(어두움) -> 낮(밝아짐) -> 저녁(어두움)
    bright_sky = color_value(noon_sky)
    w = canvas.getWidth()
    h = canvas.getHeight()
    r = sun.getRadius()  # getradius가 없다.
    x0 = w / 2.0
    y0 = h + r
    xradius = w / 2.0 - r  # 원의 중심값 x
    yradius = h
    for angle in range(181):
        rad = (angle / 180.0) * math.pi
        t = math.sin(rad)
        col = interpolate_colors(t, morning_color, noon_color)
        sun.setFillColor(col)
        sun.setBorderColor(col)
        col = interpolate_colors(t, dark_sky, bright_sky)
        canvas.setBackgroundColor(col)
        x = x0 - xradius * math.cos(rad)
        y = y0 - yradius * math.sin(rad)
        sun.moveTo(x, y)
        time.sleep(0.05)


canvas = Canvas(600, 200)

sun = Circle(30)
canvas.add(sun)

animate_sunrise(sun, "dark orange", "yellow", "dark blue", "deepskyblue")

canvas.close()
