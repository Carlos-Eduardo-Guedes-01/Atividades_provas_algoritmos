'''Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e
os dados necessários para executar cada operação.
Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.
Digite a opção desejada:'''
import math
print('Escolha uma opção:')
print('1. Somar dois números')
print('2. Raiz quadrada de um número')
opcao=int(input('Informe o número da opção desejada: '))
if(opcao==1):
    print('Opção escolhida foi a 1ª!')
    n1=float(input('Informe o 1º valor: '))
    n2=float(input('Informe o 2º valor: '))
    soma=n1+n2
    print('O valor da soma é ',soma)
elif(opcao==2):
    print('Opção escolhida foi a 2ª!')
    n=float(input('Informe um valor: '))
    raiz=math.pow(n,1/2)
    print('A raiz quadrada desse número é ',raiz)
else:
    print('Opção inválida!')
    
