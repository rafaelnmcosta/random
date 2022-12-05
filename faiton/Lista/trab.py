##
# Função auxiliar que verifica se um determinado elemento existe em um conjunto
# Executa uma busca sequencial simples comparando cada elemento de conj com
# o item informado. Assim que uma correspondência é encontrada, retorna True,
# Caso conj seja percorrido sem correspondência, retorna False
# # 
def existe_no_conjunto(item, conj):
	for i in conj:
		if item == i:
			return True

	return False

##
# Declara o novo_conj, lê a quantidade N de itens que serão incluídos;
# Executa um laço para ler as N entradas, e verifica se a entrada não foi
# digitada anteriormente.
# Caso a entrada ainda não exista no conjunto, ela é então adicionada à novo_conj,
# caso exista, é pedida uma nova entrada ao usuário, até que uma válida seja informada
# Retorna o conjunto recém criado novo_conj;
# #
def le_conjunto():
	novo_conj = []
	tamanho = int(input("Informe quantos elementos o conjunto possuirá: "))
	i=0
	while i < tamanho:
		elemento = int(input("Insira o " + str(i+1) + "o elemento do conjunto: "))
		if existe_no_conjunto(elemento, novo_conj):
			print("Esse elemento já existe no conjunto!")
		else:
			novo_conj.append(elemento)
			i = i+1

	print("Conjunto criado!: ", novo_conj)
	return novo_conj

##
# Verifica se o tamanho do conjunto é 0.
# Retorna True para vazio, False para não vazio
# #
def vazio(conj):
	if len(conj) == 0:
		#print("O conjunto é vazio")
		return True
	else:
		#print("O conjunto não é vazio")
		return False

##
# Primeiro adiciona todos os elemento do conj1 ao novo_conj,
# depois verifica se cada item do conj2 existe no conj1
# (para não adicionar elementos repetidos), caso não exista
# adiciona o item ao novo_conj.
# Retorna a união novo_conj
# #
def uniao(conj1, conj2):
	novo_conj =[]
	for item in conj1:
		novo_conj.append(item)
	for item in conj2:
		if not existe_no_conjunto(item, conj1):
			novo_conj.append(item)

	print("União: ", novo_conj)
	return novo_conj

##
# Primeiro encontra qual é o maior entre os dois conjuntos,
# então verifica se cada elemento do maior conjunto existe
# no menor conjunto, e caso exista, adiciona ele ao novo_conj.
# Se novo_conj é vazio, não há intersecção,
# se não é vazio, a intersecção novo_conj é retornada
# #
def interseccao(conj1, conj2):
	novo_conj = []
	if len(conj1) >= len(conj2):
		for i in conj1:
			if existe_no_conjunto(i, conj2):
				novo_conj.append(i)
	else:
		for i in conj2:
			if existe_no_conjunto(i, conj1):
				novo_conj.append(i)

	if vazio(novo_conj):
		print("Não há intersecção entre os conjuntos!")
	else:
		print("Intersecção: ", novo_conj)
		return novo_conj

##
# Verifica se cada elemento do conj1 existe no conj2 e,
# caso NÃO exista, ele adiciona ao novo_conj.
# Retorna o novo_conj que é o resultado da subtração.
# # 
def subtrai(conj1, conj2):
	novo_conj = []
	for i in conj1:
		if not existe_no_conjunto(i, conj2):
			novo_conj.append(i)

	print("Subtração realizada: ", novo_conj)
	return novo_conj

##
# Verifica se cada um dos elementos do conj1 existe no conj2,
# se um elemento não existir em conj2, retorna false pois não
# é um subconjunto, do contrário, retorna true
# # 
def subconjunto(conj1, conj2):
	for i in conj1:
		if not existe_no_conjunto(i, conj2):
			return False

	return True

##
# Primeiro encontra qual o maior conjunto, e então verifica se cada
# item do maior conjunto está no menor conjunto. Caso encontre uma correspondência,
# retorna False, pois isso indica que possuem elementos em comum.
# Caso não seja encontradas correspondências entre os dois conjuntos,
# retorna True, pois são disjuntos.
# #
def disjunto(conj1, conj2):
	if conj1 >= conj2:
		for item in conj1:
			if existe_no_conjunto(item, conj2):
				return False
	else:
		for item in conj2:
			if existe_no_conjunto(item, conj1):
				return False

	return True

