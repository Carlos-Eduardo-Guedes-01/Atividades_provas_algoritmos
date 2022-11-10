n1=float(input('Informe a 1ª nota: '))
n2=float(input('Informe a 2ª nota: '))
media=(n1+n2)/2
if(media>=0 and media<3):
    print('REPROVADO!')
elif(media>=3 and media<7):
    print('EXAME!')
elif(media>=7):
    print('APROVADO!')
else:
    print('Média inválida!')
