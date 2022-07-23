# This code is the property of Ramy Chmak
# ---------------------------------------

couleur = {
	"abricot": "230.126.048",
	"absinthe": "127.221.076",
	"acajou": "136.066.026",
	"aigue-marine": "121.248.248",
	"alezan": "167.103.068",
	"amande": "130.196.108",
	"amarante": "144.040.059",
	"ambre jaune": "240.195.000",
	"ambre rouge": "173.057.014",
	"améthyste": "136.077.167",
	"anthracite": "048.048.048",
	"aquilain": "173.079.009",
	"ardoise": "090.094.107",
	"argent": "206.206.206",
	"asperge": "123.160.091",
	"aubergine": "055.000.040",
	"auburn": "157.062.012",
	"aurore": "255.203.096",
	"avocat": "086.130.003",
	"azur héraldique": "030.127.203",
	"azur": "116.208.241",
	"azurin": "169.234.254",
	"baillet": "174.100.045",
	"banane": "209.182.006",
	"basané": "139.108.066",
	"beige": "200.173.127",
	"beigeasse": "175.167.123",
	"beurre": "240.227.107",
	"beurre frais": "255.244.141",
	"bis": "118.111.100",
	"bisque": "255.228.196",
	"bistre": "133.109.077",
	"bitume": "078.061.040",
	"blanc": "255.255.255",
	"blanc cassé": "254.254.226",
	"blanc crème": "253.241.184",
	"blé": "232.214.048",
	"blet": "091.060.017",
	"bleu": "000.000.255",
	"bleu canard": "004.139.154",
	"bleu charron": "142.162.168",
	"bleu d'anvers": "036.068.092",
	"blondeur": "226.188.116",
	"bordeaux": "109.007.026",
	"brun": "091.060.017",
	"brique": "132.046.027",
	"bronze": "097.078.026",
	"brun clair": "205.133.063",
	"cacao": "097.075.058",
	"capucine": "255.094.077",
	"carmin": "150.000.024",
	"carotte": "244.102.027",
	"cerise": "187.011.011",
	"chair": "254.195.172",
	"chocolat": "090.058.034",
	"citron": "247.255.060",
	"citrouille": "223.109.020",
	"colombin": "106.069.093",
	"coquelicot": "198.008.000",
	"cuivre": "179.103.000",
	"denim": "021.096.189",
	"double claro": "186.155.097",
	"émeraude": "001.215.288",
	"étain oxydé": "186.186.186",
	"fauve": "173.097.009",
	"fer": "132.132.132",
	"feu vif": "255.073.001",
	"fraise": "191.048.048",
	"framboise": "199.044.072",
	"glycine": "201.160.220",
	"gris": "096.096.096",
	"gris acier": "175.175.175",
	"gris anthracite": "048.048.048",
	"gris tourterelle": "187.172.172",
	"gueules": "207.010.029",
	"havane": "148.127.096",
	"héliotrope": "223.115.255",
	"indigo": "121.028.248",
	"isabelle": "120.094.047",
	"ivoire": "255.255.212",
	"jade": "135.233.144",
	"jaune": "255.255.000",
	"kaki": "148.129.043",
	"lapis-lazuli": "038.097.156",
	"lavallière": "143.089.034",
	"lavande": "150.131.236",
	"lie de vin": "172.030.068",
	"lilas": "182.102.230",
	"magenta": "255.000.255",
	"magenta foncé": "128.000.128",
	"mais": "255.222.117",
	"mandarine": "254.163.071",
	"marine": "003.034.076",
	"marron": "088.041.000",
	"mastic": "179.177.145",
	"mauve": "212.115.121",
	"melon": "222.152.022",
	"menthe": "022.184.078",
	"miel": "218.179.010",
	"moutarde": "199.207.000",
	"nacarat": "252.093.093",
	"noir": "000.000.000",
	"noisette": "149.086.040",
	"olive": "112.141.035",
	"or": "255.215.000",
	"orange": "237.127.016",
	"papaye": "255.239.213",
	"pastel": "086.115.154",
	"pistache": "190.245.116",
	"platine": "250.240.197",
	"plomb": "121.128.129",
	"poil de chameau": "182.120.035",
	"puce": "078.022.009",
	"rose": "253.108.158",
	"rose bonbon": "249.066.158",
	"rouge": "255.000.000",
	"rouge sang": "133.006.006",
	"rouille": "152.087.023",
	"roux": "173.079.009",
	"sable": "224.205.169",
	"saphir": "001.049.180",
	"saumon": "248.142.085",
	"soufre": "255.255.105",
	"souris": "158.158.158",
	"tabac": "159.085.030",
	"tomate": "222.041.022",
	"turquoise": "037.253.233",
	"vanille": "255.206.154",
	"vert": "000.255.000",
	"vert bouteille": "009.106.009",
	"violet": "136.006.206",
	"zinzolin": "108.002.119"
}

# Code de test d'erreurs
''' n = 0
for nom, code in couleur.items():
	if len(code) != 11:
		print("Erreur long : {}".format(nom))
		n += 1
	if code[3] != '.' or code[7] != '.':
		print("Erreur point : {}".format(nom))
		n += 1
print("Erreurs : {}".format(n)) '''

def conv_colortocode(text):
	n = 0
	for nom, code in couleur.items():
		if nom == text:
			rvb = code
			n += 1
	if n == 0:
		rvb = "Couleur introuvable ..."
	return rvb
def conv_codetocolor(rvb):
	n = 0
	for nom, code in couleur.items():
		if code == rvb:
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
	print("Code RVB : {}".format(codeout))
if choice == '2':
	codein = input("Tapez le code couleur RVB : ")
	textout = conv_codetocolor(codein)
	print("Couleur : {}".format(textout))
#end
