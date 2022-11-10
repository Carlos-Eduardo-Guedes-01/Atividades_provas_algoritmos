media_idades=0
maoires_90_kg=0
porcent_10_30=0
quant_10_30=0
for i in range(1,11):
    idade=int(input('Informe a idade: '))
    peso=float(input('Informe o peso: '))
    altura=float(input('Informe a altura: '))
    soma=soma+idade
    media_idades=soma/10
    if(peso>90 and altura<1.50):
        maiores_90_kg+=1
    if((idade>=10 and idade<=30) and altura>1.90):
        quant_10_30+=1
        porcent_10_30=(100*quant_10_30)/10
print('A média das idades: {:.2f}'.format(media_idades))
print('Quantidade de pessoas com peso superior a 90Kg e altura inferior a 1,50m: ',maiores_90_kg)
print('Porcentagem  de pessoas com idade entre 10 e 30 anos maiores de 1,90m: {:.2f}'.format(porcent_10_30))
