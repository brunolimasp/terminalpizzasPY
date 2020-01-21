

'''
ler = open('banco\estoquepizza.txt', 'r')
cont = 0
for linha1 in ler:
    cont = cont + 1 
ler.seek(0)
cont = cont // 4

for linha in range(0, cont):  
    print('SABOR        |','CÓDIGO       |','QUANTIDADE       |','PREÇO        |')
    print(ler.readline().rstrip(), end="            ")
    print(ler.readline().rstrip(), end="            ")
    print(ler.readline().rstrip(), end="            ")
    print(ler.readline().rstrip())
    print('---------------------------------------------------------------------')
ler.close()
'''

'''
ler = open('banco\estoquepizza.txt', 'r')
ler_array = []
linhas = ler.readlines()
for linha in linhas:
    ler_array.append(linha)
ler.close()

print('---------------------------------------------------------------------')
sabor = ler_array[0]
print(sabor)
'''
'''
ler = open('banco\estoquepizza.txt', 'r')
cont = 0

for linha1 in ler:
    cont = cont + 1 
ler.seek(0)
cont = cont // 4
print('COD','| SABOR'.ljust(25),'| CÓDIGO'.rjust(5).ljust(14),'| QUANTIDADE'.ljust(14).rjust(5),'| PREÇO'.ljust(8),'|')
print('---------------------------------------------------------------------')
for linha in range(0, cont): 
    linha += 1 
    print(f' {linha}  |',f'{ler.readline().rstrip().ljust(24)}|',f'{ler.readline().rstrip().rjust(5).ljust(13)}|',f'{ler.readline().rstrip().rjust(5).ljust(13)}|',f'{ler.readline().rstrip().rjust(5).ljust(7)}|')
    #print('----------------------------------------------------------------------')
ler.close()
'''
ler = open('banco\estoquepizza.txt', 'r')
cont = 0

for linha1 in ler:
    cont = cont + 1 
ler.seek(0)
cont = cont // 4
print('| CÓDIGO'.rjust(2).ljust(2),'| SABOR'.ljust(25),'| QUANTIDADE'.ljust(12).rjust(5),'| PREÇO'.ljust(7),'|')
print('------------------------------------------------------------')
for linha in range(0, cont): 
    linha += 1 
    print(f'|{ler.readline().rstrip().rjust(4).ljust(8)}|',f'{ler.readline().rstrip().ljust(24)}|',f'{ler.readline().rstrip().rjust(5).ljust(11)}|',f'{ler.readline().rstrip().rjust(5).ljust(6)}|')
print('------------------------------------------------------------')
ler.close()
opc = int(input('DESEJA SAIR? [1]SIM [2]NÃO'
                        '\n->' ))
Logo.linha()           
if opc == 1:
    pizza_editar()