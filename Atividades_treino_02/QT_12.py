sal_b=float(input('Informe o valor do seu salário bruto: '))
if(sal_b<=350):
    sal_f=sal_b+100-sal_b*7/100
    print('O valor do a receber deste funcionário é ',sal_f)
elif(sal_b>350 and sal_b<600):
    sal_f=sal_b-sal_b*7/100+75
    print('O valor do a receber deste funcionário é ',sal_f)
elif(sal_b>=600 and sal_b<=900):
    sal_f=sal_b-sal_b*7/100+50
    print('O valor do a receber deste funcionário é ',sal_f)
elif(sal_b>900):
    sal_f=sal_b-sal_b*7/100+35
    print('O valor do a receber deste funcionário é ',sal_f)
