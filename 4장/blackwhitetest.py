from PIL import Image

def blackwhitetest(img):
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            rgb = img.getpixel((i, j))
            rgb = round((rgb[0] + rgb[1] + rgb[2]) / 3)
            img.putpixel((i, j), (rgb, rgb, rgb))
    img.show()

img = Image.open("C:/Users/수연/PycharmProjects/bc_python/Growl.jpg")
blackwhitetest(img)
