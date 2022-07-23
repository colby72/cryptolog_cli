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
print("Main menu : ")
print("1- Tables for usual codes")
print("2- Translators")
print("3- Encryption and decryption")
print("4- Hashing")
print("5- Exit")
cryptolog = 'y'
while cryptolog == 'y':
	cat = ""
	prog = 'y'
	while cat != '1' and cat != '2' and cat != '3' and cat != '4' and cat != '5':
		cat = input("\nChoose a categorie from the main menu : ")
	doc = ""
	mod = ""
	if cat == '1':
		print("\nAvailable tables : ")
		print("1- Special caracters table")
		print("2- RVB color codes table")
		print("3- Hexadecimal color codes table")
		print("4- Back to main menu\n")
		while mod != '1' and mod != '2' and mod != '3' and mod != '4':
			mod = input("Choose a table : ")
		if mod == '1':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docSpecial()
			while prog.lower() == 'y':
				askSpecial()
				prog = input("Do you want to try again [Y/n] ? ")
			mod = ""
		elif mod == '2':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docRVB()
			while prog.lower() == 'y':
				askRVB()
				prog = input("Do you want to try again [Y/n] ? ")
			mod = ""
		elif mod == '3':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docHexadecimal()
			while prog.lower() == 'y':
				askHexadecimal()
				prog = input("Do you want to try again [Y/n] ? ")
			mod = ""
		elif mod == '4':
			print("Return to main menu ...")
			cat = ""
		else:
			print("Table selected unknown !")
			cryptolog = 'n'
	elif cat == '2':
		print("\nAvailable translators : ")
		print("1- Binary translator")
		print("2- Morse code translator")
		print("3- Return to main menu\n")
		while mod != '1' and mod != '2' and mod != '3':
			mod = input("Choose a translator : ")
		if mod == '1':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docBinary()
			while prog.lower() == 'y':
				askBinary()
				prog = input("Do you want to try again [Y/n] ? ")
			mod = ""
		elif mod == '2':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the  documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docMorse()
			while prog.lower() == 'y':
				askMorse()
				prog = input("Do you want to try again [Y/n] ? ")
			mod = ""
		elif mod == '3':
			print("Return to main menu ...")
			cat = ""
		else:
			print("Translator selected unknown !")
			cryptolog = 'n'
	elif cat == '3':
		print("\nAvailable encryption systems : ")
		print("1- Cesar cipher")
		print("2- Affine cipher")
		print("3- Vigenere cipher")
		print("4- Hill cipher")
		print("5- RSA cipher")
		print("6- Steganography")
		print("7- Return to main menu\n")
		while mod != '1' and mod != '2' and mod != '3' and mod != '4' and mod != '5' and mod != '6' and mod != '7':
			mod = input("Choose an encryption system : ")
		if mod == '1':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docCesar()
			while prog.lower() == 'y':
				askCesar()
				prog = input("Do you want to try again [Y/n] ? ")
			cat = ""
		elif mod == '2':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docAffine()
			while prog.lower() == 'y':
				askAffine()
				prog = input("Do you want to try again [Y/n] ? ")
			cat = ""
		elif mod == '3':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docVigenere()
			while prog.lower() == 'y':
				askVigenere()
				prog = input("Do you want to try again [Y/n] ? ")
			cat = ""
		elif mod == '4':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docHill()
			while prog.lower() == 'y':
				askHill()
				prog = input("Do you want to try again [Y/n] ? ")
			cat = ""
		elif mod == '5':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docRSA()
			while prog.lower() == 'y':
				askRSA()
				prog = input("Do want to try again [Y/n] ? ")
			cat = ""
		elif mod == '6':
			while doc.lower() != 'y' and doc.lower() != 'n':
				doc = input("Do you want to print the documentation [Y/n] ? ")
			if doc.lower() == 'y':
				docStegano()
			while prog.lower() == 'y':
				askStegano()
				prog = input("Do you want to try again [Y/n] ? ")
			cat = ""
		elif mod == '7':
			print("Return to main menu ...")
			cat = ""
		else:
			print("Encryption system selected unknown !")
			cryptolog = ""
	elif cat == '4':
		while doc.lower() != 'y' and doc.lower() != 'n':
			doc = input("Do you want to print the documentation [Y/n] ? ")
		if doc.lower() == 'y':
			docHash()
		while prog.lower() == 'y':
			askHash()
			prog = input("Do you want to try again [Y/n] ? ")
		cat = ""
	elif cat == '5':
		cryptolog = 'n'
	else:
		print("Category selected unknown !")
		cryptolog = 'n'
print("[CRYPTOLOG] Terminate ...")
