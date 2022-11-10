quant = 0
soma_idd = 0
media_idd = 0
while (True):
    idade = int (input('Digite sua idade: '))
    altura = float (input('Digite sua altura: '))
    if (idade <= 50):
        quant += 1
        soma_idd += altura
        media_idd = soma_idd / quant
    if (idade <= 0):
        break
print('A média de altura das pessoas que idade menos de 50 anos é: ',media_idd)
