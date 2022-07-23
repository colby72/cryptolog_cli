# This code is the property of Ramy Chmak
# ---------------------------------------

from data import *
import hashlib

# Tableur de caractères spéciaux
def cryptSpecial(text):
	n = 0
	for car, code in symbol_sp.items():
		if car == text:
			codout = code
			break
		n += 1
	if n == 0:
		print("Caractère introuvable dans le tableur ...")
	return codout
def decryptSpecial(text):
	n = 0
	for car, code in symbol_sp.items():
		if code == text:
			carout = car
			break
		n += 1
	if n == 0:
		print("Code introuvable dans le tableur ...")
	return carout

# Tableur de codes couleurs RVB
def cryptRVB(text):
	n = 0
	for nom, code in rvb_color.items():
		if nom == text:
			rvb = code
			n += 1
	if n == 0:
		rvb = "Couleur introuvable dans le tableur ..."
	return rvb
def decryptRVB(rvb):
	n = 0
	for nom, code in rvb_color.items():
		if code == rvb:
			text = nom
			n += 1
	if n == 0:
		text = "Code introuvable dans le tableau ..."
	return text

# Tableur de codes couleurs hexadécimaux
def cryptHexadecimal(text):
	n = 0
	for nom, code in hex_color.items():
		if nom == text:
			hex = code
			n += 1
	if n == 0:
		hex = "Couleur introuvable dans le tableur ..."
	return hex
def decryptHexadecimal(hex):
	n = 0
	for nom, code in hex_color.items():
		if code == hex:
			text = nom
			n += 1
	if n == 0:
		text = "Code introuvable dans le tableur ..."
	return text

# Convertisseur language binaire
def cryptBinary(ch):
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
def decryptBinary(bin):
	text = ""
	bin = str(bin)
	while bin != '':
		ch = bin[:8:]
		bin = bin[8::]
		ch = '0b' + ch
		ch = int(ch, 2)
		text += chr(ch)
	return text

# Chiffrement César (RoR 13)
def cryptCesar(text, key):
	text = text.upper().strip()
	key = int(key)
	let = []
	for i, l in enumerate(text):
		if l != ' ':
			x = num_alphabet[l]
			let.append(num_lettres[(x+key)%26])
		else:
			let.append(' ')
	cesar = "".join(let)
	return cesar

# Chiffrement Affine
def cryptAffine(text, keya, keyb):
	let = []
	text = text.upper().strip()
	keya = int(keya)
	keyb = int(keyb)
	for i, l in enumerate(text):
		if l != ' ':
			x = num_alphabet[l]
			let.append(num_lettres[((keya*x)+keyb)%26])
		else:
			let.append(' ')
	affine = "".join(let)
	return affine

# Fonctions de hashage
def hash_sha1(text):
	text = text.encode()
	crypt = hashlib.sha1(text).digest()
	hexcrypt = hashlib.sha1(text).hexdigest()
	return [crypt, hexcrypt]
def hash_sha224(text):
	text = text.encode()
	crypt = hashlib.sha224(text).digest()
	hexcrypt = hashlib.sha224(text).hexdigest()
	return [crypt, hexcrypt]
def hash_sha256(text):
	text = text.encode()
	crypt = hashlib.sha256(text).digest()
	hexcrypt = hashlib.sha256(text).hexdigest()
	return [crypt, hexcrypt]
def hash_sha384(text):
	text = text.encode()
	crypt = hashlib.sha384(text).digest()
	hexcrypt = hashlib.sha384(text).hexdigest()
	return [crypt, hexcrypt]
def hash_sha512(text):
	text = text.encode()
	crypt = hashlib.sha512(text).digest()
	hexcrypt = hashlib.sha512(text).hexdigest()
	return [crypt, hexcrypt]
def hash_md5(text):
	text = text.encode()
	crypt = hashlib.md5(text).digest()
	hexcrypt = hashlib.md5(text).hexdigest()
	return [crypt, hexcrypt]

# Convertisseur code Morse
def cryptMorse(text):
	text = text.upper()
	code = ""
	let = []
	for i, l in enumerate(text):
		if i<len(text)-1:
			let.append(morse_alphabet[l])
			if morse_alphabet[l] != '0000':
				let.append('000')
		else:
			let.append(morse_alphabet[l])
	code = "".join(let)
	return code
def decryptMorse(code):
	n = 0
	k = 0
	let = []
	cry = []
	tmp = []
	temp = []
	text = ""
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
		let.append(morse_lettres[m])
	text = "".join(let)
	return text

# Chiffre de Vigenère
def cryptVigenere(text, key):
	text = text.upper().strip()
	key = key.upper().strip()
	vig = ""
	t = len(text)
	k = len(key)
	let = []
	for i, l in enumerate(text):
		let.append(l)
		i += 1
	cod = []
	j = 0
	while j<t:
		if let[j] != ' ':
			x = num_alphabet[let[j]] + num_alphabet[key[j%k]]
			cod.append(num_lettres[x%26])
		else:
			cod.append(' ')
		j += 1
	vig = "".join(cod)
	return vig
def decryptVigenere(vig, key):
	vig = vig.upper().strip()
	key = key.upper().strip()
	text = ""
	k = len(key)
	v = len(vig)
	let = []
	for i, l in enumerate(vig):
		let.append(l)
		i += 1
	txt = []
	j = 0
	while j<v:
		if let[j] != ' ':
			x = num_alphabet[let[j]] - num_alphabet[key[j%k]]
			txt.append(num_lettres[x%26])
		else:
			txt.append(' ')
		j += 1
	text = "".join(txt)
	return text

# Chiffre de Hill
def cryptHill(text, a, b, c, d):
	text = text.upper()
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	code = ""
	let = []
	cry = []
	for i, l in enumerate(text):
		if ord(l) > 64 and ord(l) < 91:
			let.append(l)
	if len(let) % 2 != 0:
		let.append('X')
	i = 0
	while i < len(let)-1:
		x = num_lettres[((num_alphabet[let[i]]*a)+(num_alphabet[let[i+1]]*b)) % 26]
		y = num_lettres[((num_alphabet[let[i]]*c)+(num_alphabet[let[i+1]]*d)) % 26]
		cry.extend([x, y])
		i += 2
	code = "".join(cry)
	return code

# Chiffrement RSA
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
		while c == 0.0:
			if ((p<e) and (q<e)) and (e<phi):
				c = 1.0
			e += 1.0
		pg = pgcd(e, phi)
	cry = [n, phi, e]
	cipher = 1.0
	e = int(e)
	for i, l in enumerate(txt):
		x = ord(l)
		cipher = pow(x, e) % n
		cry.append(cipher)
	return cry
def decryptrsa(code, n, d):
	n = float(n)
	x = 1
	let = []
	for i, l in enumerate(code):
		x = pow(l, d) % n
		x = x % 256
		#x = int(x)
		let.append(chr(x))
	txt = "".join(let)
	return txt

# Stéganographie
def cryptStegano(pic, text):
	img = Image.open(pic)
	nom = 'stegano.bmp'
	imgg = stepic.encode(img, text)
	imgg.save(nom, 'BMP')
	return nom
def decryptStegano(pic):
	img = Image.open(pic)
	s = stepic.decode(img)
	d = d.decode()
	return d
