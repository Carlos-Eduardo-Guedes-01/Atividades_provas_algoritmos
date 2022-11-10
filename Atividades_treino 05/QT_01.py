for i in range(1, 6):
  n1 = int (input("Digite o primeiro valor: "))
  n2 = int (input("Digite o segundo valor: "))
  n3 = int (input("Digite o terceiro valor: "))
  n4 = int (input("Digite o quarto valor: "))
  
  print('A ordem digitada foi: ', n1, n2, n3, n4)
  
  if (n1 < n2 < n3 < n4):
     print("A ordem crescente: ", n1, n2, n3, n4)
     print("A ordem decrescente:  ", n4, n3, n2, n1)
  elif (n1 < n2 <n4 < n3): 
     print("A ordem crescente: ",n1,n2,n4,n3)
     print("A ordem decrescente: ", n3,n4, n2, n1)
  elif (n1 < n3 < n2 <n4):
     print("A ordem crescente: ", n1, n3, n2, n4)
     print("A ordem decrescente: ", n4, n2,n3, n1)
  elif (n1 < n3 < n4 < n2): 
     print("A ordem crescente: ", n1, n3, n4, n2)
     print("A ordem decrescente: ", n2, n4, n3,n1)
  elif (n1 < n4 < n3 < n2):
     print("A ordem crescente: ", n1, n4, n3, n2)
     print("A ordem decrescente: ", n2, n3, n4, n1)
  elif (n1 < n4 < n2 < n3): 
     print("A ordem crescente: ", n1, n4, n2, n3)
     print("A ordem decrescente: ", n3, n2, n4, n1)
  
  elif (n2 < n1 < n3 < n4):
     print("A ordem crescente: ", n1, n2, n3,dn4)
     print("A ordem decrescente: ",n4, n3, n2, n1)
  elif (n2 < n1 < n4 < n3): 
     print("A ordem crescente: ", n2, n1,n4, n3)
     print("A ordem decrescente: ", n3, n4, n1,n2)
  elif (n2 < n3 < n1 < n4):
     print("A ordem crescente: ", n2, n3, n1, n4)
     print("A ordem decrescente: ", n4, n1, n3, n2)
  elif (n2 < n3 < n4 < n1): 
     print("A ordem crescente: ", n2, n3, n4, n1)
     print("A ordem decrescente: ", n1, n4, n3, n2)
  elif (n2 < n4 < n3 < n1):
     print("A ordem crescente: ", n2, n4, n3, n1)
     print("A ordem decrescente: ", n1, n3, n4, n2)
  elif (n2 < n4 < n1 < n3): 
     print("A ordem crescente: ", n2, n4, n1, n3)
     print("A ordem decrescente: ", n3, n1, n4, n2)
  elif (n3 < n2 < n1 < n4):
     print("A ordem crescente: ", n3, n2, n1, n4)
     print("A ordem decrescente: ", n4, n1, n2, n3)
  elif (n3 < n2 < n4 < n1): 
     print("A ordem crescente: ", n3, n2, n4, n1)
     print("A ordem decrescente: ", n1, n4, n2, n3)
  elif (n3 < n1 < n2 < n4):
     print("A ordem crescente: ", n3, n1, n2, n4)
     print("A ordem decrescente: ", n4, n2, n1, n3)
  elif (n3 < n1 < n4 < n2): 
     print("A ordem crescente: ", n3, n1, n4, n2)
     print("A ordem decrescente: ", n2, n4, n1, n3)
