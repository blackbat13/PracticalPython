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

        # We shift color values one to the right
        # We replace red with blue, green with red and blue with green
        image.putpixel((x, y), (blue, red, green))

image.show()
