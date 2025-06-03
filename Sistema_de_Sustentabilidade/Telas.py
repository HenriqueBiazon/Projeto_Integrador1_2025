import os
from conectBanco import *
from criptografia import criptografar,descriptografar

## APAGAR TERMINAL
def apagarTerminal():
    os.system("cls" if os.name == "nt" else "clear")

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
    opcaoMenu = int(input(">"))

    while 1 > opcaoMenu or opcaoMenu > 5:
        print()
        print("ERRO! Escolha uma opção válida (1 a 5):")
        opcaoMenu = int(input(">"))

    return opcaoMenu

## CLASSIFICANDO

def classificacaoDia(data):
    consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte = DBselect_dia(data)[2:6]
    meios_transporte = string_meios_transporte.split(",")

    classificacao = ["","","",""]

    if consumo_agua < 150:
        classificacao[0] = 'Alta'
    elif 150 <= consumo_agua <= 200:
        classificacao[0] = 'Moderada'
    else:
        classificacao[0] = 'Baixa'

    if consumo_energia < 5:
        classificacao[1] = 'Alta'
    elif 5 <= consumo_energia <= 10:
        classificacao[1] = 'Moderada'
    else:
        classificacao[1] = 'Baixa'

    if porcentagem_reciclagem > 50:
        classificacao[2] = 'Alta'
    elif 20 <= porcentagem_reciclagem <= 50:
        classificacao[2] = 'Moderada'
    else:
        classificacao[2] = 'Baixa'

    if ((meios_transporte[1] == 'S') or (meios_transporte[0] == 'S') or (meios_transporte[4] == 'S') or (meios_transporte[2] == 's')) and ((meios_transporte[5] == 'S') or (meios_transporte[3] == 'S')):
        classificacao[3] = 'Moderada '
    elif (meios_transporte[5] == 'S') or (meios_transporte[3] == 'S'):
        classificacao[3] = 'Baixa'
    else:
        classificacao[3] = 'Alta'
    classificacao[0] = criptografar(classificacao[0])
    classificacao[1] = criptografar(classificacao[1])
    classificacao[2] = criptografar(classificacao[2])
    classificacao[3] = criptografar(classificacao[3])
    return classificacao

def mostrarClassificacao(data):
    classificacao_aguaCript, classificacao_energiaCript, classificacao_reciclagemCript, classificacao_transporteCript = DBselect_classificacao_dia(data)[2:6]
    classificacao_agua = descriptografar(classificacao_aguaCript)
    classificacao_energia = descriptografar(classificacao_energiaCript)
    classificacao_reciclagem = descriptografar(classificacao_reciclagemCript)
    classificacao_transporte = descriptografar(classificacao_transporteCript)

    print()
    print(f"                    CLASSIFICAÇÃO DA SUSTENTABILIDADE DO DIA {data}:                     ")
    print()
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ÁGUA: ", end="")
    print(f"{classificacao_agua} SUSTENTABILIDADE.")
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ENERGIA: ", end="")
    print(f"{classificacao_energia} SUSTENTABILIDADE.")
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE RECICLAGEM: ", end="")
    print(f"{classificacao_reciclagem} SUSTENTABILIDADE.")
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ", end="")
    print(f"{classificacao_transporte} SUSTENTABILIDADE.")
    print()

## INSERIR DIA

def telaInserir():
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
    while dataInvalida == True:
        tabela = DBselect()
        if data == "0":
            return
        if len(tabela) == 0:
            dataInvalida = False
        for x in tabela:
            if x[1] == data:
                dataInvalida = True
                break
            else:
                dataInvalida = False
        digitosData = data.split("/")
        for x in digitosData:
            if not x.isdigit():
                dataInvalida = True
                break
        if dataInvalida:
            print("\nERRO! Digite uma data válida:\n")
            print("DATAS JÁ INSERIDAS:")
            for x in tabela:
                print("-",x[1])
            print("(OU digite 0 para voltar para o menu)")
            data = input(">")
            dataInvalida = True
    while True:
        try:
            print()
            print("INSIRA SEUS DADOS DE CONSUMO DE ÁGUA (L):")
            consumo_agua = float(input("> "))
            print()

            print("INSIRA SEUS DADOS DE CONSUMO DE ENERGIA (KwH):")
            consumo_energia = float(input("> "))
            print()

            print("INSIRA A PORCENTAGEM DE RESÍDUOS RECICLADOS (%):")
            porcentagem_reciclagem = int(input("> "))
            print()

            print('QUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (S/N)')
            meios_transporte = ['', '', '', '', '', '']

            meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
            meios_transporte[1] = input('BICICLETA: ').upper()
            meios_transporte[2] = input('CAMINHADA: ').upper()
            meios_transporte[3] = input('CARRO (Combustível fóssil): ').upper()
            meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
            meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()
            break
        except:
            print("ERRO! O dado inserido está inválido")
        print()
    #Inserir dados na tabela
    string_meios_transporte = ','.join(meios_transporte)
    DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)
    #Inserir classificacao na tabela
    classificacao_aguaCript, classificacao_energiaCript,classificacao_reciclagemCript,classificacao_transporteCript = classificacaoDia(data)[0:4]
    DBinsert_classificacao(data,classificacao_aguaCript, classificacao_energiaCript,classificacao_reciclagemCript,classificacao_transporteCript)
    #Mostra a classificação do dia
    mostrarClassificacao(data)

