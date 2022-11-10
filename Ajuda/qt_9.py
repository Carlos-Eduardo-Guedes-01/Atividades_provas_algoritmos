from calendar import c


def divisores(num):
    soma=0
    cont=1
    while(cont<=num):
        if(num%cont==0):
            soma+=cont
        cont+=1
    return soma
num=int(input('Informe um número: '))
print(divisores(num))