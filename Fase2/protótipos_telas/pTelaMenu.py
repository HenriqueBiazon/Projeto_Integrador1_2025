def telaMenu():
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                            MENU
-------------------------------------------------------------------------------------------
|   1 - INSERIR   |   2 - ALTERAR   |   3 - EXCLUIR   | 4 - CLASSIFICAR |    5 - SAIR     |
-------------------------------------------------------------------------------------------
    """)
    opcaoMenu = 0
    opcaoMenu = int(input(">"))

    while 1 > opcaoMenu or opcaoMenu > 5:
        print()
        print("ERRO! Escolha uma opção válida (1 a 5):")
        opcaoMenu = int(input(">"))

    return opcaoMenu

