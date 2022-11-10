def p_ideal(altura,sexo):
    peso_ideal=0
    if((sexo=="m") or (sexo=="M")):
        peso_ideal=72.7*altura-58
        return peso_ideal
    elif((sexo=="f") or (sexo=="F")):
        peso_ideal=62.1*altura-44.7
        return peso_ideal
sexo=input('Informe o sexo(M ou F): ')
altura=float(input('Informe a altura: '))
peso=p_ideal(altura,sexo)
print("Seu peso ideal é: {:.2f}".format(peso))