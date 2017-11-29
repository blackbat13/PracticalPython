from PIL import Image
import random

image = Image.open("cat.jpg")

width = image.size[0]
height = image.size[1]

maxDistance = 10

for _ in range(0, int(width * height / 2)):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    point1 = (x, y)
    x += random.randint(-maxDistance, maxDistance)
    y += random.randint(-maxDistance, maxDistance)
    if x < 0 or x >= width or y < 0 or y >= height:
        continue

    point2 = (x, y)
    color1 = image.getpixel(point1)
    color2 = image.getpixel(point2)

    image.putpixel(point1, color2)
    image.putpixel(point2, color1)

image.show()
