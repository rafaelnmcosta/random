valor = float(input("Informe o valor do produto: "))
cod = int(input("Informe o código da condição de pagamento: "))
ok = 1
if(cod == 1): 
    valorpgt = valor-(valor*0.1)
elif(cod == 2): 
    valorpgt = valor-(valor*0.05)
elif(cod == 3): 
    valorpgt = valor
elif(cod == 4): 
    valorpgt = valor+(valor*0.1)
else:
    print("Código inválido")
    ok = 0

if ok: print("O valor na condição de pagamento", cod, "será R$", valorpgt)
