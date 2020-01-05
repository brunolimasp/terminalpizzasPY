import Logo
import os
from time import sleep




def pizza_cadastro():
    Logo.limpeza()
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
        estoque.write(sabor + '\n' + codigo + '\n' + quant + '\n' + preço + '\n' )
        estoque.close()
    
        print(f'SABOR DA PIZZA: {sabor}') 
        print(f'CÓDIGO DA PIZZA: {codigo}')
        print(f'QUANTIDADE: {quant}')
        print(f'PREÇO DA PIZZA: {preço}')
        Logo.linha()
        opc = int(input('DESEJA CADASTRAR OUTRO PRODUTO? [1]SIM [2]NÃO'
                        '\n->' ))
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
