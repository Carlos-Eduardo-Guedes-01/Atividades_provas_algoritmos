quant = 0
media = 0
soma_idades = 0
while (True):
    idade = int (input('Digite a idade: '))
    quant += 1
    soma_idades += idade
    media = soma_idades / quant
    if (idade == 0):
        break
print('A media das idades digitadas foi: ',media)
