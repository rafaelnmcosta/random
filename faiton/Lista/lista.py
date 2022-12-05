# Escreva o seu código aqui :-)
tca=int(input('digite o tamanho do do conjunto ca:'))
ca=[]
c=0
while c<tca:
    a=int(input('digite um numero para o conjunto:'))
    if ca.count(a)==0:
        ca.append(a)
        c=c+1
    else:
        print('esse numero ja existe no conjunto')
print('comjunto a:',ca)
tcb=int(input('digite o tamanho do do conjunto cb:'))
cb=[]
c=0
while c<tcb:
    b=int(input('digite um numero para o conjunto:'))
    if cb.count(b)==0:
        cb.append(b)
        c=c+1
    else:
        print('esse numero ja existe no conjunto')
print('conjunto b:',cb)
g = 0;
while g != 99:
    #menu
    print('1- conjunto união')
    print('2- conjunto intersecção')
    print('3- conjunto a-b')
    print('4- conjunto b-a')
    print('5- se a e subconjunto de b')
    print('6- se b e subconjunto de a')
    print('7- a e b sao conjuntos identico')
    print('8- a e b sao conjuntos disjunto')
    print('9- amplitude do conjunto')
    print('10- produto escalar quando possivel')
    print ('11-a e b em ordem')
    print ('12- media aritimetica')
    print ('99 - sair')
    g=int(input('escolha uma opição.'))

    if g==1:
        U=set(ca).union(set(cb))
        print('conjunto união:',list(U))
    elif g==2:
        '''D=set(ca).intersection(set(cb))'''
        D=[]
        for q in ca:
            for w in cb:
                if q==w:
                    D.append(q)
        print('conjunto intersecção:',list(D))
    elif g==3:
        E=set(ca)-set(cb)
        print(list(E))
    elif g==4:
        F=set(cb)-set(ca)
        print(list(F))
    elif g==5:
        if set(ca)==set(cb):
            print('a é subconjunto de b')
        for x in ca:
            if x in cb==ca:
                print('a é subconjunto de b')
            else:
                print('a nao é subconjunto de b')
    elif g==6:
        x=0
        while x <len(ca):
            q=ca[x]
            if cb.count(q)==0:
                x=len(ca) + 10;
            x=x+1
        if x == len(ca):
            print(' a é subconjunto de b')

    elif g==7:
        d=[]
        x=set(ca)-set(cb)
        d.append(x)
        c=set(cb)-set(ca)
        d.append(c)
        if d==[set(),set()]:
            print('os conjuntos são iguais')
        else:
            print(' os conjuntos sao diferentes')
    elif g==8:
        D=[]
        for q in ca:
            for w in cb:
                if q==w:
                    D.append(q)
        if D==[]:
            print('esses cojuntos sao dijuntos')
    elif g==9:
        ca.sort()
        cb.sort()
        ma=tca-1
        amplitude_a=ca[ma]-ca[0]
        print(amplitude_a)
        mb=tcb-1
        amplitude_=cb[mb]-cb[0]
        print(amplitude_b)
    elif g==10:
        q=float(0)
        if len(ca)==len(cb):
            for i in range(len(ca)):
                q=q+ca[i]*cb[i]
                print('o peiduto escalar é',q)
        else:
            print('nao e possivel calcular')


    elif g==11:
        U=set(ca).union(set(cb))

        print(list(U))
    elif g==12:
        U=set(ca).union(set(cb))
        soma=0
        for i in U:
            soma=soma +i
        media=soma/len(U)
        print(media)

