# This code is the property of Ramy Chmak
# ---------------------------------------

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

print "Ceci est un programme de steganographie"
print "---------------------------------------\n"
print "1- Coder une image"
print "2- Decoder une image\n"
choix = ""
while choix!='1' and choix!='2':
	choix = raw_input("Choisissez le programme adhequoit a votre besoin : ")
if choix == '1':
	imin = raw_input("Tapez le nom de l'image : ")
	textin = raw_input("Tapez le texte : ")
	crypt(imin, textin)
	print "Votre image codee : stegano.bmp"
elif choix == '2':
	imin = raw_input("Tapez le nom de l'image : ")
	textout = decrypt(imin)
	print textout
