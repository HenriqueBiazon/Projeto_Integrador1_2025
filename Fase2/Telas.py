## APAGAR TERMINAL
def apagarTerminal():
    import os
    os.system("cls")

## MENU

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
## CLASSIFICANDO
def classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte):
    medias = [0, 0, 0, 0]

    print()
    print(f"-------------------CLASSIFICAÇÃO DA SUSTENTABILIDADE DO DIA {data}:--------------------")
    print()
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ÁGUA: ", end="")

    if consumo_agua < 150:
        print('Alta sustentabilidade')
        medias[0] += 1
    elif 150 <= consumo_agua <= 200:
        print('Moderada sustentabilidade.')
    else:
        print('Baixa sustentabilidade.')
        medias[0] -= 1

    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ENERGIA: ", end="")

    if consumo_energia < 5:
        print('Alta sustentabilidade.')
        medias[1] += 1
    elif 5 <= consumo_energia <= 10:
        print('Moderada sustentabilidade.')
    else:
        print('Baixa sustentabilidade.')
        medias[1] -= 1

    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE RECICLAGEM: ", end="")

    if porcentagem_reciclagem > 50:
        print('Alta sustentabilidade.')
        medias[2] += 1
    elif 20 <= porcentagem_reciclagem <= 50:
        print('Moderada sustentabilidade.')
    else:
        print('Baixa sustentabilidade.')
        medias[2] -= 1

    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ", end="")

    if ((meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM')) and ((meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM')):
        print('Moderada sustentabilidade.')

    elif (meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM'):
        print('Baixa sustentabilidade.')
        medias[3] -= 1
    else:
        print('Alta sustentabilidade.')
        medias[3] += 1

    return medias
## INSERIR DIA
def telaInserir():
    from conectBanco import DBinsert_dados, DBselect

    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         INSERIR
-------------------------------------------------------------------------------------------
    """)
    print("INSIRA A DATA DE HOJE (DD/MM/AAAA):")
    data = str(input("> "))

    dataInvalida = True
    while dataInvalida:
        for x in DBselect():
            if x[1] == data:
                dataInvalida = True
                break
            else:
                dataInvalida = False
        if dataInvalida:
            print()
            print("ERRO! Digite uma data ainda não inserida:\n(Digite 0 para voltar para o menu)")
            data = input(">")
            if data == "0":
                return
            dataInvalida = True

    print()
    print("INSIRA SEUS DADOS DE CONSUMO DE ÁGUA (L):")
    consumo_agua = int(input("> "))
    print()

    print("INSIRA SEUS DADOS DE CONSUMO DE ENERGIA (KwH):")
    consumo_energia = int(input("> "))
    print()

    print("INSIRA A PORCENTAGEM DE RESÍDUOS RECICLADOS (%):")
    porcentagem_reciclagem = int(input("> "))
    print()

    print('QUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (SIM/NÃO)')
    meios_transporte = ['', '', '', '', '', '']

    meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
    meios_transporte[1] = input('BICICLETA: ').upper()
    meios_transporte[2] = input('CAMINHADA: ').upper()
    meios_transporte[3] = input('CARRO (Combustível fóssil): ').upper()
    meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
    meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()

    string_meios_transporte = ','.join(meios_transporte)

    classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte)

    DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)

    input("\n                                    <APERTE ENTER>")

## ALTERAR DIA

def telaAlterar():
    from conectBanco import DBselect, DBselect_dia, DBalter_dia

    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         ALTERAR
-------------------------------------------------------------------------------------------
    """)
    print("INSIRA A DATA PARA ALTERAR (DD/MM/AAAA): ")
    data = input(">")

    dataValida = False
    while not dataValida:
        for x in DBselect():
            if x[1] == data:
                dataValida = True
                break
        if not dataValida:
            print("ERRO! Digite uma data já inserida:\n(Digite 0 para voltar para o menu)")
            data = input(">")
            if data == "0":
                return

    myresult = DBselect_dia(data)
    myresult[5] = myresult[5].split(",")

    classificacaoDia(myresult[1], myresult[2], myresult[3], myresult[4], myresult[5])

    print()
    print("-----------------------------------VALORES CADASTRADOS:------------------------------------")
    print()
    print(f"CONSUMO DE ÁGUA: {myresult[2]}")
    print(f"CONSUMO DE ENERGIA: {myresult[3]}")
    print(f"PORCENTAGEM DE RECICLAGEM: {myresult[4]}")
    print()
    print("MEIOS DE TRANSPORTE UTILIZADOS:")
    print(f"TRANSPORTE PÚBLICO {myresult[5][0]}")
    print(f"BICICLETA: {myresult[5][1]}")
    print(f"CAMINHADA: {myresult[5][2]}")
    print(f"CARRO (combustível fóssil): {myresult[5][3]}")
    print(f"CARRO ELÉTRICO: {myresult[5][4]}")
    print(f"CARONA COMPARTILHADA (combustível fóssil): {myresult[5][5]}")
    print()
    input("<APERTE ENTER>")
    print()
    print("-------------------------------------------------------------------------------------------")
    print()
    print("                             QUAL DADO VOCÊ DESEJA ALTERAR?")
    print("""-------------------------------------------------------------------------------------------
|    1 - ÁGUA     |   2 - ENERGIA   | 3 - RECICLAGEM | 4 - TRANSPORTE  |    5 - NENHUM    |
-------------------------------------------------------------------------------------------""")
    
    opcaoAlterar = int(input(">"))
    while 1 > opcaoAlterar or opcaoAlterar > 5:
        print()
        print("ERRO! Escolha uma opção válida (1 a 5):")
        opcaoAlterar = int(input(">"))
    print()

    if opcaoAlterar == 1:
        print(f"ALTERANDO O CONSUMO DE ÁGUA DO DIA {data}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ÁGUA (L):")
        consumo_agua = int(input("> "))
        DBalter_dia(data, "consumo_agua", consumo_agua)

        print("\nCONSUMO DE ÁGUA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 2:
        print(f"ALTERANDO O CONSUMO DE ENERGIA DO DIA {data}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ENERGIA (KwH):")
        consumo_energia = int(input("> "))
        DBalter_dia(data, "consumo_energia", consumo_energia)

        print("\nCONSUMO DE ENERGIA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 3:
        print(f"ALTERANDO A PORCENTAGEM DE RECICLAGEM DO DIA {data}")

        print("\nINSIRA SUA PORCENTAGEM ALTERADA DE RECICLAGEM (%):")
        porcentagem_reciclagem = int(input("> "))
        DBalter_dia(data, "porcentagem_reciclagem", porcentagem_reciclagem)

        print("\nPORCENTAGEM DE RECICLAGEM ALTERADA COM SUCESSO!")

    elif opcaoAlterar == 4:
        print(f"ALTERANDO OS MEIOS DE TRANSPORTE UTILIZADOS NO DIA {data}")

        print('\nQUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (SIM/NÃO)')

        meios_transporte = ['', '', '', '', '', '']
        meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
        meios_transporte[1] = input('BICICLETA: ').upper()
        meios_transporte[2] = input('CAMINHADA: ').upper()
        meios_transporte[3] = input('CARRO (Combustível fóssil): ').upper()
        meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
        meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()

        string_meios_transporte = ','.join(meios_transporte)

        DBalter_dia(data, "meios_transporte", string_meios_transporte)

        print("\nMEIOS DE TRANSPORTE UTILIZADOS ALTERADOS COM SUCESSO!")

    else:
        print("NENHUMA ALTERAÇÃO FEITA")
        return
    
    myresult = DBselect_dia(data)
    myresult[5] = myresult[5].split(",")

    classificacaoDia(myresult[1], myresult[2], myresult[3], myresult[4], myresult[5])

    input("\n                                    <APERTE ENTER>")

## EXCLUIR DIA

def telaExcluir():
    from conectBanco import DBselect, DBselect_dia, DBdelete_dia

    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         EXCLUIR
-------------------------------------------------------------------------------------------
    """)
    print("INSIRA A DATA PARA EXCLUIR (DD/MM/AAAA): ")
    data = input(">")

    dataValida = False
    while not dataValida:
        for x in DBselect():
            if x[1] == data:
                dataValida = True
                break
        if not dataValida:
            print("ERRO! Digite uma data já inserida:\n(Digite 0 para voltar para o menu)")
            data = input(">")
            if data == "0":
                return
    print()

    myresult = DBselect_dia(data)
    myresult[5] = myresult[5].split(",")

    classificacaoDia(myresult[1], myresult[2], myresult[3], myresult[4], myresult[5])

    print()
    print("-----------------------------------VALORES CADASTRADOS:------------------------------------")
    print()
    print(f"CONSUMO DE ÁGUA: {myresult[2]}")
    print(f"CONSUMO DE ENERGIA: {myresult[3]}")
    print(f"PORCENTAGEM DE RECICLAGEM: {myresult[4]}")
    print()
    print("MEIOS DE TRANSPORTE UTILIZADOS:")
    print(f"TRANSPORTE PÚBLICO {myresult[5][0]}")
    print(f"BICICLETA: {myresult[5][1]}")
    print(f"CAMINHADA: {myresult[5][2]}")
    print(f"CARRO (combustível fóssil): {myresult[5][3]}")
    print(f"CARRO ELÉTRICO: {myresult[5][4]}")
    print(f"CARONA COMPARTILHADA (combustível fóssil): {myresult[5][5]}")
    print()
    input("<APERTE ENTER>")
    print()
    print(f"""
-------------------------------------------------------------------------------------------

                        TEM CERTEZA QUE DESEJA EXCLUIR O DIA {data}                                           
-------------------------------------------------------------------------------------------
|                   1 - SIM                   |                  2 - NÃO                  |
-------------------------------------------------------------------------------------------
""")
    opcaoExcluir = int(input(">"))
    
    while opcaoExcluir < 1 or opcaoExcluir > 2:
        print()
        print("ERRO! Escolha uma opção válida:")
        opcaoExcluir = int(input(">"))
    print()
    if opcaoExcluir == 1:
        DBdelete_dia(data)
        print(f"DIA {data} EXCLUÍDO COM SUCESSO\n")
    else:
        print("VOLTANDO PARA A TELA DE MENU\n")
    input("                                    <APERTE ENTER>")

## CLASSIFICAR DIA

def telaClassificar():
    from conectBanco import DBselect

    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                        CLASSIFICAR
-------------------------------------------------------------------------------------------""")

    myresult = DBselect()
    medias = [0, 0, 0, 0]
    for x in myresult:
        data = x[1]
        consumo_agua = x[2]
        consumo_energia = x[3]
        porcentagem_reciclagem = x[4]
        string_meio_transporte = x[5]
        meios_transporte = string_meio_transporte.split(",")

        mediaDia = classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte)
        medias = [medias[i] + mediaDia[i] for i in range(len(medias))]

    print()
    print("                       MÉDIA DA CLASSIFICAÇÃO DE TODOS OS DIAS:")
    print()
    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ÁGUA: ", end="")

    if medias[0] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[0] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ENERGIA: ", end="")

    if medias[1] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[1] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE RECICLAGEM: ", end="")

    if medias[2] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[2] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ", end="")

    if medias[3] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[3] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    input("\n                                    <APERTE ENTER>")