def calcula_digitos(num):
	dig = 0
	temp = num
	while(temp>1):
		temp /= 10
		dig += 1

	return dig

num = int(input("Informe o número a ser verificado: "))
resto = num%10

num_dig = calcula_digitos(num)
num_dig -= 1
temp = num
novo_num = 0
cont = 1

while (num_dig>=0):
	dig_atual = (temp%(10**cont))/(10**(cont-1))
	novo_num += dig_atual*(10**num_dig)
	num_dig -= 1
	cont += 1
	temp -= dig_atual*(10**(cont-2))

if(novo_num == num):
	print("O numero é capicua")
else:
	print("O numero nao é capicua")

