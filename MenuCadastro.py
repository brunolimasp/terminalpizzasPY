import Logo
import os


def MenuCadastro():
    Logo.logo()
    Logo.limpeza()

    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS')
    Logo.linha()
    print('\t\t\tESTOQUE DE PRODUTOS')
    Logo.linha()


    while True:
        escolha = int(input(('[1] PIZZA'
                           '\n[2] BEBIDAS'
                           '\n[3] CERVEJAS'
                           '\n[4] VOLTAR'
                           '\n->')))
        if escolha == 1:
            Logo.limpeza()
            import CadastroPizza
            CadastroPizza.PizzaMenu()
            break
        
        elif escolha == 2:
            Logo.limpeza()  
            break

        elif escolha == 3:
            Logo.limpeza()
            break

        elif escolha == 4:
            Logo.limpeza()
            import MenuPrincipal
            MenuPrincipal.Menu()
            break
        
        else:
            Logo.limpeza()
            print('OPÇÃO INVALIDA!')

