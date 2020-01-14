import time
import Logo


class Validador():
    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha

    def ValidacaoComum(self):
        banco = open('banco/Usuarios.txt', 'r')  # ABRE O ARQUIVO
        lista = banco.read().split()  # TRANSFORMA EM LISTA
        while True:
            self.usuario = input(str('\t\t\t################# USUARIO #################\n'
                                     '\t\t\t->'))
            self.senha = input(str('\t\t\t#################   SENHA  #################\n'
                                   '\t\t\t->'))
            validador = (self.usuario in lista)
            validadorSenha = (self.senha in lista)
            if (validador == True) and (validadorSenha == True):
                import MenuPrincipal
                MenuPrincipal.Menu()
            else:
                Logo.logo()
                print('USUARIO OU SENHA INCORRETA\n TENTE NOVAMENTE')
                time.sleep(1)


class ValidadorAdm():
    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha

    def ValidacaoAdm(self):
        banco = open('banco/UsuariosAdm.txt', 'r')  # ABRE O ARQUIVO
        lista = banco.read().split()  # TRANSFORMA EM LISTA
        while True:
            self.usuario = input(str('\t\t\t################# USUARIO #################\n'
                                     '\t\t\t->'))
            self.senha = input(str('\t\t\t#################   SENHA  #################\n'
                                   '\t\t\t->'))
            validador = (self.usuario in lista)
            validadorSenha = (self.senha in lista)
            if (validador == True) and (validadorSenha == True):
                import MenuPrincipal
                MenuPrincipal.Menu()
            else:
                Logo.logo()
                print('USUARIO OU SENHA INCORRETA\n TENTE NOVAMENTE')
                time.sleep(1)