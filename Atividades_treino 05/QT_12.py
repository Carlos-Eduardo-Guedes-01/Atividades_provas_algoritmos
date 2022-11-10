mult=0
pr = 0
for i in range(0,10):
    n=int(input('Informe um número: '))
    mult=0

    for count in range(2,n):
        if (n % count == 0):
            mult += 1

    if(mult==0):
        pr+=1
print('A quantidade de números primos é ',pr)
