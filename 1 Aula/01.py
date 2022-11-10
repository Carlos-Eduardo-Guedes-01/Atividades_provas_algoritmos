vet=[]
i=0
0,1,2,3,4,5,6
while(i<7):
    vet.append(int(input('Informe o número: ')))
    i=i+1
i=0
print('Multiplos de 2:')
while(i<7):
    if(vet[i]%2==0):
        print(vet[i])
    i=i+1
i=0
print('Multiplos de 3:')
while(i<7):
    if(vet[i]%3==0):
        print(vet[i])
    i=i+1
i=0
print('Multiplos de 2 e de 3:')
while(i<7):
    if(vet[i]%2==0 and vet[i]%3==0):
        print(vet[i])
    i=i+1
