import Logo
import os
from time import sleep
from Logo import limpeza
  

def listar():
    while True:    
        Logo.limpeza()
        Logo.logo()
        print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\LISTAR / EDITAR\\LISTAR')
        Logo.linha()
        print('\t\tLISTAR')
        Logo.linha()
    
        ler = open('banco\estoquepizza.txt', 'r')
        for linha in ler:
            linha = linha.rstrip()
            print('sabor:',linha)
    
        ler.seek(0)
        ler.close()

        opc = int(input('DESEJA SAIR? [1]SIM [2]NÃO'
                        '\n->' ))
        Logo.linha()           
        if opc == 1:
            pizza_editar()


def pizza_editar():
    Logo.limpeza()
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\LISTAR / EDITAR')
    Logo.linha()
    print('\t\tLISTAR / EDITAR')
    Logo.linha()

    while True:
        escolha = int(input(('[1] LISTAR'
                           '\n[2] EDITAR'
                           '\n[3] VOLTAR'
                           '\n->')))
        if escolha == 1:
            Logo.limpeza()
            listar()
            break

        elif escolha == 2:
            Logo.limpeza()
            break

        elif escolha == 3:
            Logo.limpeza()
            break

        else:
            Logo.limpeza()
            print('OPÇÃO INVALIDA!')
