vet=[]
i=0
quant=0
soma=0
while(i<10):
    vet.append(float(input()))
    if(vet[i]>=0):
        soma+=vet[i]
    else:
        quant+=1
    i+=1
print('''
        Soma dos posistivos: {}
        Quantidade dos negativos: {}
'''.format(soma,quant))
