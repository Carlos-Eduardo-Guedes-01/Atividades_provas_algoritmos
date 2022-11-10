log=[]
prog=[]
print('Informe a matrícula dos alunos que cursam Lógica: ')
i=0
v=[]
while(i<15):
    log.append(int(input()))
    i+=1
c=0
i=0
print('Informe a matrícula dos alunos que cursam Lingusgem de programação: ')
while(i<10):
    prog.append(int(input()))
    if(log[i]==prog[i]):
        print('Faz parte dos dois cursos: ',prog[i])
        
    i+=1
