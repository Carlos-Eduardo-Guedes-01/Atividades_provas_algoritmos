cod=[]
quant=[]
dados=[]
est=0

for i in range(0,10):
    cod.append(int(input('Informe o codigo de produto: ')))
    quant.append(int(input('Informe a quantidade desse produto: '))
cod_cli=int(input('Informe o código do cliente: '))
quantid=int(input('Informe a quantidade de produtos com esse código: '))
c=0
while(cod_cli!=0):
    while (c<10):
        if(cod[c]==cod_cli):
            if(quant[c]>quantid):
                quant[c]=quant[c]-quantid
                print('Pedido atendido. Obrigado volte sempre!')
            else:
                print('Não temos estoque suficiente dessa mercadoria.')
        else:
            print('Código inexistente!')
    cod_cli=int(input('Informe o código do cliente: '))
    quantid=int(input('Informe a quantidade de produtos com esse código: '))
i=0
print('Estoque atualizado: ')
while(i<10):
    print('''Código: {} 
	     Estoque:{}
    '''.format(cod[i],quant[i]))
