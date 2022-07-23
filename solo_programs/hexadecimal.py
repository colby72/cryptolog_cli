# This code is the property of Ramy Chmak
# ---------------------------------------

couleur = {
	"abricot": "E67E30",
	"absinthe": "7FDD4C",
	"acajou": "88421D",
	"aigue-marine": "79F8F8",
	"alezan": "A76726",
	"amande": "82C46C",
	"amarante": "912B3B",
	"ambre jaune": "F0C300",
	"ambre rouge": "AD360E",
	"améthyste": "884DA7",
	"anthracite": "303030",
	"aquilain": "AD4F09",
	"ardoise": "5A5E6B",
	"argent": "CECECE",
	"asperge": "7BA05B",
	"aubergine": "370028",
	"auburn": "9D3E0C",
	"aurore": "FFCB60",
	"avocat": "568203",
	"azur héraldique": "1E7FCB",
	"azur": "74D0F1",
	"azurin": "A9EAFE",
	"baillet": "AE642D",
	"banane": "D1B606",
	"basané": "8B6C42",
	"beige": "C8AD7F",
	"beigeasse": "AFA77B",
	"beurre": "F0E36B",
	"beurre frais": "FFF48D",
	"bis": "766F64",
	"bisque": "FFE4C4",
	"bistre": "856D4D",
	"bitume": "4E3D28",
	"blanc": "FFFFFF",
	"blanc cassé": "FEFEE2",
	"blanc crème": "FDF1B8",
	"blé": "E8D630",
	"blet": "5B3C11",
	"bleu": "0000FF",
	"bleu canard": "048B9A",
	"bleu charron": "8EA2C6",
	"bleu d'anvers": "24445C",
	"blondeur": "E2BC74",
	"bordeaux": "6D071A",
	"brun": "5B3C11",
	"brique": "842E1B",
	"bronze": "614E1A",
	"brun clair": "CD853F",
	"cacao": "614B3A",
	"capucine": "FF5E4D",
	"carmin": "960018",
	"carotte": "F4661B",
	"cerise": "BB0B0B",
	"chair": "FEC3AC",
	"chocolat": "5A3A22",
	"citron": "F7FF3C",
	"citrouille": "DF6D14",
	"colombin": "6A455D",
	"coquelicot": "C60800",
	"cuivre": "B36700",
	"denim": "1560BD",
	"double claro": "BA9B61",
	"émeraude": "BA9B61",
	"étain oxydé": "BABABA",
	"fauve": "AD4F09",
	"fer": "AD4F09",
	"feu vif": "FF4901",
	"fraise": "BF3030",
	"framboise": "C72C48",
	"glycine": "C9A0DC",
	"gris": "606060",
	"gris acier": "AFAFAF",
	"gris anthracite": "303030",
	"gris tourterelle": "BBACAC",
	"gueules": "E21313",
	"havane": "947F60",
	"héliotrope": "DF73FF",
	"indigo": "791CF8",
	"isabelle": "785E2F",
	"ivoire": "FFFFD4",
	"jade": "87E990",
	"jaune": "FFFF00",
	"kaki": "94812B",
	"lapis-lazuli": "26619C",
	"lavallière": "8F5922",
	"lavande": "9683EC",
	"lie de vin": "AC1E44",
	"lilas": "B666D2",
	"magenta": "FF00FF",
	"magenta foncé": "800080",
	"mais": "FFDE75",
	"mandarine": "FEA347",
	"marine": "03224C",
	"marron": "582900",
	"mastic": "B3B191",
	"mauve": "D473D4",
	"melon": "DE9816",
	"menthe": "16B84E",
	"miel": "DAB30A",
	"moutarde": "C7CF00",
	"nacarat": "FC5D5D",
	"noir": "000000",
	"noisette": "955628",
	"olive": "708D23",
	"or": "FFD700",
	"orange": "ED7F10",
	"papaye": "FFEFD5",
	"pastel": "56739A",
	"pistache": "BEF574",
	"platine": "FAF0C5",
	"plomb": "798081",
	"poil de chameau": "B67823",
	"puce": "4E1609",
	"rose": "FD6C9E",
	"rose bonbon": "F9429E",
	"rouge": "FF0000",
	"rouge sang": "F9429E",
	"rouille": "985717",
	"roux": "AD4F09",
	"sable": "E0CDA9",
	"saphir": "0131B4",
	"saumon": "F88E55",
	"soufre": "FFFF6B",
	"souris": "9E9E9E",
	"tabac": "9F551E",
	"tomate": "DE2916",
	"turquoise": "25FDE9",
	"vanille": "E1CE9A",
	"vert": "00FF00",
	"vert bouteille": "096A09",
	"violet": "660099",
	"zinzolin": "6C0277"
}
# Code de test d'erreurs
''' n = 0
for nom, code in couleur.items():
	if len(code) != 6:
		print("Erreur long : {}".format(nom))
		n += 1
print("Erreurs : {}".format(n)) '''

def conv_colortocode(text):
	n = 0
	for nom, code in couleur.items():
		if nom == text:
			hex = code
			n += 1
	if n == 0:
		hex = "Couleur introuvable ..."
	return hex
def conv_codetocolor(hex):
	n = 0
	for nom, code in couleur.items():
		if code == hex:
			text = nom
			n += 1
	if n == 0:
		text = "Code introuvable ..."
	return text

print("Ceci est un décodeur de couleurs hexadécimaux")
print("---------------------------------------------\n")
print("1- Couleur ==> Code")
print("2- Code ==> Couleur")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("Choisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	textin = input("Tapez le nom de la couleur : ")
	codeout = conv_colortocode(textin.lower())
	print("Code hexadécimal : {}".format(codeout))
if choice == '2':
	codein = input("Tapez le code hexadécimal : ")
	textout = conv_codetocolor(codein.upper())
	print("Couleur : {}".format(textout))
#end
