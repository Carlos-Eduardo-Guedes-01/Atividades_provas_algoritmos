preco=float(input('Informe o valor do preço: '))
if(preco<=30):
    print('Não possui desconto!')
    print('O valor do preço é %.2f'% preco)
elif(preco>30 and preco<=100):
    nv_preco=preco-preco*10/100
    print('O valor do preço é %.2f'% nv_preco)
elif(preco>100):
    nv_preco=preco-preco*15/100
    print('O valor do preço é %.2f'% nv_preco)
