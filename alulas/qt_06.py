def peso(alt,sexo):
    peso_i=0
    if(sexo=='M' or sexo=='m'):
        peso_i=72.7*alt-58
    elif(sexo=='F' or sexo=='f'):
        peso_i=62.1*alt-44.7
    return peso_i
alt=float(input('Informe a altura: '))
sexo=input('informe o sexo da pessoa: ')
peso_ideal=peso(alt,sexo)
print('Peso ideal: ',peso_ideal)
    
