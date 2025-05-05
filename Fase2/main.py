#Fase 2 - Implementação do banco de dados

from Telas import telaAlterar, telaClassificar, telaExcluir, telaInserir, telaMenu, telaLogin, apagarTerminal

#Fase 1 - Sistema de clssificação de sutentabilidade pessoal diário

#Fase 3 - Tela de log-in:
Id_usuario = telaLogin()

apagarTerminal()
print(Id_usuario)
#Tela de início
sair = False
while sair == False:

    opcaoMenu = telaMenu() #Printa o menu e pega a opção escolhida

    apagarTerminal()

    if opcaoMenu == 1:

        telaInserir(Id_usuario) 

    elif opcaoMenu == 2:

        telaAlterar(Id_usuario)

    elif opcaoMenu == 3:

        telaExcluir(Id_usuario)

    elif opcaoMenu == 4:

        telaClassificar(Id_usuario)

    elif opcaoMenu == 5:

        print("\n                    OBRIGADO POR USAR O SISTEMA DE SUSTENTABILIDADE!")
        sair = True

    input("                                    <APERTE ENTER>")

    apagarTerminal()