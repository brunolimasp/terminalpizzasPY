
ler = open('banco\estoquepizza.txt', 'r')
conjunto = ler.readlines()

print(conjunto)
print(conjunto[0], conjunto[1], conjunto[12])
ler.seek(0)

    
    