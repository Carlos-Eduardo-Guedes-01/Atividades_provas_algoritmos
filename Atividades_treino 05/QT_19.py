maior_1000 = 0
menor_200 = 0
soma_lucro = 0
while (True):
    acao = str (input('A letra da acão desejada: '))
    precoC = float (input('Preço de compra: '))
    precoV = float (input('Preço de venda: '))
    lucro = precoC - precoV
    if (lucro > 1000):
        maior_1000 += 1
    elif ( lucro < 200):
        menor_200 += 1
        soma_lucro+= 1
    soma_lucro = maior_1000+menor_200
    if(acao == 'f'):
        break
print('Os valores dos lucros foram R$ ',lucro)
print('Os valores dos lucros acima de R$ 1.000,00 foram: ',maior_1000)
print('Os valores dos lucros abaixo de R$ 200,00 foram: ',menor_200)
