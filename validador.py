import time
import logo

class Validador():
    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha
    def ValidacaoComum(self):
        banco = open('banco/Usuarios.txt', 'r')  # ABRE O ARQUIVO
        lista = banco.read().split()  # TRANSFORMA EM LISTA
        while True:
            self.usuario = input(str('################# USUARIO #################\n'))
            self.senha = input(str('#################   SENHA  #################\n'))
            validador = (self.usuario in lista)
            validadorSenha = (self.senha in lista)
            if (validador == True) and (validadorSenha == True):
                print(' ACERTOUUU')
                break
            else:
                logo
                print('USUARIO OU SENHA INCORRETA\n TENTE NOVAMENTE')
                time.sleep(1)