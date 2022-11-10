v=[]
soma=0
for i in range(0,5):
    n=int(input('Digite o {}º valor: '.format(i+1)))
    v.append(n)
    soma+=n
print('{}'.format(v[0]),end=' ')
for i in range(1,5):
    print('+ {}'.format(v[i]),end=' ')
print('=',soma,end=' ')
