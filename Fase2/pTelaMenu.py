def telaMenu():
    print("""
    -------------------------------------------------------------------------------------------
    |                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
    -------------------------------------------------------------------------------------------

                                                MENU
    -------------------------------------------------------------------------------------------
    |   1 - INSERIR   |   X - ALTERAR   |   X - EXCLUIR   | 4 - CLASSIFICAR |    5 - SAIR     |
    -------------------------------------------------------------------------------------------
    """)
    opcaoMenu = int(input(">"))

    while 1 > opcaoMenu or opcaoMenu > 5:
        print("Escolha uma opção válida")
        opcao = int(input(">"))

    return opcaoMenu

