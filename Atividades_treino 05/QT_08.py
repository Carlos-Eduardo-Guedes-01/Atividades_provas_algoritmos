quant_idade_maior50=0
media_idade_1_meio=0
quant_pessoas_1_meio=0
pessoas_olhos_azuis=0
porcent_olhos_azuis=0
quant_pessoas_ruivas=0
for i in range(1,7):
    idade=int(input('Informe a idade: '))
    peso=float(input('Informe o peso: '))
    altura=float(input('Informe a altura: '))
    cor_olhos=input('''Informe a cor dos olhos:
                    A-Azul
                    P-Preto
                    V-Verde
                    C-Castanho
                    ''')
    cor_cabelos=input('''Informe a cor dos olhos:
                    P-Preto
                    C-Castanho
                    L-Loiro
                    R-Ruivo
                    ''')
    if(idade>50 and peso<60):
        quant_idade_maior50+=1
    if(altura<1.5):
        quant_pessoas_1_meio+=1
        soma=soma+idade
        media_idade_1_meio=soma/quant_pessoas_1_meio
    if(cor_olhos=='A' or cor_olhos=='a'):
        pessoas_olhos_azuis+=1
        porcent_olhos_azuis=(100*pessoas_olhos_azuis)/6
    if((cor_cabelos=='R' or cor_cabelos=='r') and (cor_olhos!='A' or cor_olhos!='a')):
        pessoas_ruivas+=1
print('Pesosas com idade superior a 50 anos e peso superior a 60Kg: ',quant_idade_maior50)
print('Média das idades das pessoas com altura inferior a 1,50M: {:.2f}'.format(media_idade_1_meio))
print('Porcentagem de pessoas com olhos azuis: {:.2f}'.format(porcent_olhos_azuis))
print('Pesosas ruivas mas não possuem olhos azuis: ',pessoas_ruivas)
