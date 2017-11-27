from PIL import Image

image = Image.open("cat.jpg")

width = image.size[0]
height = image.size[1]

# weight to determine how bright to make the blacklight
# number between 1 and 7 with an optimal value of 2
fx_weight = 7

for y in range(0, height):
    for x in range(0, width):
        color = image.getpixel((x, y))
        red = color[0]
        green = color[1]
        blue = color[2]

        # compute the human-eye friendly luminance
        luminance = (222 * red + 707 * green + 71 * blue) / 1000

        # compute now color values
        red = abs(red - luminance) * fx_weight
        green = abs(green - luminance) * fx_weight
        blue = abs(blue - luminance) * fx_weight

        # make sure that new color values are integers below 256
        red = min(int(red), 255)
        green = min(int(green), 255)
        blue = min(int(blue), 255)

        image.putpixel((x, y), (red, green, blue))

image.show()
