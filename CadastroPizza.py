import Logo
import os

#def pizza_cadastro():


def PizzaMenu():
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA')
    print(50 * '#')
    print('\t\tCADASTRO - PIZZA')
    print(50 * '#')

    while True:
        escolha = int(input(('[1] CADASTRAR'
                           '\n[2] LISTAR / EDITAR'
                           '\n[3] VOLTAR'
                           '\n->')))
        if escolha == 1:
            os.system("cls")
            #def pizza_cadastro()
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
