preco_f=float(input('Informe o preço de fábrica do carro: '))
if(preco_f<12000):
    valor_f=preco_f+preco_f*5/100
    print('O valor do carro é ',valor_f)
elif(preco_f>=12000 and preco_f<=25000):
    valor_f=preco_f+preco_f*10/100+preco_f*15/100
    print('O valor do carro é ',valor_f)
elif(preco_f>25000):
    valor_f=preco_f+preco_f*15/100+preco_f*20/100
    print('O valor do carro é ',valor_f)
