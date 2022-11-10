Rede = 0
Juros = 0
valort=0
jurosd=0
while (True):
    cod = int (input('''Escolha o código:
    1. Poupança
    2. Poupança plus
    3. Fundos de renda fixa
    Digite aqui: '''))
    inv = float(input('Informe o valor a ser investido: '))
    if (cod == 1):
        Por = Valor * 0.015
        Valorf = por + inv
        print('O rendimento mensal: R$ ', Valorf)
    elif (cod == 2):
        Por2 = Valor * 0.02
        Valorf2 = Por2 + inv
        print('O rendimento mensal: R$ ', Valorf2)
    elif (cod == 3):
        Por3 = Valor * 0.04
        Valorf3 = Por3 + inv
        print('O rendimento mensal: R$ ', Valorf3)
        Rede += 1
        Val = Valorf + Valorf1 + Valorf2
        Valort = rede + Val
        Juros += 1
        Jurosf = Por + Por1 + Por2
        Jurosd = Jurosf + Juros
    if (cod <= 0):
        break
print('O valor total dos investimentos foi R$ ', Valort)
print('O total de juros pagos foi R$ ', Jurosd)
