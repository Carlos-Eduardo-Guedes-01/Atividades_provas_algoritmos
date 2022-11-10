def fat(num):
    res=1
    while(num>1):
        res=res*num
        num-=1
    return res
num=int(input('Digite o numero fatorial: '))
print(num,"!=",fat(num))
