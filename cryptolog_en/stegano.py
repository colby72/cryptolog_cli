# This code is the property of Ramy Chmak
# ---------------------------------------

# -*- coding: utf-8 -*-

import Image
import stepic

def crypt(pic, text):
	img = Image.open(pic)
	imgg = stepic.encode(img, text)
	imgg.save('stegano.bmp', 'BMP')
def decrypt(pic):
	img = Image.open(pic)
	s = stepic.decode(img)
	d = s.decode()
	return d

print "This is a steganography program"
print "Please make sure the picture have the extension .bmp"
print "----------------------------------------------------\n"
print "1- Coding a picture"
print "2- Decoding a picture\n"
choix = ""
while choix!='1' and choix!='2':
	choix = raw_input("Choose the service you want : ")
if choix == '1':
	imin = raw_input("Enter the picture's name : ")
	textin = raw_input("Enter the text to hide : ")
	crypt(imin, textin)
	print "Your coded picture has been generated : stegano.bmp"
elif choix == '2':
	imin = raw_input("Enter the picture's name : ")
	textout = decrypt(imin)
	print textout
