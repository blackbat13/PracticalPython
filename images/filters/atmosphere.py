from PIL import Image

image = Image.open("cat.jpg")

width, height = image.size

for y in range(0, height):
    for x in range(0, width):
        red, green, blue = image.getpixel((x, y))

        red_new = (green + blue) / 2
        green_new = (red + blue) / 2
        blue_new = (red + green) / 2
        red = int(red_new)
        green = int(green_new)
        blue = int(blue_new)

        image.putpixel((x, y), (red, green, blue))

image.show()
