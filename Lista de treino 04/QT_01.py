vet=[]
i=0
c=[]
quant_par=0
quant_impar=0
while(i<6):
    vet.append(int(input('Informe o elemento {}: '.format(i))))
    i+=1
i=0
print('-'*(90))
while(i<6):
    if(vet[i]%2==0):
        quant_par+=1
        print('{} é par'.format(vet[i]))
    else:
        quant_impar+=1
        print('{} é ímpar'.format(vet[i]))
    i+=1
print('Quantidade par: ',quant_par)
print('Quantidade ímpar: ',quant_impar)
