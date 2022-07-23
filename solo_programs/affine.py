# This code is the proprrty of Ramy Chmak
# ---------------------------------------

alphabet = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'E': 4,
	'F': 5,
	'G': 6,
	'H': 7,
	'I': 8,
	'J': 9,
	'K': 10,
	'L': 11,
	'M': 12,
	'N': 13,
	'O': 14,
	'P': 15,
	'Q': 16,
	'R': 17,
	'S': 18,
	'T': 19,
	'U': 20,
	'V': 21,
	'W': 22,
	'X': 23,
	'Y': 24,
	'Z': 25
}
lettres = {
	0: 'A',
	1: 'B',
	2: 'C',
	3: 'D',
	4: 'E',
	5: 'F',
	6: 'G',
	7: 'H',
	8: 'I',
	9: 'J',
	10: 'K',
	11: 'L',
	12: 'M',
	13: 'N',
	14: 'O',
	15: 'P',
	16: 'Q',
	17: 'R',
	18: 'S',
	19: 'T',
	20: 'U',
	21: 'V',
	22: 'W',
	23: 'X',
	24: 'Y',
	25: 'Z'
}
def convaffine(text, keya, keyb):
	let = []
	text = text.upper()
	keya = int(keya)
	keyb = int(keyb)
	for i, l in enumerate(text):
		x = alphabet[l]
		let.append(lettres[((keya*x)+keyb)%26])
	affine = "".join(let)
	return affine
print("Ceci est un décodeur du cryptage affine")
print("---------------------------------------\n")
print("1- Décodeur Code Affine ==> Texte clair")
print("2- Décodeur Texte clair ==> Code Affine")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("Choisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	codein = input("Tapez le texte à décrypter : ")
	clea = input("Tapez a : ")
	cleb = input("Tapez b : ")
	textout = convaffine(codein, clea, cleb)
	print("Voici le texte décrypté : \n{}".format(textout))
elif choice == '2':
	textin = input("Tapez le texte à crypter : ")
	clea = input("Tapez a : ")
	cleb = input("Tapez b : ")
	codeout = convaffine(textin, clea, cleb)
	print("Voici le texte crypté : \n{}".format(codeout))
