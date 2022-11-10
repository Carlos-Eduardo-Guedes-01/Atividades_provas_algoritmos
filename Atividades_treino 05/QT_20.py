med_arit = 0
media_pond = 0
while (True):
    esc = int (input('''Menu:
    1. Média Aritmética
    2. Média Ponderada
    3. Sair
    Escolha uma das opções acima: '''))
    if (esc== 1):
        n1 = float (input('Digite a nota 1: '))
        n2 = float (input('Digite a nota 2: '))
        med_arit = (n1 + n2) / 2
        print('A média aritmética desse aluno é: %.2f '% (med_arit))
    elif (esc == 2):
        n1 = float (input('Digite a primeira nota: '))
        p1 = float (input('Digite o peso dessa nota: '))
        n2 = float (input('Digite a segunda nota: '))
        p2 = float (input('Digite o peso dessa nota: '))
        n3 = float (input('Digite a terceira nota: '))
        p3 = float (input('Digite o peso dessa nota: '))
        media_pond = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / 3
        print('A media ponderada desse aluno foi: %.2f ' %(media_pond))
    if (esc == 3):
        break

