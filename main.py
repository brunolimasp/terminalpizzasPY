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
        logo()
        TipoLogin = int(input('\t\t[1] USUARIO COMUM              [0] Administrador \n'))
        if TipoLogin == 1:
            logo()
            menu.MenuPrincipal()
            break
        elif TipoLogin == 0:
            logo()
            menu.MenuPrincipal()
            break
        else:
            os.system("cls")
            logo()
            print("OPCAO INCORRETA!!\n TENTE NOVAMENTE!!")
            sleep(2)
            os.system("cls")



def ValidacaoComum():
    banco = open('Usuarios.txt', 'r') #ABRE O ARQUIVO
    print (banco.read()) #LE O ARQUIVO



logo()
TipoDeUsuario()




