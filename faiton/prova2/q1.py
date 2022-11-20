def calcula_divisores(num):
	cont = 0
	for i in range(num):
		if num%(i+1) == 0:
			cont+=1

	return cont


numero = 300
while numero<= 400:
	num_div = calcula_divisores(numero)
	print("Numero: ", numero, "- qtia de divisores: ", num_div)
	numero+=1