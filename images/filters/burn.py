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

        gray = (red + green + blue) / 3

        red = gray * 3
        green = gray
        blue = gray / 3
        red = int(red)
        red = min(red, 255)
        green = int(green)
        blue = int(blue)

        image.putpixel((x, y), (red, green, blue))

image.show()
