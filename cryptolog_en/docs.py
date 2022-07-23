# This code is the property of Ramy Chmak
# ---------------------------------------

# Documentation pour tableur de couleurs RVB
def docRVB():
	print("Explications about RGB color codes")
	print("----------------------------------\n")
	print("Every color is composed of Red, Green and Blue, but with different intensities.")
	print("The RGB color code is composed of three numbers starting from 0 to 255. It indicates the intensity of Red, Green and Blue respectively.")
	print("255 for the three is for the white, while 0 for the three is for the black.\n")

# Documentation pour tableur de couleurs hexadécimaux
def docHexadecimal():
	print("Explications about hexadecimal color codes")
	print("------------------------------------------\n")
	print("The hexadecimal color code is quite simalar to RGB, à part quelques nuances.")
	print("syntactically, in the hexadecimal code intensities of Red, Green and Blue colors aren't separated, and they're preceded by #.")
	print("Moreover, these intensities are expressed in base16, so numbers goes from '00' to 'FF'.\n")

# Documentation pour tableur de codes de caractères spéciaux
def docSpecial():
	print("Explications about HTML special caracter codes")
	print("----------------------------------------------\n")
	print("In HTML coding, many special caracters such as accented letters or scientific symbols can't be interpreted directly by browsers.")
	print("Browsers displays incomprehensible codes when they find these special caracters in the source code.")
	print("That's why in our source files, we write some codes instead of these special caracters so browers know how to display the special caracter correctly, with a code for each special caracter.\n")

# Documentation pour traducteur de language binaire
def docBinary():
	print("Explications about binary language")
	print("----------------------------------\n")
	print("Presentation :")
	print("For those who ignore it, computers understand only binary language, just 0 and 1.")
	print("All received data are translated to binary, treated, then retranslated to human language, so they can be sent to standard output(monitor, printer ...).")
	print("But for humans, it's really hard to speak binary language. That's why we have to translate our messages in binary and vice-versa.")
	print("\nPrinciple :")
	print("Translation from human language to binary language :")
	print("The translation is done caracter by caracter.")
	print("To translate a caracter, we note its ASCII code, we do a serial of divisions by 2 on this code.")
	print("Puisque le reste de la division euclidienne d'un nombre par 2 est soit 1, soit 0, on note à chaque fois ce reste en allant de droite à gauche jusqu'à avoir un quotient égal à 0 ou égal à 1.")
	print("Après avoir obtenu une série de 0 et de 1, il faut que cette série soit composée de 8 chiffres, donc on doit ajouter des 0 à gauche si nécessaire.")
	print("Traduction du language machine en language humain :")
	print("La traduction se fait par bloc de 8 chiffres. De droite à gauche, chaque chiffre présente une puissance de 2; Il sécrit sous la forme de 2^n.")
	print("n est variable selon le rang du chiffre : allant de 0 à 7. Ce que nous donne un total de 256 combinaisons.")
	print("Puis, on fait la somme des puissances de 2 pour trouver le code ASCII correspondant au caractère recherché.\n")

# Documentation pour traducteur de code Morse
def docMorse():
	print("Explications à propos du code Morse")
	print("-----------------------------------\n")
	print("Présentation :")
	print("Le code Morse inventé au 19ème siècle, permet de transmettre un message par une série d'impulsions (lumineuses, éléctriques, clignements des yeux, ...).")
	print("Il était largement utilisé au 20ème siècle pour des fins militaires.")
	print("Mais il est surtout utilisé pour la signalisation maritime, par les radioamateurs et en cas de détresse.")
	print("\nPrincipe :")
	print("Chaque caractère correspond à une combinaison unique d'impulsions.")
	print("Dans Cryptolog, on utilise 0 pour un signal inactif et 1 pour un signal actif.")
	print("On tape le code correspondant au caractère à coder, suivi par 3 signaux inactifs pour indiquer la fin du caractère.")
	print("On utilise aussi sept signaux nuls pour séparer les mots.\n")