##
# Primeiro verifica se os dois conjuntos são de mesmo tamanho, caso
# não sejam, já retorna False pois não são identicos.
# Em seguida verifica se todos os elementos de conj1 existem em conj2,
# e depois se todos os elementos de conj2 estão em conj1.
# Caso exista uma divergência retorna False pois não são identicos.
# Se não houver divergências retorna True: são identicos.
# # 
def identicos(conj1, conj2):
	if len(conj1) != len(conj2):
		return False
	else:
		for item in conj1:
			if not existe_no_conjunto(item, conj2):
				return False
		for item in conj2:
			if not existe_no_conjunto(item, conj1):
				return False
		
	return True

##
# Primeiro ordena o conjunto conj para que o menor elemento seja o primeiro
# e o maior elemento seja o ultimo da lista. Então guarda as posições do maior
# e menor elemento e armazena a diferença entre eles em amp.
# Retorna amp que é a amplitude.
# #
def amplitude(conj):
	conj_ord = ordena(conj)
	pos_maior = len(conj)-1
	pos_menor = 0

	amp = conj_ord[pos_maior] - conj_ord[pos_menor]
	return amp

##
# Primeiro verifica se os conjuntos possuem a mesma quantidade de elementos
# para calcular o produto escalar.
# Em seguida percorre o conj1 realizando a multiplização de cada item de conj1
# pelo seu correspondente em conj2 e somando o resultado à variável prod;
# Retorna prod, resultado do produto escalar.
# #
def prod_escalar(conj1, conj2):
	if len(conj1) != len(conj2):
		print("Não é possível calcular o produto escalar!")
	else:
		prod = 0
		for i in range(len(conj1)):
			prod = prod + (conj1[i] * conj2[i])

		return prod

##
# Cria uma cópia do conjunto conj e a ordena através da função sort()
# Retorna o conjunto ordenado novo_conj
# #
def ordena(conj):
	novo_conj = []
	for item in conj:
		novo_conj.append(item)

	novo_conj.sort()
	return novo_conj

##
# Encontra o tamanho do conjunto através da função len() e encontra
# a soma total do conjunto através da função sum().
# Calcula a media através da divisão de total por tamanho.
# Retorna a media
# #
def media(conj):
	tamanho = len(conj);
	total = sum(conj);

	media = total/tamanho;
	return media

