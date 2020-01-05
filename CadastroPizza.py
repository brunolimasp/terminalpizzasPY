import Logo
import os
from time import sleep




def pizza_cadastro():
    os.system("cls")
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\CADASTRAR')
    Logo.linha()
    print('\t\tCADASTRAR')
    Logo.linha()
    
    while True:  
        sabor = input('SABOR: ')
        codigo = input('CÓDIGO: ')
        quant = input('QUANTIDADE: ')
        preço = input('PREÇO: ')
        Logo.linha()

        estoque = open('banco\estoquepizza.txt', 'a')
        estoque.write('\nsabor:'+ sabor + '\n' + 'codigo:'+ codigo + '\n' + 'quant:'+ quant + '\n' + 'preco:'+ preço + '\n' )
        estoque.write(15 *'-')
        estoque.close()
    
        print(f'SABOR DA PIZZA: {sabor}') 
        print(f'CÓDIGO DA PIZZA: {codigo}')
        print(f'QUANTIDADE: {quant}')
        print(f'PREÇO DA PIZZA: {preço}')
        Logo.linha()
        opc = int(input('\tDESEJA CADASTRAR OUTRO PRODUTO?'
                        '\n\t[1] SIM' 
                        '\n\t[2] NÃO'
                        '\n\t->' ))
        Logo.linha()           
        if opc == 2:
            PizzaMenu()



def PizzaMenu():
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA')
    Logo.linha()
    print('\t\tCADASTRO - PIZZA')
    Logo.linha()

    while True:
        escolha = int(input(('[1] CADASTRAR'
                           '\n[2] LISTAR / EDITAR'
                           '\n[3] VOLTAR'
                           '\n->')))
        if escolha == 1:
            os.system("cls")
            pizza_cadastro()

            break
        elif escolha == 2:
            os.system("cls")
            #CadBebidas
            print('2')
            break
        elif escolha == 3:
            os.system("cls")
            import MenuCadastro
            MenuCadastro.MenuCadastro
            print('3')
            break
        else:
            os.system("cls")
            print('OPÇÃO INVALIDA!')
