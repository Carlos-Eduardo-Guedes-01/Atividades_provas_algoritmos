v=[]
i=0
while(i<7):
    v.append(int(input('Informe o elemento {}: '.format(i))))
    i+=1
i=0
print('multiplos de 2')
while(i<7):
    if(v[i]%2==0):
        print(v[i])
    i+=1
print('multiplos de 3')
i=0
while(i<7):
    if(v[i]%3==0):
        print(v[i])
    i+=1
print('multiplos de 2 e 3')
i=0
while(i<7):
    if(v[i]%2==0 and v[i]%3==0):
        print(v[i])
    i+=1
