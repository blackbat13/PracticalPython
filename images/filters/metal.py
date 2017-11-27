from PIL import Image

image = Image.open("cat.jpg")

width = image.size[0]
height = image.size[1]

for y in range(0, height):
    for x in range(0, width):
        color = image.getpixel((x, y))
        red = color[0]

        red = abs(red - 64)
        green = abs(red - 64)
        blue = abs(green - 64)

        gray = (red * 222 + green * 707 + blue * 71) / 1000

        red = gray + 70
        red = 2 * red - 128
        green = gray + 65
        green = 2 * green - 128
        blue = gray + 75
        blue = 2 * blue - 128
        red = min(int(red), 255)
        green = min(int(green), 255)
        blue = min(int(blue), 255)

        image.putpixel((x, y), (red, green, blue))

image.show()
