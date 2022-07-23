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
def convcesar(text, key):
	text = text.upper()
	key = int(key)
	let = []
	for i, l in enumerate(text):
		x = alphabet[l]
		let.append(lettres[(x+key)%26])
	cesar = "".join(let)
	return cesar
print("Ceci est un décodeur de cryptage César")
print("--------------------------------------")
print("\n1- Décodeur Code César ==> Texte clair")
print("2- Décodeur Texte clair ==> Code César")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("\nChoisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	codein = input("Saisissez votre code chiffré : ")
	cle = input("Saisissez votre clé de déchiffrement : ")
	textout = convcesar(codein, cle)
	print("Voici le code déchiffré : \n{}".format(textout))
elif choice == '2':
	textin = input("Saisissez le code à chiffrer : ")
	cle = input("Saisissez votre clé de chiffrement : ")
	codeout = convcesar(textin, cle)
	print("Voici le texte chiffré : \n{}".format(codeout))
