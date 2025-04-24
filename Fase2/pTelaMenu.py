
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
    opcao = int(input(">"))

    while 1 > opcao or opcao > 5:
        print("Escolha uma opção válida")
        opcao = int(input(">"))

    if opcao == 1:
        print("Inserir")   
    elif opcao == 2:
         print("Alterar")
    elif opcao == 3:
         print("Excluir")
    elif opcao == 4:
         print("CLassificar")
    elif opcao == 5:
         print("Sair")