##
# Função principal do programa; é responsável por exibir um menu, ler a entrada
# do usuário e executar a função especificada de acordo com a requisição.
# Implementa as 7 listas de acordo com os conjuntos pedidos no trabalho:
# (A. B, C, D, E, F e I) e as altera através das funções anteriores.
# 
# As variáveis run, run1 e run2 são responsáveis por garantir o loop do menu
# para aguardar uma resposta válida do usuário.
# As variáveis opt e var são responsáveis por armazenar as escolhas do usuário
# nos respectivos menus.
# 
# É poaaível fazer a verificação de todos os conjuntos durante a execução
# através da opção 2
# Após a leitura de novos conjuntos iniciais A e B, os conjuntos seguintes são
# redefinidos para não armazenar dados desatualizados.
# 
# Não há retorno pois o fim dessa função representa o fim do programa.
# #
def menu():
	run = True
	opt = 0
	conjA = []
	conjB = []
	conjC = []
	conjD = []
	conjE = []
	conjF = []
	conjI = []

	while run:
		print("\n---------- Teoria dos conjuntos ----------\n")
		print("Escolha a função desejada:")
		print("1 - Ler os conjuntos A e B")
		print("2 - Exibir os conjuntos")
		print("3 - Descobrir se o conjunto é vazio")
		print("4 - Conjunto C: União entre A e B")
		print("5 - Conjunto D: Intersecção entre A e B")
		print("6 - Conjunto E: Subtração A-B")
		print("7 - Conjunto F: Subtração B-A")
		print("8 - Descobrir se A é subconjunto de B")
		print("9 - Descobrir se B é subconjunto de A")
		print("10 - Descobrir se A e B são idênticos")
		print("11 - Descobrir se A e B são disjuntos")
		print("12 - Calcular a amplitude de A e B")
		print("13 - Calcular o produto escalar entre A e B (se possível)")
		print("14 - Conjunto I: Ordenação de A U B")
		print("15 - Calcular a média aritmética de um conjunto")
		print("99 - Encerrar o programa\n")
		opt = input()
		match opt:
			case '1':
				print("\nConjunto A:")
				conjA = le_conjunto()
				print("\nConjunto B:")
				conjB = le_conjunto()
				conjC = []
				conjD = []
				conjE = []
				conjF = []
				conjI = []

			case '2':
				print("\nConjunto A: ", conjA)
				print("Conjunto B: ", conjB)
				print("Conjunto C: ", conjC)
				print("Conjunto D: ", conjD)
				print("Conjunto E: ", conjE)
				print("Conjunto F: ", conjF)
				print("Conjunto I: ", conjI)

			case '3':
				run1 = True
				while run1:
					var = input("\nInforme qual conjunto deseja verificar se é vazio (A ou B): ")
					match var:
						case 'A':
							if vazio(conjA):
								print("\nO conjunto A é vazio")
								run1 = False
							else:
								print("\nO conjunto A não é vazio")
								run1 = False
						case 'a':
							if vazio(conjA):
								print("\nO conjunto A é vazio")
								run1 = False
							else:
								print("\nO conjunto A não é vazio")
								run1 = False
						case 'B':
							if vazio(conjB):
								print("\nO conjunto B é vazio")
								run1 = False
							else:
								print("\nO conjunto B não é vazio")
								run1 = False
						case 'b':
							if vazio(conjB):
								print("\nO conjunto B é vazio")
								run1 = False
							else:
								print("\nO conjunto B não é vazio")
								run1 = False
						case _:
							print("Opção inválida!")

			case '4':
				conjC = uniao(conjA, conjB)

			case '5':
				conjD = interseccao(conjA, conjB)
			case '6':
				conjE = subtrai(conjA, conjB)

			case '7':
				conjF = subtrai(conjB, conjA)

			case '8':
				if subconjunto(conjA, conjB):
					print("\nO conjunto A é um subconjunto de B")
				else:
					print("\nO conjunto A não é um subconjunto de B")

			case '9':
				if subconjunto(conjB, conjA):
					print("\nO conjunto B é um subconjunto de A")
				else:
					print("\nO conjunto B não é um subconjunto de A")

			case '10':
				if identicos(conjA, conjB):
					print("\nOs conjuntos A e B são identicos")
				else:
					print("\nOs conjuntos A e B não são identicos")

			case '11':
				if disjunto(conjA, conjB):
					print("\nOs conjuntos A e B são disjuntos")
				else:
					print("\nOs conjuntos A e B não são disjuntos")
			case '12':
				ampA = amplitude(conjA)
				ampB = amplitude(conjB)
				print("\nAmplitude do conjunto A: ", ampA)
				print("Amplitude do conjunto B: ", ampB)

			case '13':
				prod_esc = prod_escalar(conjA, conjB)
				print("\nO produto escalar entre A e B é: ", prod_esc)

			case '14':
				conjI = ordena(conjC)
				print("\nConjunto ordenado com os itens de A e B: ", conjI)

			case '15':
				run2 = True
				while run2:
					var = input("\nInforme qual conjunto deseja calcular a média aritmética (A, B, C, D, E, F, ou I): ")
					match var:
						case 'A':
							med = media(conjA)
							print("A media do conjunto A é: ", med)
							run2 = False

						case 'B':
							med = media(conjB)
							print("A media do conjunto B é: ", med)
							run2 = False

						case 'C':
							med = media(conjC)
							print("A media do conjunto C é: ", med)
							run2 = False

						case 'D':
							med = media(conjD)
							print("A media do conjunto D é: ", med)
							run2 = False

						case 'E':
							med = media(conjE)
							print("A media do conjunto E é: ", med)
							run2 = False

						case 'F':
							med = media(conjF)
							print("A media do conjunto F é: ", med)
							run2 = False

						case 'I':
							med = media(conjI)
							print("A media do conjunto I é: ", med)
							run2 = False

						case 'a':
							med = media(conjA)
							print("A media do conjunto A é: ", med)
							run2 = False

						case 'b':
							med = media(conjB)
							print("A media do conjunto B é: ", med)
							run2 = False

						case 'c':
							med = media(conjC)
							print("A media do conjunto C é: ", med)
							run2 = False

						case 'd':
							med = media(conjD)
							print("A media do conjunto D é: ", med)
							run2 = False

						case 'e':
							med = media(conjE)
							print("A media do conjunto E é: ", med)
							run2 = False

						case 'f':
							med = media(conjF)
							print("A media do conjunto F é: ", med)
							run2 = False

						case 'i':
							med = media(conjI)
							print("A media do conjunto I é: ", med)
							run2 = False

						case _:
							print("Opção inválida!")
			case '99':
				print("Obrigado!")
				run = False
			case _:
				print("\nOpção inválida!")


# Chamada da função principal
menu()