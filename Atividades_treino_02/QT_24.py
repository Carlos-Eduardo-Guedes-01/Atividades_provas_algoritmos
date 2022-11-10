preco=float(input('informe o preço do produto'))
print('1-Limpeza;')
print('2-Alimentação;')
print('3-Vestuário;')
cat=int(input('Digite o número correspondente a uma categoria: '))
print('R-produtos que necessitam de refrigeração;')
print('N-produtos que não necessitam de refrigeração;')
situ=input('Digite a letra correspondente a uma das letras acima: ')
valor=0
if(preco<=25):
    if(cat==1):
        if(situ=='R'):
            valor_f=preco+(preco*5/100)-(preco*5/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
        else:
            valor_f=preco+(preco*5/100)-(preco*8/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
    elif(cat==2):
        if(situ=='R'):
            valor_f=preco+(preco*8/100)-(preco*5/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
        else:
            valor_f=preco+(preco*8/100)-(preco*8/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
    elif(cat==3):
        if(situ=='R'):
            valor_f=preco+(preco*5/100)-(preco*5/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
        else:
            valor_f=preco+(preco*10/100)-(preco*8/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
if(preco>25):
    if(cat==1):
        if(situ=='R'):
            valor_f=preco+(preco*12/100)-(preco*5/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
        else:
            valor_f=preco+(preco*12/100)-(preco*8/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
    elif(cat==2):
        if(situ=='R'):
            valor_f=preco+(preco*15/100)-(preco*5/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
        else:
            valor_f=preco+(preco*15/100)-(preco*8/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
    elif(cat==3):
        if(situ=='R'):
            valor_f=preco+(preco*18/100)-(preco*5/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
        else:
            valor_f=preco+(preco*18/100)-(preco*8/100)
            print('O novo valor será %.2f'%valor_f)
            if(valor_f<=50):
                print('Barato')
            elif(valor_f<50 and valor_f<120):
                print('Normal')
            else:
                print('Caro')