# Documentation pour programme de chiffrement César
def docCesar():
	print("Explications à propos du chiffrement César")
	print("------------------------------------------\n")
	print("Présentation :")
	print("Le chiffrement est utilisé depuis des milliers d'années pour rendre un texte clair incompréhensible pour le public.")
	print("Seul en possesion des clés de chiffrement et déchiffrement, on peut comprendre le cryptogramme.")
	print("Il existe plusieurs méthodes de chiffrement dont la méthode César utilisée par Jules César il y a plus de 3000 ans pour sécuriser la transmission des messages au sein de l'armée romaine.")
	print("Le chiffre de César est dit symétrique, car on peut déchiffrer un cryptogramme à partir de la clé de chiffrement.")
	print("\nPrincipe :")
	print("On attribut aux lettres de l'alphabet des numéros allant de 0 à 25 (0 pour A, 1 pour B, ..., 25 pour Z).")
	print("Les rangs des lettres seront congru à modulo 26. Ainsi le nombre 57 par exemple donnera E (57 = 2 * 26 + 5).")
	print("On choisit une clé de chiffrement qu'on appelera KEY. Cette clé sera sous la forme d'un nombre congru à modulo 26.")
	print("Donc la fonction de chiffrement sera : y = x + KEY, avec y le rang de la lettre chiffrée et x le rang de la lettre à chiffrer.")
	print("Le principe consiste à décaler le rang de chaque lettre du message clair par la clé de chiffrement.")
	print("Par conséquence, la clé de déchiffrement sera '- KEY' modulo 26.\n")

# Documentation pour programme de chiffrement Affine
def docAffine():
	print("Explications à propos du chiffrement Affine")
	print("-------------------------------------------\n")
	print("Présentation : ")
	print("Le chiffrement est utilisé depuis des milliers d'années pour rendre un texte clair incompréhensible pour le public.")
	print("Seul en possesion des clés de chiffrement et déchiffrement, on peut comprendre le cryptogramme.")
	print("Il existe plusieurs méthodes de chiffrement dont la méthode de chiffrement Affine.")
	print("Le chiffre de Affine est dit symétrique, car on peut déchiffrer un cryptogramme à partir de la clé de chiffrement.")
	print("\nPrincipe :")
	print("On attribut aux lettres de l'alphabet des numéros allant de 0 à 25 (0 pour A, 1 pour B, ..., 25 pour Z).")
	print("Les rangs seront congru à modulo 26. Ainsi le nombre 57 par exemple donnera E (57 = 2 * 26 + 5).")
	print("On choisit une clé de chiffrement qu'on appelera KEY, composée de nombre a et b.")
	print("Donc la fonction de chiffrement sera : y = (a * x) + b, avec y le rang de la lettre chiffrée et x le rang de la lettre à chiffrer.")
	print("Le déchiffrement d'un cryptogramme se fait par le même principe.\n")

# Documentation pour programme de chiffre Vigenère
def docVigenere():
	print("Explications à propos du chiffre Vigenère")
	print("-----------------------------------------\n")
	print("Présentation :")
	print("Le chiffrement est utilisé depuis des milliers d'années pour rendre un texte clair incompréhensible pour le public.")
	print("Seul en possesion des clés de chiffrement et déchiffrement, on peut comprendre le cryptogramme.")
	print("Il existe plusieurs méthodes de chiffrement dont la méthode de Vigenère.")
	print("Le chiffre de Vigenère est dit symétrique, car on peut déchiffrer un cryptogramme à partir de la clé de chiffrement.")
	print("\nPrincipe :")
	print("On attribut aux lettres de l'alphabet des numéros allant de 0 à 25 (0 pour A, 1 pour B, ..., 25 pour Z).")
	print("Les rangs des lettres seront congru à modulo 26. Ainsi le nombre 57 par exemple donnera E (57 = 2 * 26 + 5).")
	print("On choisit une clé de chiffrement qu'on appelera KEY, sous formed'un mot, une phrase, ou même une pragraphe.")
	print("Pour chaque lettre du message, on note lettre au rang correspondant de KEY par rapport à la longueur du message. On parle pas du rang alphabétique. Puis on trouve la lettre codée en se référant au table de Vigenère, et ainsi de suite avec la deuxième lettre et ...")
	print("Si le message est plus long que KEY, on continue à répéter KEY jusqu'à avoir la longueur du message. Autrement dit, on travaille en congru modulo k; k = longueur de KEY.")
	print("Par contre, le programme présenté dans Cryptolog ne connait pas la table de Vigenère, il utilise une formule mathématique pour Chiffrer et déchiffrer les messages.")
	print("On note y le rang alphabétique de la lettre codé, x le rang alphabétique de la lettre à coder et c le rang alphabétique de la lettre de KEY.")
	print("La formule de chiffrement sera donc : y = x + c")
	print("La formule de déchiffrement est : x = y - c\n")