## ALTERAR DIA

def telaAlterar():
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         ALTERAR
-------------------------------------------------------------------------------------------
""")
    tabela = DBselect()

    if len(tabela) == 0:
        print("ERRO! Insira alguma data no sistema")
        return
    
    print("DATAS JÁ INSERIDAS:")
    for x in tabela:
        print("-",x[1])
    print("(Digite 0 para voltar para o menu)\n")
    print("INSIRA A DATA PARA ALTERAR (DD/MM/AAAA): ")
    data = input(">")

    dataInvalida = True
    while dataInvalida == True:
        if data == "0":
            return
        for x in tabela:
            if x[1] == data:
                dataInvalida = False
                break
        if dataInvalida:
            print("\nERRO! Digite uma data já inserida no sistema:\n")
            print("DATAS JÁ INSERIDAS:")
            for x in tabela:
                print("-",x[1])
            print("(OU digite 0 para voltar para o menu)")
            data = input(">")

    mostrarClassificacao(data)

    consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte = DBselect_dia(data)[2:6]
    meios_transporte = string_meios_transporte.split(",")

    print("-----------------------------------VALORES CADASTRADOS:------------------------------------")
    print()
    print(f"CONSUMO DE ÁGUA: {consumo_agua}")
    print(f"CONSUMO DE ENERGIA: {consumo_energia}")
    print(f"PORCENTAGEM DE RECICLAGEM: {porcentagem_reciclagem}%")
    print()
    print("MEIOS DE TRANSPORTE UTILIZADOS:")
    print(f"TRANSPORTE PÚBLICO {meios_transporte[0]}")
    print(f"BICICLETA: {meios_transporte[1]}")
    print(f"CAMINHADA: {meios_transporte[2]}")
    print(f"CARRO (combustível fóssil): {meios_transporte[3]}")
    print(f"CARRO ELÉTRICO: {meios_transporte[4]}")
    print(f"CARONA COMPARTILHADA (combustível fóssil): {meios_transporte[5]}")
    print()
    input("                                    <APERTE ENTER>")
    print("""
-------------------------------------------------------------------------------------------
                               QUAL DADO VOCÊ DESEJA ALTERAR?
