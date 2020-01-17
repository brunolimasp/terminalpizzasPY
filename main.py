from time import sleep
from validador import *
import Logo

def TipoDeUsuario():
    Logo.limpeza()
    Logo.logo()
    while True:
        Logo.linha()
        print('\t\t\t[1] USUARIO COMUM              [0] Administrador')
        print('####################################################################################################')
        TipoLogin = int(input('-------------> '.rjust(48).ljust(48)))
        print(end='')
        if TipoLogin == 1:
            login1()
            break
        elif TipoLogin == 0:
            login0()
            break
        else:
            Logo.limpeza()
            print("OPCAO INCORRETA!!\n TENTE NOVAMENTE!!")
            sleep(2)
            Logo.limpeza()

def login1 ():
    Logo.limpeza()
    c = Validador('','')
    c.ValidacaoComum()


def login0():
    Logo.limpeza()
    c = ValidadorAdm('','')
    c.ValidacaoAdm()






TipoDeUsuario()





