div = 3
S = 1
soma = False

for i in range(51):
	if(soma):
		S -= 1/(div**3)
		soma = True
	else:
		S += 1/(div**3)
		soma = False

	div += 2


pi = (S * 32) ** (1/3)

print("O valor de pi encontrado com 51 fatores é", pi)