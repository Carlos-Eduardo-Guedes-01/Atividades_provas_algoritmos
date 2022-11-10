sal=float(input('Informe o valor do salário: '))
if(sal<=300):
    nv_sal=sal+sal*50/100
    print('O valor do novo salário é {:.2f}'.format(nv_sal))
elif(sal>300 and sal<=500):
    nv_sal=sal+sal*40/100
    print('O valor do novo salário é {:.2f}'.format(nv_sal))
elif(sal>500 and sal<=700):
    nv_sal=sal+sal*30/100
    print('O valor do novo salário é {:.2f}'.format(nv_sal))
elif(sal>700 and sal<=800):
    nv_sal=sal+sal*20/100
    print('O valor do novo salário é {:.2f}'.format(nv_sal))
elif(sal>800 and sal<=1000):
    nv_sal=sal+sal*10/100
    print('O valor do novo salário é {:.2f}'.format(nv_sal))
elif(sal>1000):
    nv_sal=sal+sal*5/100
    print('O valor do novo salário é {:.2f}'.format(nv_sal))
