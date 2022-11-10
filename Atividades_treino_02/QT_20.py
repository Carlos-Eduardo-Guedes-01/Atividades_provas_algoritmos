idade=int(input('Informe sua idade: '))
if(idade>=5 and idade<=7):
    print('Infantil')
elif(idade>=8 and idade<=10):
    print('Juvenil')
elif(idade>=11 and idade<=15):
    print('Adolescente')
elif(idade>=16 and idade<=30):
    print('Adulto')
elif(idade>30):
    print('Sênior')
else:
    print('Muito jovem para aprender a nadar!')
    
