nome=[]
media=[]
maior=0
nome_maior=' '
nome_menor=' '
i=0
menor=10
while(i<7):
    nome.append(input('Informe o nome: '))
    media.append(float(input('Informe a média do aluno: ')))
    if(media[i]>maior):
        maior=media[i]
        nome_maior=nome[i]
    elif(media[i]<menor):
        menor=media[i]
        nome_menor=nome[i]
    i+=1
print('''Aluno com maior média: {}
        Média: {}
        Aluno com menor média: {}
        Média: {}
'''.format(nome_maior,maior,nome_menor,menor))
i=0
while(i<7):
    if(media[i]<7):
        exame_f=10-media[i]
        print('O aluno {} precisa tirar {} no exame final.'.format(nome[i],exame_f))
    i+=1
