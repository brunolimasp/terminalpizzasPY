import Logo
import os
from time import sleep
from Logo import limpeza




def pizza_cadastro():
    Logo.limpeza()
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\CADASTRAR')
    Logo.linha()
    print('\t\tCADASTRAR')
    Logo.linha()
    
    while True:
        codigo = input('CÓDIGO: ')  
        sabor = input('SABOR: ').upper()
        quant = input('QUANTIDADE: ')
        preço = float(input('PREÇO: '))
        
        
        Logo.linha()

        estoque = open('banco\estoquepizza.txt', 'a')
        estoque.write(codigo + '\n' + sabor + '\n' + quant + '\n' + str(preço) + '\n' )
        estoque.close()
    
        print(f'CÓDIGO DA PIZZA: {codigo}')    
        print(f'SABOR DA PIZZA: {sabor}') 
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
    print('\t\t\tCADASTRO - PIZZA')
    Logo.linha()

    while True:
        escolha = int(input(('[1] CADASTRAR'
                           '\n[2] LISTAR / EDITAR'
                           '\n[3] VOLTAR'
                           '\n->')))
        if escolha == 1:
            Logo.limpeza()
            pizza_cadastro()
            break
        elif escolha == 2:
            Logo.limpeza()
            import ListarEditar
            ListarEditar.pizza_editar()
            break
        elif escolha == 3:
            Logo.limpeza()
            import MenuCadastro
            MenuCadastro.MenuCadastro()
            break
        else:
            Logo.limpeza()
            print('OPÇÃO INVALIDA!')
