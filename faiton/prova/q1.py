div = 3
res = 4
soma = False

while (4/div >= 0.0001):
	if (soma):
		res += 4/div
		soma = False
	else:
		res -= 4/div
		soma = True

	div += 2

print("O valor de pi encontrado é", res)