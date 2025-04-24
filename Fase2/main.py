#Fase 2 - Implementação do banco de dados

from pTelaMenu import telaMenu
from pTelaInserir import telaInserir
from pApagarTerminal import apagarTerminal

#Fase 1 - Sistema de clssificação de sutentabilidade pessoal diário

#Tela de início
sair = False
while sair == False:

    opcaoMenu = telaMenu() #Printa o menu e pega a opção escolhida

    

    if opcaoMenu == 1:
        telaInserir() 
    elif opcaoMenu == 2:
        print("Alterar")
    elif opcaoMenu == 3:
        print("Excluir")
    elif opcaoMenu == 4:
        print("CLassificar")
    elif opcaoMenu == 5:
        print("Saindo")
        sair = True
        break
    
    apagarTerminal()