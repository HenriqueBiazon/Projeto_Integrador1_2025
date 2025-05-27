##Sistema de monitoramento de sustentabilidade pessoal diária

from Telas import *

apagarTerminal()
print("\n\n      BEM VINDO AO SISTEMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL DIÁRIA!")
input("                                    <APERTE ENTER>")
apagarTerminal()

#Tela de início
sair = False
while sair == False:

    opcaoMenu = telaMenu() #Menu

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

        print("\n\n                    OBRIGADO POR USAR O SISTEMA DE SUSTENTABILIDADE!")
        sair = True

    input("                                    <APERTE ENTER>")

    apagarTerminal()