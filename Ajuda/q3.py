def num(a,b):
    if(a%b==0):
        return 0
    else:
        p=a%b
        while(p!=0):
            b=b+1
            p=a%b
        return b
             
v1=int(input('Informe o primeiro valor: '))
v2=int(input('Informe o segundo número: '))
print(num(v1,v2))