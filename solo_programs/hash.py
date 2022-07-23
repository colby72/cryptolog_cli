# This code is the property of Ramy Chmak
# ---------------------------------------

import hashlib

def hash_text(text, hash):
	text = text.encode()
	if hash=="sha1":
		crypt = hashlib.sha1(text).hexdigest()
		return crypt
	elif hash=="sha224":
		crypt = hashlib.sha224(text).hexdigest()
		return crypt
	elif hash=="sha256":
		crypt = hashlib.sha256(text).hexdigest()
		return crypt
	elif hash=="sha384":
		crypt = hashlib.sha384(text).hexdigest()
		return crypt
	elif hash=="sha512":
		crypt = hashlib.sha512(text).hexdigest()
		return crypt
	elif hash=="md5":
		crypt = hashlib.md5(text).hexdigest()
		return crypt
	elif hash=="all":
		sha1 = hashlib.sha1(text).hexdigest()
		sha224 = hashlib.sha224(text).hexdigest()
		sha256 = hashlib.sha256(text).hexdigest()
		sha384 = hashlib.sha384(text).hexdigest()
		sha512 = hashlib.sha512(text).hexdigest()
		md5 = hashlib.md5(text).hexdigest()
		return [sha1, sha224, sha256, sha384, sha512, md5]
	else:
		print("Système de hashage inconnu !")

print("Ceci est un système de hashage")
print("------------------------------\n")
print("Choisissez un des systèmes de hashage suivants : ")
print("sha1\tsha224\tsha256\tsha384\tsha512\tmd5\tall")
print("all: encode votre texte avec tous les systèmes de hashage disponibles !\n")
textin = input("Saisissez le texte à hasher : \n")
hashsys = 'a'
while hashsys!='sha1' and hashsys!='sha224' and hashsys!='sha256' and hashsys!='sha384' and hashsys!='sha256' and hashsys!='md5' and hashsys!='all':
	hashsys = input("Choisissez votre système de hashage préféré : ")
print("\nHaché : {}".format(textin))
if hashsys=='sha1' or hashsys=='sha224' or hashsys=='sha256' or hashsys=='sha384' or hashsys=='sha512' or hashsys=='md5':
	hashout = hash_text(textin, hashsys)
	print("Système de hashage : {}".format(hashsys))
	print("Hash : {}".format(hashout))
elif hashsys=='all':
	lst = hash_text(textin, hashsys)
	ls = ["sha1", "sha224", "sha256", "sha384", "sha512", "md5"]
	print("Voici les hash : ")
	for i, l in enumerate(lst):
		print("{} : {} {}".format(ls[i], lst[i]))
