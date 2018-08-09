import os
from PIL import Image
from PIL import ImageFilter

while True:
	print("1. Rotate Image /n 2.change colour of image/n 3.Convert Image to Black and White /n 4. Change the size/n 5.Blur the Image /n")
	ch=int(input("enter index num:"))

	if ch==1:
		im=Image.open("images_i/5.jpg")
		out=im.transpose(Image.ROTATE_90)
		out.show()

	elif ch==2:
		im= Image.open("images_i/5.jpg")
		source = im.split()
		R, G, B = 0, 0, 1
		mask = source[B].point(lambda i: i < 100 and 255)
		source[B].paste(mask)
		im = Image.merge(im.mode, source)
		im.show()

	elif ch==3:
		im=Image.open("images_i/5.jpg")
		bw=im.convert('L')
		bw.show()

	elif ch==4:
		size=(450,450)
		for f in os.listdir("images_i"):
			if f.endswith(".jpg"):
 				im =Image.open("images_i/"+str(f))
	 			filename, file_extn= os.path.splitext(f)
	 			im.thumbnail(size)
	 			im.show()
	elif ch==5:
		im=Image.open("images_i/5.jpg")
		blurred = im.filter(ImageFilter.BLUR)
		blurred = blurred.filter(ImageFilter.BLUR)

		blurred.show()	