# Documentation pour programme de chiffre de Hill
def docHill():
	print("Explications à propos du chiffre de Hill")
	print("----------------------------------------\n")
	print("Présentation :")
	print("Inventé en 1929 par Lester Hill, le chiifrement est devenu un des plus célèbres aujourd'hui.")
	print("Le chiffre de Hill est dit symétrique car on peut déchiffrer un cryptogramme à partir de la clé de chiffrement.")
	print("Les clés de chiffrement et déchiffrement sont des matrices : |a  b|")
	print("                                                             |c  d|")
	print("\nPrincipe :")
	print("On attribut aux lettres de l'alphabet des numéros allant de 0 à 25 (0 pour A, 1 pour B, ..., 25 pour Z).")
	print("Les rangs des lettres seront congru à modulo 26. Ainsi le nombre 57 par exemple donnera E (57 = 2 * 26 + 5).")
	print("On regroupe les lettres par couples: (c1, c2), (c3, c4), (c5, c6) ...")
	print("Les lettres cryptées seront aussi par couples: (p1, p2), (p3, p4), (p5, p6) ...")
	print("On crypte les couples de lettres selon la formule: p1 = [(a*c1) + (b*c2)] mod 26")
	print("                                                   p2 = [(c*c1) + (d*c2)] mod 26")
	print("Le déchiffrement se fait de lamême manière, mais pas avec la même matrice.")
	print("La matrice de déchiffrement est l'inverse de la matrice de chiffrement.")
	print("Cryptolog ne peut pas encore déchiffrer des messages aves la clé de chiffrement, il a besoin d'une clé de déchiffrement prête.\n")

# Documentation pour programme de chiffre RSA
def docRSA():
	print("Explications à propos du chiffrement RSA")
	print("----------------------------------------\n")
	print("Présentation :")
	print("Les méthodes de cryptage sont tous basées sur des principes mathématiques. On cherche toujours des formules simples et efficaces.")
	print("Une de ces méthodes est la méthode RSA inventé par Rivest, Shamir et Adleman en 1978, et c'est la plus répondue de nos jours.")
	print("Cette méthode est surtout utilisée par les gouvernements, les militaires et quelques banques.")
	print("Aujourd'hui, le chiffrement RSA est le plus sur et le plus difficile à casser.")
	print("Le chiffrement RSA est dit asymétrique car la clé de cryptage n'est pas la même de décryptage.")
	print("\nPrincipe :")
	print("On commence par choisir deux grands nombres premiers p et q, plus qu'il soirnt grands, plus il sera difficile de casser le code.")
	print("On calcule n = p * q, puis phi de n : phi = (p-1) * (q-1).")
	print("On cherche la puissance d'encryptage e, tel que e < p, e < q et e < Phi et pgcd(e, Phi) = 1.")
	print("Le couple (e, n) est la clé publique qui permet de crypter les messages selon la formule c = m^e mod n.")
	print("On utilise à la place des lettres, leurs codes ASCII, avec c le crypté et m le message.")
	print("On détermine après la puissance de décryptage d, tel que d = 1/e mod phi.")
	print("Le couple (d, n) est la clé privée qui permet de décrypter les cryptogrammes selon la formule m = c^d mod n.\n")

# Documentation pour programme de stéganographie
def docStegano():
	print("Explications à propos de la stéganographie")
	print("------------------------------------------\n")
	print("La stéganographie est l'art de cacher des messages, des documents, des fichiers en général, derrière une image.")
	print("Le programme inclut dans Cryptolog ne permet de cacher que du texte.")
	print("")

# Documentation pour programme de hashage
def docHash():
	print("Explications à propos des fonctions de Hashage")
	print("----------------------------------------------\n")
	print("Le hashage permet de convertir des entrées de taille variable vers une taille fixe (ou signature).")
	print("Il permet le calcul d'empreintes uniques, c'est donc une fonction à sens unique (on peut pas trouver l'antècédent d'un haché).")
	print("Il est utilisé dans le stockage des mots de passe, les codes d'authentification des messages, la vérification d'intégrité ...")
	print("Une fonction de hashage doit se comporter aléatoirement, donc il n'y a aucune relation entre le haché et le message d'entrée.")
	print("Donc il est extrêment difficile de fabriquer deux messages donnant le même haché.")
	print("La force d'une foction de hashage est meusuré par sa résistance aux collisions et aux préimages.")
	print("La sortie est généralement un code hexadécimal de taille fixe.")
	print("Cryptolog renvoie le haché sous deux formes: la première de type byte, et la deuxème en hexadécimal.")
	print("Il existe plusieurs fonctions de hashage : MD2, MD4, RIPEMD, HAVAL, Tiger, Whirlpool, AES, SHA-0, SHA-2, ...")
	print("Les fonctions les plus utilisées de nos jours sont ceux des familles MD et SHA.")
	print("\nVoici les fonctions traîtées par Cryptolog :\n")
	print("Fonction\tTaille du haché")
	print("--------\t---------------")
	print("MD5\t\t32 caractères")
	print("SHA-1\t\t40 caractères")
	print("SHA-224\t\t56 caractères")
	print("SHA-256\t\t64 caractères")
	print("SHA-384\t\t96 caractères")
	print("SHA-512\t\t128 caractères\n")
