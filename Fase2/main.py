#Fase 2 - Implementação do banco de dados

from pTelaMenu import telaMenu
from pTelaInserir import telaInserir
from pApagarTerminal import apagarTerminal
from pTelaClassificar import telaClassficar
apagarTerminal()
#Fase 1 - Sistema de clssificação de sutentabilidade pessoal diário
input(">")
#Tela de início
sair = False
while sair == False:

    opcaoMenu = telaMenu() #Printa o menu e pega a opção escolhida

    apagarTerminal()    
    
    if opcaoMenu == 1:
        telaInserir() 
        apagarTerminal()
    elif opcaoMenu == 2:
        print("Alterar")
    elif opcaoMenu == 3:
        print("Excluir")
    elif opcaoMenu == 4:
        telaClassficar()
        apagarTerminal()
    elif opcaoMenu == 5:
        print("Saindo")
        sair = True
        apagarTerminal()
        break