litros = float(input("Informe a quantia em litros: "))
tipo = input("Informe o tipo de combustível:\nA=alcool, G=Gasolina, D=Diesel: ")
ok = 1

if(tipo == 'A'): 
    valor = litros*4.805
elif(tipo == 'D'): 
    valor = litros*5.953
elif(tipo == 'G'):
    valor = litros*6.565
else:
    print("Tipo inválido")
    ok = 0

if ok: print("O valor do combustível será R$", valor)

