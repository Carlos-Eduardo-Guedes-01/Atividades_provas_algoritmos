p4 = 0
p5 = 0
p7 = 0
p12 = 0
c12 = 0
c5 = 0
c7 = 0
c4 = 0
while (True):
    canal = int (input('''Informe o canal que está assistindo:
    Canal - 4
    Canal - 5
    Canal - 7
    Canal - 12
    Digite o numero do canal: '''))
    qp = int (input('Quantos telespectadores assistiram a esse canal? '))
    if (canal == 4):
        c4 += 1
        p4 = (100 * c4) / 4
    elif (canal == 5):
        c5 += 1
        p5 = (100 * c5) / 4
    elif (canal == 7):
        c7 += 1
        p7 = (100 * c7) / 4
    elif (canal == 12):
        c12 += 1
        p12 = (100 * c12) / 4
    else:
        print('Canal invválido!')
    if (qp == 0):
        break
print('''A porcentagem de pessoas no canal:
        Canal 4: {}
        Canal 5: {}
        Canal 7: {}
        Canal 12: {}
      '''.format(c4,c5,c7,c12
                 ))
    