-------------------------------------------------------------------------------------------
|    1 - ÁGUA     |   2 - ENERGIA   | 3 - RECICLAGEM | 4 - TRANSPORTE  |    5 - NENHUM    |
-------------------------------------------------------------------------------------------
""")

    opcaoAlterar = int(input(">"))
    while 1 > opcaoAlterar or opcaoAlterar > 5:
        print()
        print("ERRO! Escolha uma opção válida (1 a 5):")
        opcaoAlterar = int(input(">"))
    print()

    if opcaoAlterar == 1:
        print(f"ALTERANDO O CONSUMO DE ÁGUA DO DIA {data}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ÁGUA (L):")
        consumo_agua = float(input("> "))
        DBalter_dia(data, "consumo_agua", consumo_agua, )

        print("\nCONSUMO DE ÁGUA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 2:
        print(f"ALTERANDO O CONSUMO DE ENERGIA DO DIA {data}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ENERGIA (KwH):")
        consumo_energia = float(input("> "))
        DBalter_dia(data, "consumo_energia", consumo_energia, )

        print("\nCONSUMO DE ENERGIA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 3:
        print(f"ALTERANDO A PORCENTAGEM DE RECICLAGEM DO DIA {data}")

        print("\nINSIRA SUA PORCENTAGEM ALTERADA DE RECICLAGEM (%):")
        porcentagem_reciclagem = int(input("> "))
        DBalter_dia(data, "porcentagem_reciclagem", porcentagem_reciclagem, )

        print("\nPORCENTAGEM DE RECICLAGEM ALTERADA COM SUCESSO!")

    elif opcaoAlterar == 4:
        print(f"ALTERANDO OS MEIOS DE TRANSPORTE UTILIZADOS NO DIA {data}")

        print('\nQUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (S/N)')

        meios_transporte = ['', '', '', '', '', '']
        meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
        meios_transporte[1] = input('BICICLETA: ').upper()
        meios_transporte[2] = input('CAMINHADA: ').upper()
        meios_transporte[3] = input('CARRO (Combustível fóssil): ').upper()
        meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
        meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()

        string_meios_transporte = ','.join(meios_transporte)
        DBalter_dia(data, "meios_transporte", string_meios_transporte, )

        print("\nMEIOS DE TRANSPORTE UTILIZADOS ALTERADOS COM SUCESSO!")

    else:
        print("NENHUMA ALTERAÇÃO FEITA")
        return
    #Alterando as classificações na tabela
    classificacao_aguaCript, classificacao_energiaCript,classificacao_reciclagemCript,classificacao_transporteCript = classificacaoDia(data)[0:4] #Novas classsificações
    DBalter_classificacao(data,classificacao_aguaCript, classificacao_energiaCript,classificacao_reciclagemCript,classificacao_transporteCript)
    mostrarClassificacao(data)

## EXCLUIR DIA

def telaExcluir():
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         EXCLUIR
-------------------------------------------------------------------------------------------
    """)
    tabela = DBselect()

    if len(tabela) == 0:
        print("ERRO! Insira alguma data no sistema")
        return
    print("DATAS JÁ INSERIDAS:")
    for x in tabela:
        print("- ",x[1])
    print("(Digite 0 para voltar para o menu)\n")
    print("INSIRA A DATA PARA EXCLUIR (DD/MM/AAAA): ")
    data = input(">")
    
    dataInvalida = True
    while dataInvalida == True:
        if data == "0":
            return
        for x in tabela:
            if x[1] == data:
                dataInvalida = False
                break
        if dataInvalida:
            print("\nERRO! Digite uma data já existente no sistema:\n")
            print("DATAS JÁ INSERIDAS:")
            for x in tabela:
                print("-",x[1])
            print("(OU digite 0 para voltar para o menu)")
            data = input(">")
    print()

    mostrarClassificacao(data)

    consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte = DBselect_dia(data)[2:6]
    meios_transporte = string_meios_transporte.split(",")

    print()
    print("-----------------------------------VALORES CADASTRADOS:------------------------------------")
    print()
    print(f"CONSUMO DE ÁGUA: {consumo_agua}")
    print(f"CONSUMO DE ENERGIA: {consumo_energia}")
    print(f"PORCENTAGEM DE RECICLAGEM: {porcentagem_reciclagem}%")
    print()
    print("MEIOS DE TRANSPORTE UTILIZADOS:")
    print(f"TRANSPORTE PÚBLICO {meios_transporte[0]}")
    print(f"BICICLETA: {meios_transporte[1]}")
    print(f"CAMINHADA: {meios_transporte[2]}")
    print(f"CARRO (combustível fóssil): {meios_transporte[3]}")
    print(f"CARRO ELÉTRICO: {meios_transporte[4]}")
    print(f"CARONA COMPARTILHADA (combustível fóssil): {meios_transporte[5]}")
    print()
    input("                                      <APERTE ENTER>")

    print(f"""
-------------------------------------------------------------------------------------------

                               TEM CERTEZA QUE DESEJA EXCLUIR?                                           
-------------------------------------------------------------------------------------------
|                   1 - SIM                   |                  2 - NÃO                  |
-------------------------------------------------------------------------------------------
""")
    try:
        opcaoExcluir = int(input(">"))
    except:
        opcaoExcluir = 0
    while opcaoExcluir < 1 or opcaoExcluir > 2:
        print()
        print("ERRO! Escolha uma opção válida:")
        opcaoExcluir = int(input(">"))
    print()
    if opcaoExcluir == 1:
        DBdelete(data)
        print(f"DIA EXCLUÍDO COM SUCESSO\n")
    else:
        print("VOLTANDO PARA A TELA DE MENU\n")

## MEDIAS

