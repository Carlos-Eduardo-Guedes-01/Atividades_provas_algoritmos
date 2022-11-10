tot_vendas=[]
perc_comi=[]
nome=[]
i=0
maior=0
menor=0
nom_maior=' '
nom_menor=' '
result=0
soma=0
while(i<10):
    nome.append(input('Informe o nome deste vendedor: '))
    tot_vendas.append(float(input('Informe o total de vendas deste vendedor: ')))
    perc_comi.append(float(input('Informe o percentual de comição deste vendedor: ')))
    i+=1
i=0
while(i<10):
    result=(perc_comi[i]*100)/tot_vendas[i]
    print('Funcionário :{}'.format(i+1))
    print('''Nome: {}
            Valor comição:{}
    
            '''.format(nome[i],result))
    soma+=tot_vendas[i]
    print('Total de vendas: ',soma)
    if(result>maior):
        maior=result
        nom=nome[i]
    if(result<menor):
        menor=result
        nom=nome[i]
    i+=1
print('''
    Nome do funcionário que receberá mais: {}
    Valor: {}
    Nome do funcionário que receberá menos: {}
    Valor{}

'''.format(nom_maior,maior,nom_menor,menor))
