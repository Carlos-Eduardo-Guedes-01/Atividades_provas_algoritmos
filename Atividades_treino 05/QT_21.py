vt1=0
vt2=0
vt3=0
vt4=0
vt5=0
vt6=0
pcb=0
pcn=0
while (True):
    voto=int(input(''' Vote:
    Candidato - 1
    Candidato - 2
    Candidato - 3
    Candidato - 4
    Voto nulo - 5
    Voto em branco - 6
    Digit sua escolha: '''))
    if (voto==1):
        vt1+=1
    elif (voto==2):
        vt2+=1
    elif (voto==3):
        vt3+=1
    elif (voto==4):
        vt4+=1
    elif (voto == 5):
        vt5 += 1
        pcn = (100 * vt5) / 6
    elif (voto == 6):
        vt6 += 1
        pcb = (100 * vt6) / 6
    if (voto <= 0):
        print('Numero de candidato errado!')
        break
print('''Quantidade de votos:
Candidato 1 foram: {}
Candidato 2 foram: {}
Candidato 3 foram: {}
Candidato 4 foram: {}
votos nulos foram: {}
porcentagem dos votos em branco foram: {:.2f} 
porcentagem dos votos nulos foram: {:.2f}  '''.format(vt1,vt2,vt3,vt4,pcb,pcn)
