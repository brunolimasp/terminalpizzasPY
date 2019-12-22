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
    sleep(1)


def TipoDeUsuario():
    while True:
        TipoLogin = int(input('\t\t[1] USUARIO COMUM              [0] Administrador \n'))
        if TipoLogin == 1:
            logo()
            menu.MenuPrincipal()
        elif TipoLogin == 0:
            logo()
            menu.MenuPrincipal()
        else:
            print("OPCAO INCORRETA!!\n TENTE NOVAMNETE!!")
            os.system("cls")


logo()
TipoDeUsuario()




