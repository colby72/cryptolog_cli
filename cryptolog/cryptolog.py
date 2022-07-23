# This code is the property of Ramy Chmak
# ---------------------------------------

from programs import *
from docs import *

print("******************************************************")
print("*                                                    *")
print("*"+"Cryptolog v1.0 Build 2015".center(52)+"*")
print("*"+"Developed by Ramy Chmak".center(52)+"*")
print("*                                                    *")
print("******************************************************\n\n")
print("Menu principal : ")
print("1- Tableur de codes usuels")
print("2- Traducteur de langue")
print("3- Chiffrement et déchiffrement")
print("4- Hashage")
print("5- Quitter")
cryptolog = 'o'
while cryptolog == 'o':
	cat = ""
	prog = 'o'
	while cat != '1' and cat != '2' and cat != '3' and cat != '4' and cat != '5':
		cat = input("\nChoisissez une catégorie : ")
	doc = ""
	mod = ""
	if cat == '1':
		print("\nTableurs disponibles : ")
		print("1- Tableur caractères spéciaux")
		print("2- Tableur codes couleurs RVB")
		print("3- Tableur codes couleurs hexadécimaux")
		print("4- Retour au menu principal\n")
		while mod != '1' and mod != '2' and mod != '3' and mod != '4':
			mod = input("Choisissez un tableur : ")
		if mod == '1':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docSpecial()
			while prog.lower() == 'o':
				askSpecial()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			mod = ""
		elif mod == '2':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docRVB()
			while prog.lower() == 'o':
				askRVB()
				prog = input("Voulez-vous réessayez [O/n] ? ")
			mod = ""
		elif mod == '3':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docHexadecimal()
			while prog.lower() == 'o':
				askHexadecimal()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			mod = ""
		elif mod == '4':
			print("Retour au menu principal ...")
			cat = ""
		else:
			print("Tableur choisi inconnu !")
			cryptolog = 'n'
	elif cat == '2':
		print("\nTraducteurs disponibles : ")
		print("1- Traducteur de language binaire")
		print("2- Traducteur de code Morse")
		print("3- Retour au menu principal\n")
		while mod != '1' and mod != '2' and mod != '3':
			mod = input("Choisissez un traducteur : ")
		if mod == '1':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docBinary()
			while prog.lower() == 'o':
				askBinary()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			mod = ""
		elif mod == '2':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docMorse()
			while prog.lower() == 'o':
				askMorse()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			mod = ""
		elif mod == '3':
			print("Retour au menu principal ...")
			cat = ""
		else:
			print("Traducteur choisi inconnu !")
			cryptolog = 'n'
	elif cat == '3':
		print("\nSystèmes de chiffrement disponibles : ")
		print("1- Chiffrement César")
		print("2- Chiffrement Affine")
		print("3- Chiffrement Vigenère")
		print("4- Chiffre de Hill")
		print("5- Chiffre RSA")
		print("6- Stéganographie")
		print("7- Retour au menu principal\n")
		while mod != '1' and mod != '2' and mod != '3' and mod != '4' and mod != '5' and mod != '6' and mod != '7':
			mod = input("Choisissez un système de chiffrement : ")
		if mod == '1':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docCesar()
			while prog.lower() == 'o':
				askCesar()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			cat = ""
		elif mod == '2':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docAffine()
			while prog.lower() == 'o':
				askAffine()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			cat = ""
		elif mod == '3':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docVigenere()
			while prog.lower() == 'o':
				askVigenere()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			cat = ""
		elif mod == '4':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docHill()
			while prog.lower() == 'o':
				askHill()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			cat = ""
		elif mod == '5':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docRSA()
			while prog.lower() == 'o':
				askRSA()
				prog = input("Voulez-vous réessayer [O/n] ? ")
			cat = ""
		elif mod == '6':
			while doc.lower() != 'o' and doc.lower() != 'n':
				doc = input("Voulez-vous afficher la documentation [O/n] ? ")
			if doc.lower() == 'o':
				docStegano()
			while prog.lower() == 'o':
				askStegano()
				prog = input("Voulez-vous réessayez [O/n] ? ")
			cat = ""
		elif mod == '7':
			print("Retour au menu principal ...")
			cat = ""
		else:
			print("Système de chiffrement inconnu !")
			cryptolog = ""
	elif cat == '4':
		while doc.lower() != 'o' and doc.lower() != 'n':
			doc = input("Voulez-vous afficher la documentation [O/n] ? ")
		if doc.lower() == 'o':
			docHash()
		while prog.lower() == 'o':
			askHash()
			prog = input("Voulez-vous réessayer [O/n] ? ")
		cat = ""
	elif cat == '5':
		cryptolog = 'n'
	else:
		print("Catégorie choisie inconnue !")
		cryptolog = 'n'
print("[CRYPTOLOG] Fin du programme ...")
