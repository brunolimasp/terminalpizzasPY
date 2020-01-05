import os
import sys

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

# Print de linhas para estetica do sistema
def linha():
    print(100 * '#')

def limpeza():
    import sys
    # Pega qual é o SO
    so = sys.platform
    so_clear = ''

    # Defini o argumento para limpeza de tela de acordo com o SO
    if (so == 'linux'):
        so_clear = 'clear'
    elif (so[:3] == 'win'):
        so_clear = 'cls'

    # Função lambda para limpeza de tela
    if so_clear:
        limpar = lambda l: os.system(l)
    else:
        limpar = lambda l: l