# This code is the property of Ramy Chmak
# ---------------------------------------

from fonctions import *

# Tableur des caractères spéciaux
def askSpecial():
	print("This is a table for special caracters")
	print("-------------------------------------\n")
	print("1- Caracter ==> Code")
	print("2- Code ==> Caracter")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter your special caracter : ")
		codeout = cryptSpecial(textin)
		print("Correspondant code : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the special caracter code : ")
		textout = decryptSpecial(codein)
		print("Correspondant caracter : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askSpecial()

# Tableur de codes couleurs RVB
def askRVB():
	print("This is a table for RGB color codes")
	print("-----------------------------------\n")
	print("1- Color ==> Code")
	print("2- Code ==> Color")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the name of your color : ")
		codeout = cryptRVB(textin)
		print("Correspondant code : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter your color code : ")
		textout = decryptRVB(codein)
		print("Correspondant code : {]\n".format(textout))
	else:
		print("Program selected unknown !")
		return askRVB()

# Tableur de codes couleurs hexadécimaux
def askHexadecimal():
	print("This is a table for hexadecimal color codes")
	print("-------------------------------------------\n")
	print("1- Color ==> Code")
	print("2- Code ==> Color")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("Choose the service you want : ")
	if choix == '1':
		textin = input("Enter the name of your color : ")
		codeout = cryptHexadecimal(textin)
		print("Correspondant code : #{}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the color code : #")
		textout = decryptHexadecimal(codein)
		print("Correspondant color : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askHexadecimal()

# Convertisseur language binaire
def askBinary():
	print("This a binary code translator")
	print("---------------------------------------------\n")
	print("1- Coding: Text ==> Binary code")
	print("2- Décodage: Binary code ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the text to code : ")
		codeout = cryptBinary(textin)
		print("Coded text : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the coded text : ")
		while len(codein) % 8 != 0:
			print("Invalid code ..")
			codein = input("Enter the coded text : ")
		textout = decryptBinary(codein)
		print("Decoded text : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askBinary()

# Convertisseur de code Morse
def askMorse():
	print("This is a Morse code translator")
	print("Concerning the Morse code, we admit that '0' represent an inactive signal, while '1' represent an active one.")
	print("-------------------------------------------------------------------------------------------------------------\n")
	print("1- Coding: Text ==> Morse code")
	print("2- Decoding: Morse code ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want :")
	if choix == '1':
		textin = input("Enter the text to code : ")
		codeout = cryptMorse(textin)
		print("Coded text : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the coded text : ")
		textout = decryptMorse(codein)
		print("Decoded text : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askMorse()

# Programme de cryptage César
def askCesar():
	print("This is a Cesar cipher decoder")
	print("------------------------------\n")
	print("1- Coding: Text ==> Cesar cipher")
	print("2- Decoding: Cesar cipher ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the message to cipher : ")
		cle = input("Enter your encryption key : ")
		codeout = cryptCesar(textin, cle)
		print("Crytogram deciphered : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the cryptogram to decipher : ")
		cle = input("Enter your decryption key : ")
		textout = cryptCesar(codein, cle)
		print("Message deciphered : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return cryptCesar()

# Programme de cryptage Affine
def askAffine():
	print("This is a linear cipher decoder")
	print("PS: The encryption function take the form 'ax + b'")
	print("-------------------------------------------------\n")
	print("1- Coding: Text ==> Cesar cipher")
	print("2- Decoding: Cesar cipher ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the message to cipher : ")
		print("Enter your your encryption key : ")
		a = input("a = ")
		b = input("b = ")
		codeout = cryptAffine(textin, a, b)
		print("Cryptogram ciphered : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the cryptogram to decipher : ")
		print("Enter your decryption key : ")
		a = input("a = ")
		b = input("b = ")
		textout = cryptAffine(codein, a, b)
		print("Message déchiffré : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askAffine()

# Programme de cryptage Vigenère
def askVigenere():
	print("This is a Vigenère cipher decoder")
	print("---------------------------------\n")
	print("1- Coding: Text ==> Vigenère cipher")
	print("2- Decoding: Vigenère cipher ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the message to cipher : ")
		cle = input("Enter your encryption key : ")
		codeout = cryptVigenere(textin, cle)
		print("Ciphered cryptogram : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter the cryptogram to decipher : ")
		cle = input("Enter your decryption key : ")
		textout = decryptVigenere(codein, cle)
		print("Deciphered message : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askVigenere()

# Programme de cryptage Hill
def askHill():
	print("This is a Hill cipher decoder")	
	print("The matrix take the form : |a  b|")
	print("                           |c  d|")
	print("If the message lenght cannot be divided by 2, we add 'X' at the end.")
	print("--------------------------------------------------------------------\n")
	print("1- Coding: Text ==> Cryptogram")
	print("2- Decoding: Cryptogram ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the message to cipher : ")
		print("Enter your encryption key : ")
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		d = input("d = ")
		codeout = cryptHill(textin, a, b, c, d)
		print("Ciphered cryptogram : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Enter th cryptogram to decipher : ")
		print("Enter your decryption key : ")
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		d = input("d = ")
		textout = cryptHill(codein, a, b, c, d)
		print("Deciphered message : {}\n".format(textout))
	else:
		print("Program selected unknown !")
		return askHill()

# Programme de cryptage RSA
def askRSA():
	print("This is a RSA cipher decoder")
	print("----------------------------\n")
	print("1- Coding: Text ==> Cryptogram")
	print("2- Decoding: Cryptogram ==> Text")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoose the service you want : ")
	if choix == '1':
		textin = input("Enter the message to cipher : ")
		pin = input("Enter p : ")
		qin = input("Enter q : ")
		pin = int(pin)
		qin = int(qin)
		codeout = cryptrsa(textin, pin, qin)
		print("n = {}\nPhi of n = {}\ne = {}\n".format(codeout[0], codeout[1], codeout[2]))
		for i, l in enumerate(codeout[3:]):
			print("Block: {}".format(l))
	elif choix == '2':
		nb = input("How many blocks in the cryptogram ? ")
		nb = int(nb)
		i = 0
		codein = []
		while i < nb:
			cod = input("Enter the code : ")
			cod = int(cod)
			codein.append(cod)
			i += 1
		nin = input("Tapez n : ")
		din = input("Tapez d : ")
		nin = int(nin)
		din = int(din)
		textout = decryptrsa(codein, nin, din)
		print("Deciphered message : {}".format(textout))
	else:
		print("Program selected unknown !")
		return askRSA()

# Programme de stéganographie
def askStegano():
	print("This is a steganography program")
	print("Please make sure that the image have the extension .bmp")
	print("You should execute the program \"stagano\" independantly from the software because of incompatibility error")
	#print("Si le programme ne marche pas, vous pouvez éxecuter le programme 'stegano' indépendament du logiciel (Python 2)")
	#print("---------------------------------------------------------------------------------------------------------------\n")
	#print("1- Chiffrer un texte dans une image")
	#print("2- Déchiffrer une image")
	#choix = ""
	#while choix != '1' and choix != '2':
	#	choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	#if choix == '1':
	#	textin = input("Tapez le message à chiffrer : ")
	#	imgin = input("Entrez le nom de l'image à coder : ")
	#	imgout = cryptStegano(textin, imgin)
	#	print("Image chiffrée : {}\n".format(imgout))
	#elif choix == '2':
	#	imgin = input("Entrez le nom de l'image à déchiffrer : ")
	#	textout = decryptStegano(imgin)
	#	print("Message caché : {}\n".format(textout))
	#else:
	#	print("Programme choisi inconnu !")
	#	return askStegano()

# Programme de Hash
def askHash():
	print("This is a Hash program")
	print("----------------------\n")
	print("These are all the available Hash systems :")
	print("1- All \t2- sha-1\t3- sha-224\t4- sha-256\t5- sha-384\t6- sha-512\t7- md5")
	choix = ""
	while choix != '1' and choix != '2' and choix != '3' and choix != '4' and choix != '5' and choix != '6' and choix != '7':
		choix = input("\nChoose the service you want : ")
	textin = input("Enter the text to hash : ")
	if choix == '1':
		sha1 = hash_sha1(textin)
		sha224 = hash_sha224(textin)
		sha256 = hash_sha256(textin)
		sha384 = hash_sha384(textin)
		sha512 = hash_sha512(textin)
		md5 = hash_md5(textin)
		lst_hash = [sha1, sha224, sha256, sha384, sha512, md5]
		lst_sys = ["sha-1", "sha-224", "sha-256", "sha-384", "sha-512", "md5"]
		print("Your Hashs : ")
		for i, l in enumerate(lst_sys):
			#print("{} : {}".format(lst_sys[i], lst_hash[i][0]))
			print("{} Hexadecimal : {}".format(lst_sys[i], lst_hash[i][1]))
	elif choix == '2':
		codeout = hash_sha1(textin)
		print("Hash system : sha-1")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hexadecimal Hash : {}\n".format(codeout[1]))
	elif choix == '3':
		codeout = hash_sha224(textin)
		print("Hash system : sha-224")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hexadecimal Hash : {}\n".format(codeout[1]))
	elif choix == '4':
		codeout = hash_sha256(textin)
		print("Hash system : sha-256")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hexadecimal Hash : {}\n".format(codeout[1]))
	elif choix == '5':
		codeout = hash_sha384(textin)
		print("Hash system : sha-384")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hexadecimal Hash : {}\n".format(codeout[1]))
	elif choix == '6':
		codeout = hash_sha512(textin)
		print("Hash system : sha-512")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hexadecimal Hash : {}\n".format(codeout[1]))
	elif choix == '7':
		codeout = hash_md5(textin)
		print("Hash system : md5")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hexadecimal Hash : {}\n".format(codeout[1]))
	else:
		print("Program selected unknown :")
		return askHash()
