from PIL import Image, ImageDraw
import random

image = Image.open("cat.jpg")
draw = ImageDraw.Draw(image)

width = image.size[0]
height = image.size[1]

maxDistance = 5

for _ in range(0, 100000):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    point1 = (x, y)
    x += random.randint(-maxDistance, maxDistance)
    y += random.randint(-maxDistance, maxDistance)
    if x < 0 or x >= width or y < 0 or y >= height:
        continue

    point2 = (x, y)
    x += random.randint(-maxDistance, maxDistance)
    y += random.randint(-maxDistance, maxDistance)
    if x < 0 or x >= width or y < 0 or y >= height:
        continue

    point3 = (x, y)
    color1 = image.getpixel(point1)
    color2 = image.getpixel(point2)
    color3 = image.getpixel(point3)
    red = (color1[0] + color2[0] + color3[0]) / 3
    green = (color1[1] + color2[1] + color3[1]) / 3
    blue = (color1[2] + color2[2] + color3[2]) / 3
    red = int(red)
    green = int(green)
    blue = int(blue)

    draw.polygon([point1, point2, point3], (red, green, blue))

image.show()
