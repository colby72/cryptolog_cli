# This code is the property of Ramy Chmak
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
def convhill(text, a, b, c, d):
	text = text.upper()
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	code = ""
	let = []
	cry= []
	for i, l in enumerate(text):
		if ord(l) > 64 and ord(l) < 91:
			let.append(l)
	if len(let) % 2 != 0:
		let.append('X')
	i = 0
	while i < len(let)-1:
		x = lettres[((alphabet[let[i]]*a)+(alphabet[let[i+1]]*b)) % 26]
		y = lettres[((alphabet[let[i]]*c)+(alphabet[let[i+1]]*d)) % 26]
		cry.extend([x, y])
		i += 2
	code = "".join(cry)
	return code
print("Ceci est un décodeur de chiffre de Hill")
print("La matrice est sous la forme : |a  b|")
print("                               |c  d|")
print("Si le message ne peut pas être découpé par 2, on rajoute un 'X' à la fin")
print("------------------------------------------------------------------------\n")
print("Décodeur Texte clair ==> Code Hill")
print("Décodeur Code Hill ==> Texte clair")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("Choisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	textin = input("Tapez le message à chiffrer : ")
	print("Tapez la clé de chiffrement : ")
	a = input("a = ")
	b = input("b = ")
	c = input("c = ")
	d = input("d = ")
	codeout = convhill(textin, a, b, c, d)
	print("Voici votre texte chiffré : {}".format(codeout))
if choice == '2':
	codein = iput("Tapez le cryptogramme à déchiffrer : ")
	print("Tapez la clé de déchiffrement : ")
	a = input("a = ")
	b = input("b = ")
	c = input("c = ")
	d = input("d = ")
	textout = convhill(codein, a, b, c, d)
	print("Voici le message clair : {}".format(textout))
#end
