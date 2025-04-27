#Fase 2 - Implementação do banco de dados

from Telas import telaAlterar, telaClassificar, telaExcluir, telaInserir, telaMenu, apagarTerminal

#Fase 1 - Sistema de clssificação de sutentabilidade pessoal diário

#Tela de início
sair = False
while sair == False:

    opcaoMenu = telaMenu() #Printa o menu e pega a opção escolhida

    apagarTerminal()

    if opcaoMenu == 1:

        telaInserir() 

    elif opcaoMenu == 2:

        telaAlterar()

    elif opcaoMenu == 3:

        telaExcluir()

    elif opcaoMenu == 4:

        telaClassificar()

    elif opcaoMenu == 5:

        print("OBRIGADO POR USAR O SISTEMA DE SUSTENTABILIDADE!")
        input("\n                                    <APERTE ENTER>")
        sair = True

    apagarTerminal()