import Logo
import os
from time import sleep

def listar():
    Logo.linha()
    ler = open('banco\estoquepizza.txt', 'r')
    print(ler.readlines())
    ler.seek(0)
    Logo.linha()
    ler.close()
    

def pizza_editar():
    Logo.limpeza()
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\LISTAR / EDITAR')
    Logo.linha()
    print('\t\tLISTAR / EDITAR')
    Logo.linha()
    while True:
        escolha = int(input(('[1] LISTAR'
                           '\n[2] EDITAR'
                           '\n[3] VOLTAR'
                           '\n->')))
        if escolha == 1:
            Logo.limpeza()
            Logo.logo()
            listar()
            break
        elif escolha == 2:
            Logo.limpeza()
            Logo.logo()
            break
        elif escolha == 3:
            Logo.limpeza()
            Logo.logo()

            break
        else:
            Logo.limpeza()
            print('OPÇÃO INVALIDA!')


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
            pizza_editar()
            break
        elif escolha == 3:
            Logo.limpeza()
            import MenuCadastro
            MenuCadastro.MenuCadastro()
            break
        else:
            Logo.limpeza()
            print('OPÇÃO INVALIDA!')
