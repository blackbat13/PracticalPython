from PIL import Image, ImageDraw

im = Image.open("filters/cat.jpg")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=(0,0,255))
draw.line((0, im.size[1], im.size[0], 0), fill=(0,0,255))
del draw

# write to stdout
im.show()