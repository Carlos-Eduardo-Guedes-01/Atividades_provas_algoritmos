media_i_3 = 0
escolha_3 = 0
soma_idade_3 = 0
escolha_1 = 0
escolha_2 = 0
media_i_2 = 0
soma_i_2 = 0
for i in range(1,16):
  idade=int(input('Digite sua idade: '))
  escolha=int(input('''O Que você achou do filme:
  3 - Ótimo
  2 - Bom
  1 - Regular
  Digite sua escolha: '''))
  if (escolha==3):
    escolha_3+=1
    soma_idade_3+=idade

  elif (escolha==1):
    escolha_1+=1
  elif (escolha==2):
    escolha_2+=1
    soma_i_2+=escolha_2
media_i_2=soma_i_2/15
media_i_3=soma_i_3/escolha_3
print('A media das idades das pessoas que responderam Ótimo: ',media_i_3)
print('A quantidade de pessoas que responderam Regular: ',escolha_1)
print('A porcentagem de todas as pessoas que responderam Bom: ',media_i_2)
