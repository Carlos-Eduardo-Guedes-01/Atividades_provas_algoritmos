n1=float(input('Informe o 1º valor: '))
n2=float(input('Informe o 2º valor: '))
n3=float(input('Informe o 3º valor: '))
if(n1>n2 and n1>n3):
    print('O primeiro valor é maior!')
    print('Sendo esse valor igual a ',n1)
elif(n2>n1 and n2>n3):
    print('O segundo valor é o maior!')
    print('Sendo esse valor igual a ',n2)
elif(n3>n1 and n3>n2):
    print('O terceiro valor é o maior!')
    print('Sendo esse valor igual a ',n3)
else:
    print('Os 3 valores são iguais!')
