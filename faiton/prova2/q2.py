def candidato_mais_votado(lista_dados, sexo):
	votos_A = 0
	votos_B = 0
	votos_C = 0
	for i in range(150):
		if(sexo != None):
			if(lista_dados[i][2] == sexo):
				if(lista_dados[i][0] == "A"):
					votos_A+=1
				elif(lista_dados[i][0] == "B"):
					votos_B+=1
				else:
					votos_C+=1
		else:
			if(lista_dados[i][0] == "A"):
					votos_A+=1
			elif(lista_dados[i][0] == "B"):
				votos_B+=1
			else:
				votos_C+=1

	if(votos_A>=votos_B and votos_A>=votos_C):
		mais_votado = "A"
	elif(votos_B>=votos_A and votos_B>=votos_C):
		mais_votado = "B"
	else:
		mais_votado = "C"

	return mais_votado

def media_de_idade(lista_dados, mais_votado):
	total = 0
	cont = 0
	for i in range(150):
		if(lista_dados[i][0] == mais_votado):
			total+=int(lista_dados[i][1])
			cont+=1

	media = total/cont
	return media


lista_dados = []
for i in range(150):
	print("Dados numero:", i)
	cand = input("Informe o candidato (A, B ou C):")
	idade = input("Informe a idade:")
	sexo = input("Informe o sexo:")
	
	lista_dados.append((cand, idade, sexo))

print(lista_dados)

mais_votado = candidato_mais_votado(lista_dados, None)
media_idade = media_de_idade(lista_dados, mais_votado)
pref_mulh = candidato_mais_votado(lista_dados, "F") #Considerando que o sexo é representado por letras M ou F

print("O candidato mais votado é:", mais_votado)
print("A média de idade dos eleitores do candidato mais votado é:", media_idade)
print("O candidato preferido das mulheres é:", pref_mulh)