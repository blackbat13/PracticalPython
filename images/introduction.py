# We use Pillow library to work with images
from PIL import Image

print("Loading image from file")
image = Image.open("filters/cat.jpg")

print("Showing loaded image")
image.show()

print(f"Image format is: {image.format}")
print(f"Image color mode is: {image.mode}")

print("Get the image size")
size = image.size

print(f"Image size is: {size}")
print("Size is returned as a tuple with two elements: (width, height)")
print(f"Width of the image is {size[0]} and height is {size[1]}")

print("Resizing image")

resized_image = image.resize((128, 128))
resized_image.show()

print("Rotating image")
rotated_image = image.rotate(45)
rotated_image.show()

print("Flipping image")
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.show()

print("Cropping image")
cropped_image = image.crop((300, 50, 600, 400))
cropped_image.show()
