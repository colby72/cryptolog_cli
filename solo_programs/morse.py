# This code is the property of Ramy Chmak
# ---------------------------------------

alphabet = {
	'A' : "10111",
	'B' : "111010101",
	'C' : "11101011101",
	'D' : "1110101",
	'E' : "1",
	'F' : "101011101",
	'G' : "111011101",
	'H' : "1010101",
	'I' : "101",
	'J' : "1011101110111",
	'K' : "111010111",
	'L' : "101110101",
	'M' : "1110111",
	'N' : "11101",
	'O' : "11101110111",
	'P' : "10111011101",
	'Q' : "1110111010111",
	'R' : "1011101",
	'S' : "10101",
	'T' : "111",
	'U' : "1010111",
	'V' : "101010111",
	'W' : "101110111",
	'X' : "11101010111",
	'Y' : "1110101110111",
	'Z' : "11101110101",
	'0' : "1110111011101110111",
	'1' : "10111011101110111",
	'2' : "101011101110111",
	'3' : "1010101110111",
	'4' : "10101010111",
	'5' : "101010101",
	'6' : "11101010101",
	'7' : "1110111010101",
	'8' : "111011101110101",
	'9' : "11101110111011101",
	' ' : "0000"
}
lettres = {
	"10111": 'A',
	"111010101": 'B',
	"11101011101": 'C',
	"1110101": 'D',
	"1": 'E',
	"101011101": 'F',
	"111011101": 'G',
	"1010101": 'H',
	"101": 'I',
	"1011101110111": 'J',
	"1110101111": 'K',
	"101110101": 'L',
	"1110111": 'M',
	"11101": 'N',
	"11101110111": 'O',
	"10111011101": 'P',
	"1110111010111": 'Q',
	"1011101": 'R',
	"10101": 'S',
	"111": 'T',
	"1010111": 'U',
	"101010111": 'V',
	"101110111": 'W',
	"11101010111": 'X',
	"1110101110111": 'Y',
	"11101110101": 'Z',
	"10111011101110111": '1',
	"101011101110111": '2',
	"1010101110111": '3',
	"10101010111": '4',
	"101010101": '5',
	"11101010101": '6',
	"1110111010101": '7',
	"111011101110101": '8',
	"11101110111011101": '9',
	"1110111011101110111": '0',
	"0000": ' '
}
def conv_morsetotext(code):
	n = 0
	let = []
	temp = []
	cry = []
	tmp = []
	text = ""
	k = 0
	cry = code.split('000')
	for i, m in enumerate(cry):
		if m == '':
			cry = []
			n += 1
	if n > 0:
		tmp = code.split('0000000')
		for i, l in enumerate(tmp):
			temp = l.split('000')
			cry.extend(temp)
			if k < n:
				cry.append('0000')
			k += 1
	for j, m in enumerate(cry):
		let.append(lettres[m])
	text = "".join(let)
	return text
def conv_texttomorse(text):
	text = text.upper()
	code = ""
	let = []
	for i, l in enumerate(text):
		if i<len(text)-1:
			let.append(alphabet[l])
			if alphabet[l] != '0000':
				let.append('000')
		else:
			let.append(alphabet[l])
	code = "".join(let)
	return code
print("Ceci est un convertisseur de code Morse")
print("Concernant le code Morse, on admet que '0' représente un signal nul, alors que '1' représente un signal actif.")
print("--------------------------------------------------------------------------------------------------------------")
print("\n1- Convertisseur Code Morse ==> Texte clair")
print("2- Convertisseur Texte clair ==> Code Morse")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("\nChoisissez le programme adhéquoit à votre besoin : ")
if choice=='1':
	codein = input("Saisissez votre code morse : ")
	textout = conv_morsetotext(codein)
	print("Voici le code déchiffré : \n{}".format(textout))
elif choice=='2':
	textin = input("Saisissez votre texte : ")
	codeout = conv_texttomorse(textin)
	print("Voici le texte chiffré : \n{}".format(codeout))
