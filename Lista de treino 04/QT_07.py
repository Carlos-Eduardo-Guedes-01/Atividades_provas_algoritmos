quant_neg=0
soma_pos=0
v=[]
i=0
while(i<10):
    v.append(float(input('Informe um número: ')))
    if(v[i]<0):
        quant_neg+=1
    else:
        soma_pos+=v[i]
    i+=1
print('''Quantidade de números negativos: {}
        Soma dos números positivos: {}
'''.format(quant_neg,soma_pos))
    
