idade=int(input('Informe sua idade: '))
peso=float(input('Informe seu peso: '))
if(idade<20):
    if(peso<=60):
        print('Grupo: 9')
    elif(peso>60 and peso<=90):
        print('Grupo: 6')
    elif(peso>90):
        print('Grupo: 3')
elif(idade>=20 and idade<=50):
    if(peso<=60):
        print('Grupo: 8')
    elif(peso>60 and peso<=90):
        print('Grupo: 5')
    elif(peso>90):
        print('Grupo: 2')
elif(idade>50):
    if(peso<=60):
        print('Grupo: 7')
    elif(peso>60 and peso<=90):
        print('Grupo: 4')
    elif(peso>90):
        print('Grupo: 1')
    
