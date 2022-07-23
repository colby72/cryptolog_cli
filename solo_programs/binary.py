# This code is the property of Ramy Chmak
# ---------------------------------------

def texttobin(ch):
	text = ''
	zero = 0
	while ch != '':
		c = ch[:1:]
		ch = ch[1::]
		c = ord(c)
		ch1 = bin(c)
		ch1 = ch1[2::]
		zero = 8 - len(ch1)
		ch1 =  ("0" * zero ) + ch1
		text = text + ch1
	return text
def bintotext(bin):
	text = ""
	bin = str(bin)
	while bin != '':
		ch = bin[:8:]
		bin = bin[8::]
		ch = '0b' + ch
		ch = int(ch, 2)
		text += chr(ch)
	return text
print("Ceci est un conc=vertisseur de code binaire")
print("1- Convertisseur Code binaire ==> Texte clair")
print("2- Convertisseur Texte clair ==> Code binaire")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("\nChoisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	codein = input("Tapez votre code binaire : ")
	textout = bintotext(codein)
	print("Votre texte : {}".format(textout))
elif choice == '2':
	textin = input("Tapez votre texte : ")
	codeout = texttobin(textin)
	print("Votre code : {}".format(codeout))
#end
