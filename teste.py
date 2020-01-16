


ler = open('banco\estoquepizza.txt', 'r')
cont = 0
for linha1 in ler:
    cont = cont + 1 
ler.seek(0)
cont = cont // 4

for linha in range(0, cont):  
    print('SABOR:',ler.readline().rstrip())
    print('CÓDIGO:',ler.readline().rstrip())
    print('QUANTIDADE:',ler.readline().rstrip())
    print('PREÇO:',ler.readline().rstrip())
    print('--------------------------------')

ler.close()
