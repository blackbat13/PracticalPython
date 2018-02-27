from PIL import Image, ImageEnhance

def change(px):
    return 0

image1 = Image.open("filters/cat.jpg")
image2 = Image.open("filters/cat2.jpg")

# image2 = image2.crop((0, 0, image1.size[0], image1.size[1]))
image2 = image2.resize(image1.size)

image3 = Image.blend(image1, image2, 0.6)

image3.show()

# image2 = Image.eval(image2, lambda px: 0 if px <= 60 else px)
# image2 = Image.eval(image2, lambda px: min(255, px+100))
image2 = Image.eval(image2, change)
image2.show()

image1 = ImageEnhance.Color(image1)
image1.enhance(0.5).show()

