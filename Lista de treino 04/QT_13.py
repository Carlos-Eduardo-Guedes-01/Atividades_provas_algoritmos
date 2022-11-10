nome=[]
nota=[]
media=0
soma=0
for i in range(0,8):
    nm=input('Digite o nome do {}º aluno: '.format(i+1))
    nome.append(nm)
    num=input('Digite a nota do(a) {}: '.format(nm))
    nota.append(num)
    soma+=num
    media=soma/8
print('Relatório de notas')
for i in range(0,8):
    print('{} {}'.format(nome[i],nota[i]))
print('Média da turma: {:.2f}'.format(media))
