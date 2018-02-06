from PIL import Image, ImageEnhance

image = Image.open("filters/cat.jpg")

colorEnhancer = ImageEnhance.Color(image)
colorEnhancer.enhance(0.5).show("Enhanced color with factor 0.5")

contrastEnhancer = ImageEnhance.Contrast(image)
contrastEnhancer.enhance(0.5).show("Enhanced contrast with factor 0.5")

brightnessEnhancer = ImageEnhance.Brightness(image)
brightnessEnhancer.enhance(0.5).show("Enhanced brightness with factor 0.5")

sharpnessEnhancer = ImageEnhance.Sharpness(image)
sharpnessEnhancer.enhance(0.5).show("Enhanced sharpness with factor 0.5")