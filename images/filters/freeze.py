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

        red = abs((red - green - blue) * 1.5)
        green = abs((green - blue - red) * 1.5)
        blue = abs((blue - red - green) * 1.5)
        red = min(int(red), 255)
        green = min(int(red), 255)
        blue = min(int(red), 255)

        image.putpixel((x, y), (red, green, blue))

image.show()
