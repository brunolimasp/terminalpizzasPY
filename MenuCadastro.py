import Logo
import os


def MenuCadastro():
    Logo.logo()
    Logo.limpeza()

    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS')
    Logo.linha()
    print('\t\tESTOQUE DE PRODUTOS')
    Logo.linha()


    while True:
        escolha = int(input(('[1] PIZZA'
                           '\n[2] BEBIDAS'
                           '\n[3] CERVEJAS'
                           '\n[4] VOLTAR'
                           '\n->')))
        if escolha == 1:
            os.system("cls")
            import CadastroPizza
            CadastroPizza.PizzaMenu()
            break
        
        elif escolha == 2:
            os.system("cls")
            #CadastroCervejas  
            break

        elif escolha == 3:
            os.system("cls")
            #CadastroCervejas
            break

        elif escolha == 4:
            os.system("cls")
            
            
            break
        else:
            os.system("cls")
            print('OPÇÃO INVALIDA!')

MenuCadastro()