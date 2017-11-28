from PIL import Image, ImageDraw
import random

image = Image.open("cat.jpg")
draw = ImageDraw.Draw(image)

width = image.size[0]
height = image.size[1]

maxDistance = 8

for _ in range(0, 100000):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    point1 = (x, y)
    distance = random.randint(-maxDistance, maxDistance)
    x += distance
    y += distance
    if x < 0 or x >= width or y < 0 or y >= height:
        continue

    point2 = (x, y)
    color1 = image.getpixel(point1)
    color2 = image.getpixel(point2)
    red = (color1[0] + color2[0]) / 2
    green = (color1[1] + color2[1]) / 2
    blue = (color1[2] + color2[2]) / 2
    red = int(red)
    green = int(green)
    blue = int(blue)

    draw.ellipse([point1, point2], (red, green, blue))

image.show()
