from time import sleep
import os
import menu

def logo():
    os.system("cls")
    print("\n\n\n\t\t\t\t    1.0 B",)
    print("\t\t\t\tVERSAO PYTHON")
    print("\n\t######## ######## ########  ##     ## #### ##    ##    ###    ##\n")
    print("\t   ##    ##       ##     ## ###   ###  ##  ###   ##   ## ##   ##\n")
    print("\t   ##    ##       ##     ## #### ####  ##  ####  ##  ##   ##  ##\n")
    print("\t   ##    ######   ########  ## ### ##  ##  ## ## ## ##     ## ##\n")
    print("\t   ##    ##       ##   ##   ##     ##  ##  ##  #### ######### ##\n")
    print("\t   ##    ##       ##    ##  ##     ##  ##  ##   ### ##     ## ##\n")
    print("\t   ##    ######## ##     ## ##     ## #### ##    ## ##     ## ########\n\n")
    print("\t >PIZZAS_\n\n\n")


def TipoDeUsuario():
    while True:
        TipoLogin = int(input('\t\t[1] USUARIO COMUM              [0] Administrador \n'))
        if TipoLogin == 1:
            ValidacaoComum()
            break
        elif TipoLogin == 0:
            menu.MenuPrincipal()
            break
        else:
            os.system("cls")
            logo()
            print("OPCAO INCORRETA!!\n TENTE NOVAMENTE!!")
            sleep(2)
            os.system("cls")




def ValidacaoComum():
    logo()
    banco = open('banco/Usuarios.txt', 'r')  # ABRE O ARQUIVO
    lista = banco.read().split()  # TRANSFORMA EM LISTA

    while True:
        usuario = input(str('################# USUARIO #################\n'))
        validador = (usuario in lista)
        if validador == True:
            Senha = input(str('#################   SENHA   #################\n'))
            validador = (Senha in lista)
            if validador == True:
                menu.MenuPrincipal()
                break
        else:
            print('SENHA INCORRETA!!\n TENTE NOVAMENTE')


logo()
TipoDeUsuario()




