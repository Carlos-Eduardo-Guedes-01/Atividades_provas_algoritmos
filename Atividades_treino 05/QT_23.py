while (True):
    opcao = int (input(''' Menu:
    1 - Novo salário
    2 - Férias
    3 - Décimo terceiro
    4 - Sair
    Escolha desejada: '''))
    if (opcao ==1):
        sal = float (input('Informe o salário: '))
        if (sal < 210):
            acresc = sal * 0.15
            salf = sal + acresc
            print('Salário final: R$ {:.2f}'.format(salf))
        elif (sal >= 210 and sal <= 600):
            acresc1 = sal * 0.10
            salf1 = sal + acresc1
            print('Salário final: R$ {:.2f}'.format(salf1))
        else:
            acresc2 = sal * 0.05
            salf2 = acresc2 + sal
            print('Salário final: {:.2f}'.format(salf2))
    if (opcao == 2):
        sal = float (input('Informe o salário: '))
        acresc3 = sal * 1/3
        salf = acresc3 + sal
        print( 'Seu salário diranteas férias: R${:.2f}'.format(salf))
    if (opcao == 3):
        sal = float (input('Informe o salário: '))
        meses = int (input('Quantos meses de trabalho: '))
        dec = (sal * meses) / 12
        print('Décimo terceiro: R$ {:.2f}'.format(dec))
    if (opcao ==4):
        break
    elif(opcao>4 or opcao<1):
        print('Opção inválida!')
