mediaIdade1 = 0
mediaIdade11 = 0
mediaIdade21 = 0
mediaIdade31 = 0
totalidade1 = 0
totalidade11 = 0
totalidade21 = 0
totalidade31 = 0
idade1 = 0
idade11 = 0
idade21 = 0
idade31 = 0
s = 1
for i in range(1,11):
    idade = int (input("Digite sua idade: "))
    peso = float (input("Digite seu peso: "))
    if (idade >= 1 and idade <= 10):
        idade1 += 1
        totalidade1 = totalidade1 + peso
        mediaIdade1 = totalidade1 / idade1
    elif (idade >= 11 and idade <= 20):
        idade11 += 1
        totalidade11 = totalidade11 + peso
        mediaIdade11 = totalidade11 / idade11
    elif (idade >= 21 and idade <= 30):
        idade21 += 1
        totalidade21 = totalidade21 + peso
        mediaIdade21 = totalidade21 / idade21
    elif (idade > 31):
        idade31 += 1
        totalidade31 = totalidade31 + peso
        mediaIdade31 = totalidade31 / idade31
print('A media do peso das pessoas entre 1 e 10 anos é: ',mediaIdade1)
print('A media do peso das pessoas entre 11 e 20 anos é: ',mediaIdade11)
print('A media do peso das pessoas entre 21 e 30 anos é: ',mediaIdade21)
print('A media do peso das pessoas acima de 31 anos é: ', mediaIdade31)
