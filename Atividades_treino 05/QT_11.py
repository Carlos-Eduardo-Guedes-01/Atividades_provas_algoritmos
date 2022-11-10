passo=6
preco=float(input('Informe o preco do carro: '))
for i in range(6, 61, passo):
    preco_f=preco+preco*(i/2)/100
    parc=preco*(i/2)/100
    print('Com {} parcelas custam R${:.2f} '.format(i,preco_f))
    print('O valor da parcela é {:.2f}'.format(parc))
