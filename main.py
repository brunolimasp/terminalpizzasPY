from time import sleep
from validador import *
import logo


def TipoDeUsuario():
    while True:
        TipoLogin = int(input('\t\t[1] USUARIO COMUM              [0] Administrador \n'))
        if TipoLogin == 1:
            login1()
            break
        elif TipoLogin == 0:
            login1()
            break
        else:
            os.system("cls")
            print("OPCAO INCORRETA!!\n TENTE NOVAMENTE!!")
            sleep(2)
            os.system("cls")

def login1 ():
    c = Validador('','')
    c.ValidacaoComum()

logo.Logo()


TipoDeUsuario()




