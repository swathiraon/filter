import os
from PIL import Image,ImageTk
from PIL import ImageFilter

def rotate(i):
	p=[]
	im=Image.open(i)
	out=im.transpose(Image.ROTATE_90)
	image_tk = ImageTk.PhotoImage(out)
	p.append(out)
	p.append(image_tk)
	print(type(image_tk))
	return p
def bw(i):
	p=[]
	im=Image.open(i)
	bw1=im.convert('L')
	image_tk = ImageTk.PhotoImage(bw1)
	p.append(bw1)
	p.append(image_tk)
	print(type(image_tk))
	return p
def crop(i,length,width):
	size=(length,width)
	im =Image.open(i)
	im.thumbnail(size)
	return im
def blur1(i):
	p=[]
	im=Image.open(i)
	blurred = im.filter(ImageFilter.BLUR)
	blurred = blurred.filter(ImageFilter.BLUR)
	image_tk = ImageTk.PhotoImage(blurred)
	p.append(blurred)
	p.append(image_tk)
	return p
def contrast(i,factor):
	im=Image.open(i)
	c = ImageEnhance.Contrast(im)
	c = c.enhance(factor)
	return c
