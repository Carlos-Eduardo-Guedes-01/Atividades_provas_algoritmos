'''#include<stdio.h> 
#include<conio.h> 
#include<math.h> 

main() { 
   int i, j, k, sm=0, n[10], p=0, pr, r; 
   for(i=0; i<10; i++) { 
      printf("Digite o %dº número: ", i+1); 
      scanf("%d",&n[i]); 
   } 
   for(j=0;j<10;j++) { 
      if(n[j]%2 == 0) { 
         sm += n[j]; 
      } 
      pr = 0; 
      for (k=2; k<n[j]; k++) { 
         if (n[j]%k == 0) 
            pr++; 
      } 
      if(pr == 0) { 
         p += n[j]; 
      } 
   } 
   printf("A soma dos numeros pares e %i", sm); 
   printf("A soma dos numeros primos e %i", p); 
   getch(); '''
soma_par=0
soma_primo=0
for i in range(1,11):
    valor=float(input('Informe o número: '))
    if(valor%2==0):
        soma_par+=valor
    c=2
##    quant=0
    while(c<=valor):    
        if(valor%c==0):
            quant+=1
        c+=1
    if(quant==2):
        soma_primo=soma_primo+valor
print('A quantidade de números pares é: ',soma_par)
print('A quantidade de números primos é: ',soma_primo)
