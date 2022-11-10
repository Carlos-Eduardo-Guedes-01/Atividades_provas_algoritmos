tot_v=0
tot_p=0
q_v=0
q_p=0
vt=0
prest=0
for i in range(0,15):
    cod=input('Informe o código desse produto(P ou V): ')
    preco=float(input('Informe o valor desse produto: '))
    if(cod == 'V' or cod == 'v'):
        q_v+=1
        tot_v=q_v*preco
    elif(cod=='P' or cod=='p'):
        q_p+=1
        tot_p=q_p*preco
        prest=(prest+(preco*q_p))/3
    else:
        print('Código inválido!')
vt=tot_v+tot_p
print('Valor total de compras a vista: ',tot_v)
print('Valor total de compras a prazo: ',tot_p)
print('Valor total de compras efetuadas: ',vt)
print('Valor da 1ª prestação: ',prest)
