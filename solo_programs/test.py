nb = 1245557856321590
print(type(nb))
ch = str(nb)
print(ch)
print(type(ch))
ls = ch.split()
print(ls)
print(type(ls))
ls = []
for i, elt in enumerate(ch):
	ls.append(elt)
	i += 1
print(ls)
chh = "".join(ls)
print(chh)
let = []
nom = "ramy"
mot = "1245"
for i, l in enumerate(nom):
	if i<len(nom)-1:
		let.append(mot+"000")
	else:
		let.append(mot)
print(let)
lst = ['a', 'f', 'c']
print("lst --> ", len(lst))
