import os
from PIL import Image
from PIL import ImageFilter
from PIL import Image
from PIL import Image, ImageEnhance

im=Image.open("images_i/5.jpg")

contrast = ImageEnhance.Contrast(im)
contrast = contrast.enhance(FACTOR)
contrast.show()