import Logo


def Menu():
    Logo.limpeza()
    Logo.logo()
    print('>MENU PRINCIPAL')
    Logo.linha()
    print('\t\tMENU PRINCIPAL')
    Logo.linha()

    escolha = int(input(('[1] VENDAS'
                       '\n[2] RESGISTRAR FEEDBACK DE CLIENTES'
                       '\n[3] ESTOQUE E PRODUTOS'
                       '\n[4] RELATÓRIO DE VENDAS'
                       '\n[5] VOLTAR'
                        '\n->')))
    if escolha == 1:
        Logo.limpeza()
        
    
    elif escolha == 2:
        Logo.limpeza()
        
        
    elif escolha == 3:
        Logo.limpeza()
        import MenuCadastro
        MenuCadastro.MenuCadastro()

    elif escolha == 4:
        Logo.limpeza()
        
    elif escolha == 5:
        Logo.limpeza()
        import main
        main.TipoDeUsuario()
    else:
        Logo.limpeza()
        print('OPÇÃO INVALIDA!')
