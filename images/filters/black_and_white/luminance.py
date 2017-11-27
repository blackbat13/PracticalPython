from PIL import Image

image = Image.open("../cat.jpg")

width = image.size[0]
height = image.size[1]

for y in range(0, height):
    for x in range(0, width):
        color = image.getpixel((x, y))
        red = color[0]
        green = color[1]
        blue = color[2]

        gray = red * 0.3 + green * 0.59 + blue * 0.11
        gray = int(gray)
        image.putpixel((x, y), (gray, gray, gray))

image.show()
