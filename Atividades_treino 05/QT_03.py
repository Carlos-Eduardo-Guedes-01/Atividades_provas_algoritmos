q1=0
q2=0
q3=0
q4=0
q5=0
for i in range(0,8):
    idade=int(input('Informe sua idade: '))
    if(idade<=15):
        q1+=1
    elif(idade>=16 and idade<=30):
        q2+=1
    elif(idade>=31 and idade<=45):
        q3+=1
    elif(idade>=46 and idade<=60):
        q4+=1
    elif(idade>60):
        q5+=1
print('Na 1ª faixa temos ', q1,' pessoas')
print('Na 2ª faixa temos ', q2,' pessoas')
print('Na 3ª faixa temos ', q3,' pessoas')
print('Na 4ª faixa temos ', q4,' pessoas')
print('Na 5ª faixa temos ', q5,' pessoas')
f1=q1+q1*8/100
f5=q5+q5*8/100
print(f1,'% de pessoas são da 1ª faixa etária.')
print(f5,'% de pessoas são da 5ª faixa etária.')
