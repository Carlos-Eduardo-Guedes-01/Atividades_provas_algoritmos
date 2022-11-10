'''Faça um programa que receba três números obrigatoriamente em ordem crescente e um
quarto número que não siga essa regra. Mostre, em seguida, os quatro números em ordem
decrescente. Suponha que o usuário digitará quatro números diferentes.'''
print('Informe 3 valores em ordem crescente:')
n1=int(input('Informe o primeiro valor: '))
n2=int(input('Informe o segundo valor: '))
n3=int(input('Informe o terceiro valor: '))
print('Esse 4º valor não precisa seguir a ordem crescente.')
n4=int(input('Informe o quarto valor: '))
if(n4>n3):
    print('A ordem é ',n4,n3,n2,n1)
elif(n4==n3):
    print('A ordem é ',n4,n3,n2,n1)
if(n4>n2 and n4<n3):
    print('A ordem é ',n3,n4,n2,n1)
elif(n4==n2 or n4==n3):
    print('A ordem é ',n3,n4,n2,n1)
if(n4>n1 and n4<n2):
    print('A ordem é ',n3,n2,n4,n1)
elif(n4==n1):
    print('A ordem é ',n3,n2,n4,n1)
if(n4<n1):
    print('A ordem é ',n3,n2,n1,n4)
elif(n4==n1):
    print('A ordem é ',n3,n2,n1,n4)
