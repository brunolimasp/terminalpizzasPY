from time import sleep
from validador import *
import Logo


def TipoDeUsuario():
    while True:
        Logo.linha()
        TipoLogin = int(input('\t\t\t[1] USUARIO COMUM              [0] Administrador \n'
                                                       '\t\t\t->'))
                                                       
        if TipoLogin == 1:
            login1()
            break
        elif TipoLogin == 0:
            login1()
            break
        else:
            Logo.limpeza()
            print("OPCAO INCORRETA!!\n TENTE NOVAMENTE!!")
            sleep(2)
            Logo.limpeza()

def login1 ():
    c = Validador('','')
    c.ValidacaoComum()

Logo.logo()

TipoDeUsuario()