def caucularMediaDia(data):
    classificacao_aguaCript, classificacao_energiaCript, classificacao_reciclagemCript, classificacao_transporteCript = DBselect_classificacao_dia(data)[2:6]
    classificacao_agua = descriptografar(classificacao_aguaCript)
    classificacao_energia = descriptografar(classificacao_energiaCript)
    classificacao_reciclagem = descriptografar(classificacao_reciclagemCript)
    classificacao_transporte = descriptografar(classificacao_transporteCript)
    medias = [0,0,0,0]
    if classificacao_agua == "ALTA":
        medias[0] += 1
    elif classificacao_agua == "MODERADA":
        medias[0] += 0
    else:
        medias[0] -= 1
    if classificacao_energia == "ALTA":
        medias[1] += 1
    elif classificacao_energia == "MODERADA":
        medias[0] += 0
    else:
        medias[1] -= 1
    if classificacao_reciclagem == "ALTA":
        medias[2] += 1
    elif classificacao_reciclagem == "MODERADA":
        medias[0] += 0
    else:
        medias[2] -= 1
    if classificacao_transporte == "ALTA":
        medias[0] += 1
    elif classificacao_transporte == "MODERADA":
        medias[3] += 0
    else:
        medias[3] -= 1
    return medias

## CLASSIFICAR

def telaClassificar():
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                        CLASSIFICAR
-------------------------------------------------------------------------------------------
|    1 - DIA ESPECÍFICO      |     2 - LISTAR TODOS      |   3 - MÉDIA DE CLASSIFICACÃO   |
-------------------------------------------------------------------------------------------
""")

    tabela = DBselect()
    medias = [0, 0, 0, 0]
    if len(tabela) == 0:
        print("Nenhum dia para classificar")
        return
    
    opcaoClassificar = int(input(">"))
    while opcaoClassificar < 1 or opcaoClassificar > 3:
        print()
        print("ERRO! Escolha uma opção válida:")
        opcaoClassificar = int(input(">"))
    print()
    
    if opcaoClassificar == 1: #DIA ESPECÍFICO
        #INPUT + VALIDAÇÃO
        print("DATAS JÁ INSERIDAS:")
        for x in tabela:
            print("-",x[1])
        print("(Digite 0 para voltar para o menu)\n")
        print("INSIRA O DIA PARA CLASSIFICAR (DD/MM/AAAA): ")
        data = input(">")
        dataInvalida = True
        while dataInvalida == True:
            if data == "0":
                return
            for x in tabela:
                if x[1] == data:
                    dataInvalida = False
                    break
            if dataInvalida:
                print("\nERRO! Digite uma data já inserida no sistema:\n")
                print("DATAS JÁ INSERIDAS:")
                for x in tabela:
                    print("-",x[1])
                print("(OU digite 0 para voltar para o menu)")
                data = input(">")
        mostrarClassificacao(data)

    elif opcaoClassificar == 2: #LISTAR TODOS
        for x in tabela:
            mostrarClassificacao(x[1])
    else: #MÉDIA DA CLASSIFICAÇÃO
        for x in tabela:
            mediaDia = caucularMediaDia(x[1])
            medias = [medias[i] + mediaDia[i] for i in range(len(medias))]
        print()
        print("-------------------------------------------------------------------------------------------")
        print("                       MÉDIA DA CLASSIFICAÇÃO DE TODOS OS DIAS:")
        print("-------------------------------------------------------------------------------------------")
        print()
        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ÁGUA: ", end="")

        if medias[0] == len(tabela):
            print('ALTA SUSTENTABILIDADE.')
        elif medias[0] == -len(tabela):
            print('BAIXA SUSTENTABILIDADE.')
        else:
            print('MODERADA SUSTENTABILIDADE.')

        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ENERGIA: ", end="")

        if medias[1] == len(tabela):
            print('ALTA SUSTENTABILIDADE.')
        elif medias[1] == -len(tabela):
            print('BAIXA SUSTENTABILIDADE.')
        else:
            print('MODERADA SUSTENTABILIDADE.')

        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE RECICLAGEM: ", end="")

        if medias[2] == len(tabela):
            print('ALTA SUSTENTABILIDADE.')
        elif medias[2] == -len(tabela):
            print('BAIXA SUSTENTABILIDADE.')
        else:
            print('MODERADA SUSTENTABILIDADE.')

        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ", end="")

        if medias[3] == len(tabela):
            print('ALTA SUSTENTABILIDADE.')
        elif medias[3] == -len(tabela):
            print('BAIXA SUSTENTABILIDADE.')
        else:
            print('MODERADA SUSTENTABILIDADE.')