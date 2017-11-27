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

        red = (green + blue) / 2
        green = (red + blue) / 2
        blue = (red + green) / 2
        red = int(red)
        green = int(green)
        blue = int(blue)

        image.putpixel((x, y), (red, green, blue))

image.show()
