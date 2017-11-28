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

        red = gray - green - blue
        green = gray - red - blue
        blue = gray - red - green
        red = min(max(int(red), 0), 255)
        green = min(max(int(green), 0), 255)
        blue = min(max(int(blue), 0), 255)

        image.putpixel((x, y), (red, green, blue))

image.show()
