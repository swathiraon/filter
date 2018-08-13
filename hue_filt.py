import os
from PIL import Image
from PIL import Image, ImageEnhance
import colorsys

while true:
	print("1.first\n 2.second\n 3.third\n 4.fourth\n")
	ch=int(input("enter:"))
# for contrast
	if ch=="1":
		img = Image.open('images_i/3.jpg')
		enhancer = ImageEnhance.Color(img)
		factor = 0.25
		enhancer.enhance(factor).show("Sharpness %f" % factor)
		factor = 1.0
		enhancer.enhance(factor).show("Sharpness %f" % factor)

#for brightness
	elif ch=="2":
		img=Image.open('images_i/3.jpg')
		enhancer=ImageEnhance.Brightness(img)
		factor=0.25
		enhancer.enhance(factor).show("Sharpness %f" % factor)
		factor=1.0
		enhancer.enhance(factor).show("Sharpness %f" % factor)

#for sharpness
	elif ch=="3":		
		img=Image.open('images_i/3.jpg')
		enhancer=ImageEnhance.Sharpness(img)
		factor=0.5
		enhancer.enhance(factor).show("Sharpness %f" % factor)
		factor=2.0
		enhancer.enhance(factor).show("Sharpness %f" % factor)

#for saturation/hue
	elif ch=="4":
		img = Image.open('images_i/3.jpg')    
		r,g,b = img.split()
		Hdat = []
		Ldat = []
		Sdat = []    
		for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()):
		    h,l,s = colorsys.rgb_to_hls(rd/255.,gn/255.,bl/255.)
		    Hdat.append(int(h*255.))
    		Ldat.append(int(l*255.))
		    Sdat.append(int(s*255.))

		r.putdata(Hdat)
		g.putdata(Ldat)
		b.putdata(Sdat)
		newimg = Image.merge('RGB',(r,g,b))
		newimg.show()




















