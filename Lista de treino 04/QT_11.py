vet=[]
impar=[]
par=[]
for i in range(0,10):
    numero=int(input('Informe o {}º valor: '.format(i+1)))
    vet.append(numero)
aux_impar=0
aux_par=0
for i in range(0,10):
    if(vet[i]%2==0):
        aux_par=vet[i]
        par.append(aux_par)
    else:
        aux_impar=vet[i]
        impar.append(aux_impar)
print('Vetor par:')
print(par)
print('Vetor impar:')
print(impar)
