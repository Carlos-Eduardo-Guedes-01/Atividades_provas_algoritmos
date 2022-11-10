saldo_m=float(input('Informe o saldo médio anual: '))
if(saldo_m>400):
    credito=saldo_m*30/100
    print('Seu crédito é ', credito)
elif(saldo_m<=400 and saldo_m>300):
    credito=saldo_m*25/100
    print('Seu crédito é ',credito)
elif(saldo_m<=300 and saldo_m>200):
    credito=saldo_m*20/100
    print('Seu crédito é ',credito)
else:
    credito=saldo_m*10/100
    print('Seu crédito é ',credito)
