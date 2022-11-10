cod=int(input('Informe o código do produto: '))
qtd=int(input('Informe a quantidade de produtos'))
if(cod>=1 and cod<=10):
    valor=qtd*10
    if(valor<=250):
        desconto=valor*5/100
        valor_f=valor-desconto
        print('Valor intário: R$10.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>250 and valor<=500):
        desconto=valor*10/100
        valor_f=valor-desconto
        print('Valor intário: R$10.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>500):
        desconto=valor*15/100
        valor_f=valor-desconto
        print('Valor intário: R$10.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
elif(cod>=11 and cod<=20):
    valor=qtd*15
    if(valor<=250):
        desconto=valor*5/100
        valor_f=valor-desconto
        print('Valor intário: R$15.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>250 and valor<=500):
        desconto=valor*10/100
        valor_f=valor-desconto
        print('Valor intário: R$15.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>500):
        desconto=valor*15/100
        valor_f=valor-desconto
        print('Valor intário: R$15.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)    
elif(cod>=21 and cod<=30):
    valor=qtd*20
    if(valor<=250):
        desconto=valor*5/100
        valor_f=valor-desconto
        print('Valor intário: R$20.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>250 and valor<=500):
        desconto=valor*10/100
        valor_f=valor-desconto
        print('Valor intário: R$20.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>500):
        desconto=valor*15/100
        valor_f=valor-desconto
        print('Valor intário: R$20.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
elif(cod>=31 and cod<=40):
    valor=qtd*30
    if(valor<=250):
        desconto=valor*5/100
        valor_f=valor-desconto
        print('Valor intário: R$30.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>250 and valor<=500):
        desconto=valor*10/100
        valor_f=valor-desconto
        print('Valor intário: R$30.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
    elif(valor>500):
        desconto=valor*15/100
        valor_f=valor-desconto
        print('Valor intário: R$30.00')
        print('Preço total: %.2f'%valor)
        print('Valor do desconto: %.2f'%desconto)
        print('Preço com desconto: %.2f'%valor_f)
