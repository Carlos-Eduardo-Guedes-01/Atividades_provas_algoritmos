quant = 0
maior = 0
v = int(input('Informe número: '))
menor=v
while (True):
    v = int(input('Informe número: '))
    if(v==0):
        break
    if (v > maior):
        maior=v
    if (v < menor):
        menor = v
    v = int(input('Informe número: '))
print('O maior número é: ', maior, 'e o menor é: ', menor)
