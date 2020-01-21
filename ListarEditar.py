import Logo
import os
from time import sleep
from Logo import limpeza
  
def editar():
    Logo.limpeza()
    Logo.logo()
    print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\LISTAR / EDITAR\\EDITAR')
    Logo.linha()
    print('\t\tEDITAR')
    Logo.linha()
    
    ler = open('banco\estoquepizza.txt', 'r')
    cont = 0

    for linha1 in ler:
        cont = cont + 1 
    ler.seek(0)
    cont = cont // 4
    print('| CÓDIGO'.rjust(2).ljust(2),'| SABOR'.ljust(25),'| QUANTIDADE'.ljust(14).rjust(5),'| PREÇO'.ljust(8),'|')
    print('------------------------------------------------------------')
    for linha in range(0, cont): 
        linha += 1 
        print(f'|{ler.readline().rstrip().rjust(4).ljust(8)}|',f'{ler.readline().rstrip().ljust(24)}|',f'{ler.readline().rstrip().rjust(5).ljust(13)}|',f'{ler.readline().rstrip().rjust(5).ljust(7)}|')
    print('------------------------------------------------------------')
    ler.close()
    opc = int(input('DESEJA SAIR? [1]SIM [2]NÃO'
                    '\n->' ))
    Logo.linha()           
    if opc == 1:
        pizza_editar()




def listar():
    while True:    
        Logo.limpeza()
        Logo.logo()
        print('>MENU PRINCIPAL\\ESTOQUE DE PRODUTOS\\PIZZA\\LISTAR / EDITAR\\LISTAR')
        Logo.linha()
        print('\t\tLISTAR')
        Logo.linha()
    
        ler = open('banco\estoquepizza.txt', 'r')
        cont = 0

        for linha1 in ler:
            cont = cont + 1 
        ler.seek(0)
        cont = cont // 4
        print('| CÓDIGO'.rjust(2).ljust(2),'| SABOR'.ljust(25),'| QUANTIDADE'.ljust(14).rjust(5),'| PREÇO'.ljust(8),'|')
        print('------------------------------------------------------------')
        for linha in range(0, cont): 
            linha += 1 
            print(f'|{ler.readline().rstrip().rjust(4).ljust(8)}|',f'{ler.readline().rstrip().ljust(24)}|',f'{ler.readline().rstrip().rjust(5).ljust(13)}|',f'{ler.readline().rstrip().rjust(5).ljust(7)}|')
        print('------------------------------------------------------------')
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
            editar()
            break

        elif escolha == 3:
            import CadastroPizza
            CadastroPizza.PizzaMenu()
            break

        else:
            Logo.limpeza()
            print('OPÇÃO INVALIDA!')
