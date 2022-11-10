sal=float(input('Informe o valor do salário: '))
if(sal<=300):
    sal_f=sal+sal*35/100
    print('O valor do salário reajustado é %.2f'%sal_f)
else:
    sal_f=sal+sal*15/100
    print('O valor do salário reajustado é %.2f'%sal_f)
