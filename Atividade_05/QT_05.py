'''Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a
R$ 500,00. Faça um programa que receba o salário do funcionário e mostre o valor do
salário reajustado ou uma mensagem, caso ele não tenha direito ao aumento.'''
sal=float(input('Informe o valor do seu salário: '))
if(sal<500):
    print('Você tem direito ao acréscimo do salário!')
    sal_f=sal+sal*30/100
    print('Após o acréscimo do salário, ele ficou ',sal_f)
else:
    print('Você não tem direito ao acréscimo!')
