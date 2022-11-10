print('Informe um dos tipos de investimentos abaixo!')
print('1.Polpança')
print('2.Fundos de renda fixa')
tipo=int(input('TIPO: '))
valor=float(input('Informe o valor que desja investir: '))
if(tipo==1):
    valor_r=valor+valor*3/100
    print('O novo valor é %.2f'%valor_r)
elif(tipo==2):
    valor_r=valor+valor*4/100
    print('O novo valor é %.2f'%valor_r)
else:
    print('Tipo inválido!')
