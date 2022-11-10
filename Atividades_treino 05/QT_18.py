media_sal = 0
soma_sal = 0
sal = 0
quant = 0
menor_i = 0
maior_i =0
mulher_pb = 0
menor_sal = 0
maoir_sal = 0
sexos = 0
idades = 0
idade = int (input('Digite a idade do participante: '))
while (idade > 0):
    sx = input(''' Sexo:
    F - Feminino
    M - Masculino
    Qual o sexo: ''')
    salario = float (input('Qual o salario do participante: '))
    print('________________________________________________________')
    sal += 1
    soma_sal += salario
    media_sal = soma_sal / sal
    quant += 1
    if (quant == 1):
        maior_i = menor_i = idade
    else:
        if (idade > maior_i ):
            maior_i = idade
        if (idade < menor_i):
            menor_i = idade
        if ( sx == 'f' and salario < 200):
            mulher_pb += 1
        if (quant == 1):
            maior_sal = menor_sal = salario
        else:
            if (salario > maior_sal):
                maior_sal = salario
            if (salario < menor_sal):
                menor_sal = salario
            if ( salario == menor_sal):
                sexos = sx
                idades = idade
    idade = int (input('Digite a idade do participante: '))
print('A media do salário do grupo é : ', media_sal)
print('A maior idade do grupo é: ',maiori_,'A menor idade do grupo é: ', menor_i)
print('A quantidade de mulheres que recebem salário abaixo de R$ 200,00 é: ', mulher_pb)
print('O sexo da pessoa que recebeu o menor salario é ', sexos,'e a idade é: ' ,idades)
