# This code is the property of Ramy Chmak
# ---------------------------------------

from fonctions import *

# Tableur des caractères spéciaux
def askSpecial():
	print("Ceci est un tableur de caractères spéciaux")
	print("------------------------------------------\n")
	print("1- Caractère ==> Code")
	print("2- Code ==> Caractère")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez votre caractère spécial : ")
		codeout = cryptSpecial(textin)
		print("Code correspondant : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le code du caractère spécial : ")
		textout = decryptSpecial(codein)
		print("Caractère correspondant : {}\n".format(textout))
	else:
		print("Programme choisi inconnu")
		return askSpecial()

# Tableur de codes couleurs RVB
def askRVB():
	print("Ceci est un tableur de codes couleurs RVB")
	print("Le code couleur s'écrit sous la forme RRR.VVV.BBB")
	print("-------------------------------------------------\n")
	print("1- Couleur ==> Code")
	print("2- Code ==> Couleur")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le nom de votre couleur : ")
		codeout = cryptRVB(textin)
		print("Code correspondant : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le code couleur : ")
		textout = decryptRVB(codein)
		print("Couleur correspondante : {]\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askRVB()
# Tableur de codes couleurs hexadécimaux
def askHexadecimal():
	print("Ceci est un tableur de codes couleurs hexadécimaux")
	print("--------------------------------------------------\n")
	print("1- Couleur ==> Code")
	print("2- Code ==> Couleur")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("Choisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le nom de votre couleur : ")
		codeout = cryptHexadecimal(textin)
		print("Code correspondant : #{}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le code couleur : #")
		textout = decryptHexadecimal(codein)
		print("Couleur correspondante : {}\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askHexadecimal()

# Convertisseur language binaire
def askBinary():
	print("Ceci est un convertisseur de language binaire")
	print("---------------------------------------------\n")
	print("1- Codage: Texte clair ==> Code binaire")
	print("2- Décodage: Code binaire ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à vore besoin : ")
	if choix == '1':
		textin = input("Tapez le texte à chiffrer : ")
		codeout = cryptBinary(textin)
		print("Texte chiffrée : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le code à déchiffrer : ")
		while len(codein) % 8 != 0:
			print("Code invalide ..")
			codein = input("Tapez le code à déchiffrer : ")
		textout = decryptBinary(codein)
		print("Texte déchiffré : {}\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askBinary()

# Convertisseur de code Morse
def askMorse():
	print("Ceci est un convertisseur de code morse")
	print("Concernant le code Morse, on admet que '0' réprésente un signal nul, alors que '1' représente un signal actif.")
	print("--------------------------------------------------------------------------------------------------------------\n")
	print("1- Chiffrement: Texte clair ==> Code Morse")
	print("2- Déchiffrement: Code Morse ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin :")
	if choix == '1':
		textin = input("Tapez le texte à chiffrer : ")
		codeout = cryptMorse(textin)
		print("Texte chiffrée : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le code à déchiffrer : ")
		textout = decryptMorse(codein)
		print("Texte déchiffrée : {}\n".format(textout))
	else:
		print("Programme choisi inconnu")
		return askMorse()

# Programme de cryptage César
def askCesar():
	print("Ceci est un décodeur de cryptage César")
	print("--------------------------------------\n")
	print("1- Chiffrement: Texte clair ==> Code César")
	print("2- Déchiffrement: Code César ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le message à chiffrer : ")
		cle = input("Tapez votre clé de chiffrement : ")
		codeout = cryptCesar(textin, cle)
		print("Crytogramme chiffré : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le cryptogramme à déchiffrer : ")
		cle = input("Tapez votre clé de déchiffrement : ")
		textout = cryptCesar(codein, cle)
		print("Message déchiffré : {}\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return cryptCesar()

# Programme de cryptage Affine
def askAffine():
	print("Ceci est un décodeur de cryptage Affine")
	print("NB: La fonction de cryptage prend la forme 'ax + b'")
	print("---------------------------------------------------\n")
	print("1- Chiffrement: Texte clair ==> Code César")
	print("2- Déchiffrement: Code César ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le message à crypter : ")
		print("Tapez votre clé de chiffrement : ")
		a = input("a = ")
		b = input("b = ")
		codeout = cryptAffine(textin, a, b)
		print("Cryptogramme chiffré : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le cryptogramme à déchiffrer : ")
		print("Tapez votre clé de déchiffrement : ")
		a = input("a = ")
		b = input("b = ")
		textout = cryptAffine(codein, a, b)
		print("Message déchiffré : {}\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askAffine()

# Programme de cryptage Vigenère
def askVigenere():
	print("Ceci est un décodeur du chiffre Vigenère")
	print("----------------------------------------\n")
	print("1- Chiffrement: Texte clair ==> Code Vigenère")
	print("2- Déchiffrement: Code Vigenère ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le message à chiffrer : ")
		cle = input("Tapez la clé de chiffrement : ")
		codeout = cryptVigenere(textin, cle)
		print("Cryptogramme chiffré : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le cryptogramme à déchiffrer : ")
		cle = input("Tapez la clé de déchiffrement : ")
		textout = decryptVigenere(codein, cle)
		print("Message déchiffré : {}\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askVigenere()

# Programme de cryptage Hill
def askHill():
	print("Ceci est un décodeur de chiffre de Hill")	
	print("La matrice est sous la forme : |a  b|")
	print("                               |c  d|")
	print("Si le message ne peut pas être découpé en 2, on rajoute un 'X' à la fin.")
	print("------------------------------------------------------------------------\n")
	print("1- Chiffrement: Texte clair ==> Code crypté")
	print("2- Déchiffrement: Code crypté ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le message à chiffrer : ")
		print("Entrez la clé clé de chiffrement : ")
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		d = input("d = ")
		codeout = cryptHill(textin, a, b, c, d)
		print("Cryptogramme chiffré : {}\n".format(codeout))
	elif choix == '2':
		codein = input("Tapez le cryptogramme à déchiffrer : ")
		print("Entrez la clé de déchiffrement : ")
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		d = input("d = ")
		textout = cryptHill(codein, a, b, c, d)
		print("Message déchiffré : {}\n".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askHill()

# Programme de cryptage RSA
def askRSA():
	print("Ceci est un système de chiffrement RSA")
	print("--------------------------------------\n")
	print("1- Chiffrement: Texte clair ==> Texte chiffré")
	print("2- Déchiffrement: Texte chiffré ==> Texte clair")
	choix = ""
	while choix != '1' and choix != '2':
		choix = input("\nChoisissez le programme adhéquoit à votre besoin : ")
	if choix == '1':
		textin = input("Tapez le message à chiffrer : ")
		pin = input("Tapez p : ")
		qin = input("Tapez q : ")
		pin = int(pin)
		qin = int(qin)
		codeout = cryptrsa(textin, pin, qin)
		print("n = {}\nPhi de n = {}\ne = {}\n".format(codeout[0], codeout[1], codeout[2]))
		for i, l in enumerate(codeout[3:]):
			print("Block: {}".format(l))
	elif choix == '2':
		nb = input("Combien de block dans le cryptogramme ? ")
		nb = int(nb)
		i = 0
		codein = []
		while i < nb:
			cod = input("Tapez le code : ")
			cod = int(cod)
			codein.append(cod)
			i += 1
		nin = input("Tapez n : ")
		din = input("Tapez d : ")
		nin = int(nin)
		din = int(din)
		textout = decryptrsa(codein, nin, din)
		print("Message déchiffré : {}".format(textout))
	else:
		print("Programme choisi inconnu !")
		return askRSA()

# Programme de stéganographie
def askStegano():
	print("Ceci est un programme de stéganographie")
	print("Veillez à ce que l'image à coder ait l'extension .bmp")
	print("Il faudrait mieux exécuter le programme \"stagano\" indépandamment du logiciel à cause d'une erreur d'icompatibilté")
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
	print("Ceci est un programme de Hash")
	print("-----------------------------\n")
	print("Voici les systèmes de Hash disponibles :")
	print("1- Tout \t2- sha-1\t3- sha-224\t4- sha-256\t5- sha-384\t6- sha-512\t7- md5")
	choix = ""
	while choix != '1' and choix != '2' and choix != '3' and choix != '4' and choix != '5' and choix != '6' and choix != '7':
		choix = input("\nChoisissez le système qui vous convient : ")
	textin = input("Tapez le texte à hasher : ")
	if choix == '1':
		sha1 = hash_sha1(textin)
		sha224 = hash_sha224(textin)
		sha256 = hash_sha256(textin)
		sha384 = hash_sha384(textin)
		sha512 = hash_sha512(textin)
		md5 = hash_md5(textin)
		lst_hash = [sha1, sha224, sha256, sha384, sha512, md5]
		lst_sys = ["sha-1", "sha-224", "sha-256", "sha-384", "sha-512", "md5"]
		print("Voici les hash : ")
		for i, l in enumerate(lst_sys):
			#print("{} : {}".format(lst_sys[i], lst_hash[i][0]))
			print("{} hexadécimal : {}".format(lst_sys[i], lst_hash[i][1]))
	elif choix == '2':
		codeout = hash_sha1(textin)
		print("Système de hashage : sha-1")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hash hexadécimal : {}\n".format(codeout[1]))
	elif choix == '3':
		codeout = hash_sha224(textin)
		print("Système de hashage : sha-224")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hash hexadécimal : {}\n".format(codeout[1]))
	elif choix == '4':
		codeout = hash_sha256(textin)
		#print("Système de hashage : sha-256")
		print("Hash : {}\n".format(codeout[0]))
		print("Hash hexadécimal : {}\n".format(codeout[1]))
	elif choix == '5':
		codeout = hash_sha384(textin)
		print("Système de hashage : sha-384")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hash hexadécimal : {}\n".format(codeout[1]))
	elif choix == '6':
		codeout = hash_sha512(textin)
		print("Système de hashage : sha-512")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hash hexadécimal : {}\n".format(codeout[1]))
	elif choix == '7':
		codeout = hash_md5(textin)
		print("Système de hashage : md5")
		#print("Hash : {}\n".format(codeout[0]))
		print("Hash hexadécimal : {}\n".format(codeout[1]))
	else:
		print("Programme choisi inconnu :")
		return askHash()
#end
