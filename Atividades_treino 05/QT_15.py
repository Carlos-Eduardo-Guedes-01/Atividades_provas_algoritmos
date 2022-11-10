ss = 0
n = 0
mulher_Ss = 0
homem_N = 0
med_H = 0
homem = 0
toth = 0
for i in range(1, 11):
  sx = input('''Qual seu sexo:
  F - Feminino
  M - Masculino
  Digite aqui sua resposta: ''')
  prod = input('''Você gostou do produto:
  S - Sim
  N - Não
  Digite aqui sua resposta: ''')
  
  if (prod == 's'):
    ss+= 1
  elif (prod == 'n'):
    n += 1
  if (sx == 'f' and prod == 's'):
    mulher_Ss += 1
  if (sx == 'm'):
    homem += 1
    if (prod == 'n'):
      homem_N += 1
      toth += homem
      med_H = homem / homem_N
  print('Quantidade de pessoas que responderam sim: ', ss)
  print('Quantidade de pessoas que responderam não: ', n)
  print('Quantidade de mulheres que responderam sim: ', mulher_Ss)
  print('Media dos homens que responderam não: ',med_H)
