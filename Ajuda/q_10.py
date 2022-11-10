def sequencia(n):
    s=0
    cont=1
    while(cont<=n):
        s=s+1/cont
        cont+=1
    return s
n=int(input('Informe o limite da sequência: '))
print(sequencia(n))