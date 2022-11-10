sal=float(input('Informe o valor do seu salário: '))
if(sal<500):
    print('Você tem direito ao acréscimo do salário!')
    sal_f=sal+sal*30/100
    print('Após o acréscimo do salário, ele ficou {:.2f}'.format(sal_f))
else:
    print('Você não tem direito ao acréscimo!')
