nome=[]
cod=[]
preco=[]
nv_preco=0
i=0
while(i<10):
    nome.append(input('Informe o nome: '))
    cod.append(int(input('Informe o código do produto: ')))
    preco.append(float(input('Informe o preço do produto: ')))
i=0
print('-'*(90))
while(i<10):
    if(cod[i]%2==0 or preco[i]>1000):
        print('''
            Nome: {}
            Código: {}
            Preço Antes do aumento: {:.2f}
            '''.format(nome[i],cod[i],preco[i]))
        if(cod[i]%2==0 and preco[i]>1000):
            nv_preco=preco[i]+preco[i]*20/100
            print('Novo preço: R${:.2f}'.format(nv_preco))
        elif(cod[i]%2==0):
            nv_preco=preco[i]+preco[i]*15/100
            print('Novo preço: R${:.2f}'.format(nv_preco))
        elif(preco[i]>1000):
            nv_preco=preco[i]+preco[i]*10/100
            print('Novo preço: R${:.2f}'.format(nv_preco))
