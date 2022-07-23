def pgcd(a, b):
	if b == 0:
		return a
	else:
		r = a % b
		return pgcd(b, r)
x = input("Tapez x : ")
x = int(x)
y = input("Tapez y : ")
y = int(y)
p = pgcd(x, y)
print("==> ", p)
