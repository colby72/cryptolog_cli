from math import *
# Fonction PGCD
def pgcd(a, b):
	while a!= b:
		if a > b:
			a -= b
		else:
			b -= a
	return a;
p = input("Tapez un grand nombre premier p : ")
p = int(p)
q = input("Tapez un grand nombre premier q : ")
q = int(q)
n = p * q
print("n = {}".format(n))
phiden = (p-1)*(q-1)
print("phi de n = {}".format(phiden))
# Variables de la boucle
c = 0
pgc = 0
# Tant que phiden ^ e <> 1
while pgc != 1:
	while c == 0:
		if ((p<e) and (q<e)) and (e<phiden):
			c = 1
		e += 1
	pgc = pgcd(e, phiden)
print("Clé publique : {} , {}".format(e, n))
textin = input("Tapez le texte à crypter : ")
t = len(textin)
i = 0
cry = []
while i < t:
	ascii = ord(mot[i]) # On covertit la lettre à crypter
	let = pow(ascii,e)%n # On crypte la lettre ou plutôt son code
	if ascii > n:
		print("p et q sont très petits, veuillez recommencez")
		break
	if let > phiden:
		print("Erreur de calcul")
		break
	cry.append(let)
	i += 1
print(cry)
print("Fin !")
