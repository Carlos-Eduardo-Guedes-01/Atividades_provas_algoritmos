primeiro_vetor = []
segundo_vetor = []

for i in range(1,11):
  numero = int(input('Digite um numero: '))
  primeiro_vetor.append(numero)

print(''*(40))
for i in range(1,6):
  numero = int(input('Digite um numero: '))
  segundo_vetor.append(numero)

soma_segundo_vetor = 0
for i in range(len(segundo_vetor)):
  soma_segundo_vetor = soma_segundo_vetor + segundo_vetor[i]

primeiro_vetor_rst = []
segundo_vetor_rst = []
variavel_aux = 0
for i in range(len(primeiro_vetor)):
  if(primeiro_vetor[i]%2==0):
    variavel_aux = soma_segundo_vetor+primeiro_vetor[i]
    primeiro_vetor_rst.append(variavel_aux)

  if(primeiro_vetor[i]%2!=0):
    numero = primeiro_vetor[i] 
    aux=numero
    cont = 0
    while aux >= 1:
      if(numero%aux==0):
        cont = cont + 1
      aux = aux - 1
    segundo_vetor_rst.append(cont)
      
print(primeiro_vetor)
print(segundo_vetor)
print(soma_segundo_vetor)
print(primeiro_vetor_rst)
print(segundo_vetor_rst)
