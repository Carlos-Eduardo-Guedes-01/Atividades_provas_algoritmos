import math
print('a.Primeiro número elevado ao segundo.')
print('b.Raíz quadrada de cada um dos números.')
print('c.Raíz cúbica de cada um dos números.')
opcao=input('Informe a letra da opção desejada: ')
if(opcao=='a'):
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    pot=v1**v2
    print('O resultado da potência é ',pot)
elif(opcao=='b'):
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    raiz_1=v1**1/2
    raiz_2=v2**1/2
    print('O valor da raíz do 1º número é %.2f e do segundo é %.2f'%(raiz_1, raiz_2))
elif(opcao=='c'):
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    raiz_1=v1**1/3
    raiz_2=v2**1/3
    print('O valor da raíz do 1º número é %.2f e do segundo é %.2f'%(raiz_1, raiz_2)
else:
    print('Opção inválida!')
