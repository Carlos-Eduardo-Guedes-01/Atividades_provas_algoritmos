horas_extras=float(input('Informe o número de horas extras: '))
horas_flt=float(input('Informe o número de horas faltadas: '))
H=horas_extras-(2/3*horas_flt)
minutos=H*60
if(minutos>=2400):
    print('Seu prêmio é R$500')
elif(minutos>1800 and minutos<2400):
    print('Seu prêmio é R$400')
elif(minutos>=1200 and minutos<1800):
    print('Seu prêmio é R$300')
elif(minutos>=600 and minutos<1200):
    print('Seu prêmio é R$200')
elif(minutos<600):
    print('Seu prêmio é R$100')
