from PIL import Image

image = Image.open("cat.jpg")

width = image.size[0]
height = image.size[1]

for y in range(0, height):
    for x in range(0, width):
        color = image.getpixel((x, y))
        red = color[0]
        green = color[1]
        blue = color[2]

        red = 255 - red
        green = 255 - green
        blue = 255 - blue

        image.putpixel((x, y), (red, green, blue))

image.show()
