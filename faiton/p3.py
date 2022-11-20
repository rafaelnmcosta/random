nome_posto = input("Informe o nome do posto: ")
consumo_anual  = int(input("Informe o consumo anual em litros: "))

if(consumo_anual <= 70000):
    preco = round(5.35+(5.35*0.25), 2)
else:
    preco = round(5.35+(5.35*0.15), 2)

print("O preço para o posto", nome_posto, "será R$", preco)

