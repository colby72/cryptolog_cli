# This code is the property of Ramy Chmak
# ---------------------------------------

from math import *
def pgcd(a, b):
	if b == 0:
		return a
	else:
		return pgcd(b, a%b)
def cryptrsa(txt, p, q):
	n = 1.0
	phi = 1.0
	n = p * q
	phi = (p-1) * (q-1)
	e = 1.0
	c = 1.0
	pg = 1.0
	while pg != 1:
		while c == 0:
			if ((p<e) and (q<e)) and (e<phi):
				c = 1
			e += 1
		pg = pgcd(e, phi)
	cry = [n, phi, e]
	cipher = 1.0
	for i, l in enumerate(txt):
		x = ord(l)
		cipher = pow(x, e) % n
		cry.append(cipher)
	return cry
def decryptrsa(code, n, d):
	n = float(n)
	#d = float(d)
	x = 1.0
	let = []
	for i, l in enumerate(code):
		x = float(x)
		x = pow(l, d) % n
		x = int(x)
		let.append(chr(x))
	txt = "".join(let)
	return txt
print("Ceci est un décodeur de cryptage RSA")
print("------------------------------------\n")
print("1- Décodeur Texte clair ==> Texte chiffré")
print("2- Décodeur Texte chiffré ==> Texte clair")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("\nChoisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	textin = input("Tapez le texte à crypter : ")
	pin = input("Tapez p : ")
	pin = int(pin)
	qin = input("Tapez q : ")
	qin = int(qin)
	codeout = cryptrsa(textin, pin, qin)
	print("n = {}\tphi de n = {}\te = {}".format(codeout[0], codeout[1], codeout[2]))
	print("Voici le code crypté : \n")
	for i, l in enumerate(codeout[3:]):
		print("Block : ", l)
elif choice == '2':
	codein = []
	tin = 'a'
	while tin != 'q':
		tin = input("Tapez le code : ")
		if tin != 'q':
			tin = float(tin)
		codein.append(tin)
	nin = input("Tapez n : ")
	nin = int(nin)
	din = input("Tapez d : ")
	din = int(din)
	textout = decryptrsa(codein, nin, din)
	print("Voici le texte décrypté : {}".format(textout))
#end
