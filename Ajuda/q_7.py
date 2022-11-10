def semfim():
    quant=0
    soma=0
    num=float(input('Informe o {:.1f} valor: '.format(quant)))
    while(num!=0):
        quant+=1
        soma+=num
        num=float(input('Informe o {:.1f} valor: '.format(quant)))
    return soma/quant
print(semfim())