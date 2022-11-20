valor = float(input("Informe a quantia em reais a ser convertida: "))
moeda = input("Informe para que moeda sera convertido\n(E=euro, L=Libra, D=dolar, I=Iene): ")
ok = 1

if(moeda == 'E'):
    valor = valor*6.617
elif(moeda == 'L'):
    valor = valor*6.816
elif(moeda == 'D'):
    valor = valor*5.71
elif(moeda == 'I'):
    valor = valor*3.78
else:
    ok = 0
    print("Opção inválida")

if ok: print("O valor convertido é ", valor)

