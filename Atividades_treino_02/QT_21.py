preco=float(input('Informe preço do produto: '))
cod=int(input('Informe o código de origem do produto: '))
if(cod==1):
    print('Sul')
elif(cod==2):
    print('Norte')
elif(cod==3):
    print('Leste')
elif(cod==4):
    print('Oeste')
elif(cod==5 or cod==6):
    print('Nordeste')
elif(cod>=7 and cod<=9):
    print('Sudeste')
elif(cod>=10 and cod<=20):
    print('Centro-oeste')
elif(cod>=21 and cod<=30):
    print('Noroeste')
