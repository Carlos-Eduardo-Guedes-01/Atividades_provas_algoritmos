idade_acima_50=0
idade_entre_10_20=0
total_altura_10_20=0
media_altura_10_20=0
porcentagem_pessoas=0
pessoas_peso_40=0
for i in range(1,6):
    idade=int(input('Informe a idade: '))
    altura=float(input('Informe a altura: '))
    peso=float(input('Informe o peso: '))
    if(idade>50):
        idade_acima_50+=1
    if(idade>=10 and idade<=20):
        idade_entre_10_20+=1
        total_altura_10_20+=altura
        media_altura_10_20=total_altura_10_20/idade_entre_10_20
    if(peso<40):
        pessoas_peso_40+=1
        porcentagem_pessoas=(100*pessoas_peso_40)/5
print('A quantidade de pessoas com idade superior a 50 anos: ',idade_acima_50)
print('A média de altura das pessoas com idade entre 10 e 20 anos: ',media_altura_10_20)
print('A porcentagem de pessoas com peso inferior a 40kg: {:.2f} %'.format(porcentagem_pessoas))

        
        
