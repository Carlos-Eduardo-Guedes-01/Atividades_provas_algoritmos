preco=float(input('Informe o preço do produto: '))
if(preco<=50):
    nv_preco=preco+preco*5/100
    print('Novo preço: {:.2f}'.format(nv_preco))
    if(nv_preco<=80):
        print('BARATO')
    elif(nv_preco>80 and nv_preco<=120):
        print('NORMAL')
    elif(nv_preco>120 and nv_preco<=200):
        print('CARO')
    elif(nv_preco>200):
        print('MUITO CARO')
elif(preco>50 and preco<=100):
    nv_preco=preco+preco*10/100
    print('Novo preço: {:.2f}'.format(nv_preco))
    if(nv_preco<=80):
        print('BARATO')
    elif(nv_preco>80 and nv_preco<=120):
        print('NORMAL')
    elif(nv_preco>120 and nv_preco<=200):
        print('CARO')
    elif(nv_preco>200):
        print('MUITO CARO')
elif(preco>100):
    nv_preco=preco+preco*15/100
    print('Novo preço: {:.2f}'.format(nv_preco))
    if(nv_preco<=80):
        print('BARATO')
    elif(nv_preco>80 and nv_preco<=120):
        print('NORMAL')
    elif(nv_preco>120 and nv_preco<=200):
        print('CARO')
    elif(nv_preco>200):
        print('MUITO CARO')

        
