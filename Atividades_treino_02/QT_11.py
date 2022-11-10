sal=float(input('Informe seu salário atual: '))
if(sal<=300):
    aumento=sal*15/100
    sal_f=sal+aumento
    print('O valor do aumento é %.2f e o valor final do salário é %.2f'%(aumento,sal_f))
elif(sal>300 and sal<600):
    aumento=sal*10/100
    sal_f=sal+aumento
    print('O valor do aumento é %.2f e o valor final do salário é %.2f'%(aumento,sal_f))
elif(sal>=600 and sal<=900):
    aumento=sal*5/100
    sal_f=sal+aumento
    print('O valor do aumento é %.2f e o valor final do salário é %.2f'%(aumento,sal_f))
elif(sal>900):
    aumento=sal*0/100
    sal_f=sal+aumento
    print('O valor do aumento é %.2f e o valor final do salário é %.2f'%(aumento,sal_f))
