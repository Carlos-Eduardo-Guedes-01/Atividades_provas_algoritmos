'''Faça um programa que receba dois números e execute as operações listadas a seguir,
de acordo com a escolha do usuário.

Se a opção digitada for inválida, mostre uma mensagem de erro e termine a execução do
programa. Lembre-se de que, na operação 4, o segundo número deve ser diferente de zero.'''
print('1.Média dos números digitados.')
print('2.Diferença do maior pelo menor.')
print('3.Produto entre os npumeros digitados.')
print('4.Divisão do primeiro pelo segundo.')
opcao=int(input('Informe a opção desejada: '))
if(opcao==1):
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    print('A opção escolhida foi ',opcao)
    media=(v1+v2)/2
    print('O valor da média é ',media)
elif(opcao==2):
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    print('A opção escolhida foi ',opcao)
    if(v1>v2):
        dif=v1-v2
        print('O valor da diferença é ',dif)
    if(v2>v1):
        dif=v2-v1
        print('O valor da diferença é ',dif)
    else:
        print('O valor da diferença é 0')
elif(opcao==3):
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    print('A opção escolhida foi ',opcao)
    prod=v1*v2
    print('O valor do produto foi ',prod)
elif(opcao==4):
    print('A opção escolhida foi ',opcao)
    v1=float(input('Informe um número: '))
    v2=float(input('Informe outro número: '))
    if(v2!=0):
        div=v1/v2
        print('O valor da divisão foi ',div)
    else:
        print('Divisão impossível!')
else:
    print('Erro!')
