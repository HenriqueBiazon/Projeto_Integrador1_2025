import os
from conectBanco import (
    DBinsert_dados,
    DBselect,
    DBselect_dia,
    DBalter_dia,
    DBdelete_dia,
    DBselect_usuario,
    DBinsert_usuario,
    DBselect_tabela_usuarios
)
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

def classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte):
    medias = [0, 0, 0, 0]

    print()
    print(f"                    CLASSIFICAÇÃO DA SUSTENTABILIDADE DO DIA {data}:                     ")
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

    if ((meios_transporte[1] == 'S') or (meios_transporte[0] == 'S') or (meios_transporte[4] == 'S') or (meios_transporte[2] == 's')) and ((meios_transporte[5] == 'S') or (meios_transporte[3] == 'S')):
        print('Moderada sustentabilidade.')

    elif (meios_transporte[5] == 'S') or (meios_transporte[3] == 'S'):
        print('Baixa sustentabilidade.')
        medias[3] -= 1
    else:
        print('Alta sustentabilidade.')
        medias[3] += 1

    return medias

## INSERIR DIA

def telaInserir(Id_usuario):
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
        tabela = DBselect(Id_usuario)
        if data == "0":
            return
        if len(tabela) == 0:
            dataInvalida = False
        for x in tabela:
            x = list(x)
            x[1] = descriptografar(x[1])
            if x[1] == data:
                dataInvalida = True
                break
            else:
                dataInvalida = False
        if dataInvalida:
            print("\nERRO! Digite uma data válida:\n")
            print("DATAS JÁ INSERIDAS:")
            for x in tabela:
                x = list(x)
                x[1] = descriptografar(x[1])
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
    string_meios_transporte = ','.join(meios_transporte)

    classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte)
    data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte = criptografar(data), criptografar(consumo_agua), criptografar(consumo_energia), criptografar(porcentagem_reciclagem), criptografar(string_meios_transporte)
    DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte, Id_usuario)

## ALTERAR DIA

def telaAlterar(Id_usuario):
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         ALTERAR
-------------------------------------------------------------------------------------------
    """)
    tabela = DBselect(Id_usuario)

    if len(tabela) == 0:
        print("ERRO! Insira alguma data no sistema")
        return
    
    print("DATAS JÁ INSERIDAS:")
    for x in tabela:
        x = list(x)
        x[1] = descriptografar(x[1])
        print("-",x[1])
    print("(Digite 0 para voltar para o menu)\n")
    print("INSIRA A DATA PARA ALTERAR (DD/MM/AAAA): ")
    data = input(">")

    dataInvalida = True
    while dataInvalida == True:
        if data == "0":
            return
        for x in tabela:
            x = list(x)
            x[1] = descriptografar(x[1])
            if x[1] == data:
                dataInvalida = False
                break
        if dataInvalida:
            print("\nERRO! Digite uma data já inserida no sistema:\n")
            print("DATAS JÁ INSERIDAS:")
            for x in tabela:
                x = list(x)
                x[1] = descriptografar(x[1])
                print("-",x[1])
            print("(OU digite 0 para voltar para o menu)")
            data = input(">")
    print()
    data = criptografar(data)
    diaSelecionado = DBselect_dia(data,Id_usuario)
    diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5] = descriptografar(diaSelecionado[1]), descriptografar(diaSelecionado[2]), descriptografar(diaSelecionado[3]), descriptografar(diaSelecionado[4]), descriptografar(diaSelecionado[5])
    diaSelecionado[5] = diaSelecionado[5].split(",")
    
    classificacaoDia(diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5])

    print()
    print("-----------------------------------VALORES CADASTRADOS:------------------------------------")
    print()
    print(f"CONSUMO DE ÁGUA: {diaSelecionado[2]}")
    print(f"CONSUMO DE ENERGIA: {diaSelecionado[3]}")
    print(f"PORCENTAGEM DE RECICLAGEM: {diaSelecionado[4]}%")
    print()
    print("MEIOS DE TRANSPORTE UTILIZADOS:")
    print(f"TRANSPORTE PÚBLICO {diaSelecionado[5][0]}")
    print(f"BICICLETA: {diaSelecionado[5][1]}")
    print(f"CAMINHADA: {diaSelecionado[5][2]}")
    print(f"CARRO (combustível fóssil): {diaSelecionado[5][3]}")
    print(f"CARRO ELÉTRICO: {diaSelecionado[5][4]}")
    print(f"CARONA COMPARTILHADA (combustível fóssil): {diaSelecionado[5][5]}")
    print()
    input("                                    <APERTE ENTER>")
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
        print(f"ALTERANDO O CONSUMO DE ÁGUA DO DIA {diaSelecionado[1]}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ÁGUA (L):")
        consumo_agua = float(input("> "))
        consumo_agua = criptografar(consumo_agua)
        DBalter_dia(data, "consumo_agua", consumo_agua, Id_usuario)

        print("\nCONSUMO DE ÁGUA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 2:
        print(f"ALTERANDO O CONSUMO DE ENERGIA DO DIA {diaSelecionado[1]}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ENERGIA (KwH):")
        consumo_energia = float(input("> "))
        consumo_energia = criptografar(consumo_energia)
        DBalter_dia(data, "consumo_energia", consumo_energia, Id_usuario)

        print("\nCONSUMO DE ENERGIA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 3:
        print(f"ALTERANDO A PORCENTAGEM DE RECICLAGEM DO DIA {diaSelecionado[1]}")

        print("\nINSIRA SUA PORCENTAGEM ALTERADA DE RECICLAGEM (%):")
        porcentagem_reciclagem = int(input("> "))
        porcentagem_reciclagem = criptografar(porcentagem_reciclagem)
        DBalter_dia(data, "porcentagem_reciclagem", porcentagem_reciclagem, Id_usuario)

        print("\nPORCENTAGEM DE RECICLAGEM ALTERADA COM SUCESSO!")

    elif opcaoAlterar == 4:
        print(f"ALTERANDO OS MEIOS DE TRANSPORTE UTILIZADOS NO DIA {diaSelecionado[1]}")

        print('\nQUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (S/N)')

        meios_transporte = ['', '', '', '', '', '']
        meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
        meios_transporte[1] = input('BICICLETA: ').upper()
        meios_transporte[2] = input('CAMINHADA: ').upper()
        meios_transporte[3] = input('CARRO (Combustível fóssil): ').upper()
        meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
        meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()

        string_meios_transporte = ','.join(meios_transporte)
        string_meios_transporte = criptografar(string_meios_transporte)
        DBalter_dia(data, "meios_transporte", string_meios_transporte, Id_usuario)

        print("\nMEIOS DE TRANSPORTE UTILIZADOS ALTERADOS COM SUCESSO!")

    else:
        print("NENHUMA ALTERAÇÃO FEITA")
        return

    diaSelecionado = DBselect_dia(data, Id_usuario)
    diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5] = descriptografar(diaSelecionado[1]), descriptografar(diaSelecionado[2]), descriptografar(diaSelecionado[3]), descriptografar(diaSelecionado[4]), descriptografar(diaSelecionado[5])
    diaSelecionado[5] = diaSelecionado[5].split(",")
    classificacaoDia(diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5])

## EXCLUIR DIA

def telaExcluir(Id_usuario):
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         EXCLUIR
-------------------------------------------------------------------------------------------
    """)
    tabela = DBselect(Id_usuario)

    if len(tabela) == 0:
        print("ERRO! Insira alguma data no sistema")
        return
    print("DATAS JÁ INSERIDAS:")
    for x in tabela:
        x = list(x)
        x[1] = descriptografar(x[1])
        print("- ",x[1])
    print("(Digite 0 para voltar para o menu)\n")
    print("INSIRA A DATA PARA EXCLUIR (DD/MM/AAAA): ")
    data = input(">")
    
    dataInvalida = True
    while dataInvalida == True:
        if data == "0":
            return
        for x in tabela:
            x = list(x)
            x[1] = descriptografar(x[1])
            if x[1] == data:
                dataInvalida = True
                break
        if not dataInvalida:
            print("\nERRO! Digite uma data já existente no sistema:\n")
            print("DATAS JÁ INSERIDAS:")
            for x in tabela:
                x = list(x)
                x[1] = descriptografar(x[1])
                print("-",x[1])
            print("(OU digite 0 para voltar para o menu)")
            data = input(">")
    print()
    data = criptografar(data)
    diaSelecionado = DBselect_dia(data, Id_usuario)

    diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5] = descriptografar(diaSelecionado[1]), descriptografar(diaSelecionado[2]), descriptografar(diaSelecionado[3]), descriptografar(diaSelecionado[4]), descriptografar(diaSelecionado[5])
    diaSelecionado[5] = diaSelecionado[5].split(",")

    classificacaoDia(diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5])

    print()
    print("-----------------------------------VALORES CADASTRADOS:------------------------------------")
    print()
    print(f"CONSUMO DE ÁGUA: {diaSelecionado[2]}")
    print(f"CONSUMO DE ENERGIA: {diaSelecionado[3]}")
    print(f"PORCENTAGEM DE RECICLAGEM: {diaSelecionado[4]}%")
    print()
    print("MEIOS DE TRANSPORTE UTILIZADOS:")
    print(f"TRANSPORTE PÚBLICO {diaSelecionado[5][0]}")
    print(f"BICICLETA: {diaSelecionado[5][1]}")
    print(f"CAMINHADA: {diaSelecionado[5][2]}")
    print(f"CARRO (combustível fóssil): {diaSelecionado[5][3]}")
    print(f"CARRO ELÉTRICO: {diaSelecionado[5][4]}")
    print(f"CARONA COMPARTILHADA (combustível fóssil): {diaSelecionado[5][5]}")
    print()
    input("                                      <APERTE ENTER>")
    print()

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
        DBdelete_dia(data, Id_usuario)
        print(f"DIA EXCLUÍDO COM SUCESSO\n")
    else:
        print("VOLTANDO PARA A TELA DE MENU\n")

## CLASSIFICAR DIA

def telaClassificar(Id_usuario):
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                        CLASSIFICAR
-------------------------------------------------------------------------------------------
|    1 - DIA ESPECÍFICO      |     2 - LISTAR TODOS      |   3 - MÉDIA DE CLASSIFICACÃO   |
-------------------------------------------------------------------------------------------
""")

    tabela = DBselect(Id_usuario)
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

    if opcaoClassificar == 1:

        print("DATAS JÁ INSERIDAS:")
        for x in tabela:
            x = list(x)
            x[1] = descriptografar(x[1])
            print("-",x[1])
        print("(Digite 0 para voltar para o menu)\n")
        print("INSIRA O DIA PARA CLASSIFICAR (DD/MM/AAAA): ")
        data = input(">")
        dataValida = False
        while dataValida == False:
            if data == "0":
                return
            for x in tabela:
                x = list(x)
                x[1] = descriptografar(x[1])
                if x[1] == data:
                    dataValida = True
                    break
            if not dataValida:
                print("\nERRO! Digite uma data já inserida no sistema:\n")
                print("DATAS JÁ INSERIDAS:")
                for x in tabela:
                    x = list(x)
                    x[1] = descriptografar(x[1])
                    print("-",x[1])
                print("(OU digite 0 para voltar para o menu)")
                data = input(">")
        data = criptografar(data)
        diaSelecionado = DBselect_dia(data,Id_usuario)
        diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5] = descriptografar(diaSelecionado[1]), descriptografar(diaSelecionado[2]), descriptografar(diaSelecionado[3]), descriptografar(diaSelecionado[4]), descriptografar(diaSelecionado[5])
        diaSelecionado[5] = diaSelecionado[5].split(",")
        classificacaoDia(diaSelecionado[1], diaSelecionado[2], diaSelecionado[3], diaSelecionado[4], diaSelecionado[5])

    elif opcaoClassificar == 2:
        for x in tabela:
            data = descriptografar(x[1])
            consumo_agua = descriptografar(x[2])
            consumo_energia = descriptografar(x[3])
            porcentagem_reciclagem = descriptografar(x[4])
            string_meio_transporte = descriptografar(x[5])
            meios_transporte = string_meio_transporte.split(",")
            classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte)
    else:
        for x in tabela:
            data = descriptografar(x[1])
            consumo_agua = descriptografar(x[2])
            consumo_energia = descriptografar(x[3])
            porcentagem_reciclagem = descriptografar(x[4])
            string_meio_transporte = descriptografar(x[5])
            meios_transporte = string_meio_transporte.split(",")
            mediaDia = classificacaoDia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte)
            medias = [medias[i] + mediaDia[i] for i in range(len(medias))]
        apagarTerminal()
        print()
        print("-------------------------------------------------------------------------------------------")
        print("                       MÉDIA DA CLASSIFICAÇÃO DE TODOS OS DIAS:")
        print("-------------------------------------------------------------------------------------------")
        print()
        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ÁGUA: ", end="")

        if medias[0] == len(tabela):
            print('Alta sustentabilidade')
        elif medias[0] == -len(tabela):
            print('Baixa sustentabilidade.')
        else:
            print('Moderada sustentabilidade.')

        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ENERGIA: ", end="")

        if medias[1] == len(tabela):
            print('Alta sustentabilidade')
        elif medias[1] == -len(tabela):
            print('Baixa sustentabilidade.')
        else:
            print('Moderada sustentabilidade.')

        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE RECICLAGEM: ", end="")

        if medias[2] == len(tabela):
            print('Alta sustentabilidade')
        elif medias[2] == -len(tabela):
            print('Baixa sustentabilidade.')
        else:
            print('Moderada sustentabilidade.')

        print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ", end="")

        if medias[3] == len(tabela):
            print('Alta sustentabilidade')
        elif medias[3] == -len(tabela):
            print('Baixa sustentabilidade.')
        else:
            print('Moderada sustentabilidade.')        

def telaLogin():
    login = False
    while login == False:
        print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------

                                            LOG-IN                                           
-------------------------------------------------------------------------------------------
|                1 - CADASTRAR                 |                2 - ENTRAR                |
-------------------------------------------------------------------------------------------""")
        try:
            opcaoLogin = int(input(">"))
        except:
            opcaoLogin = 0
        while opcaoLogin != 1 and opcaoLogin != 2:
            print()
            print("ERRO! Escolha uma opção válida (1 ou 2):")
            try:
                opcaoLogin = int(input(">"))
            except:
                opcaoLogin = 0

        if opcaoLogin == 2:
            print("\n                                         ENTRANDO:\n")
            nome = input("INSIRA O SEU NOME: ")
            senha = input("INSIRA SUA SENHA: ")
            try:
                usuario = DBselect_usuario(nome,senha)
                Id_usuario = usuario[0]
                print("Você fez log-in na sua conta!")
                input("                                      <APERTE ENTER>")
                login = True
            except:
                print("ERRO! O usuário e/ou a senha estão incorretos")
                input("                                      <APERTE ENTER>")
        else:
            print("\n                                         CADASTRO:\n")
            nome = input("INSIRA O SEU NOME: ")
            senha = input("INSIRA SUA SENHA: ")
            try:
                tabela = DBselect_tabela_usuarios()
                Invalido = False
                for x in tabela:
                    if nome == x[1]:
                        print("ERRO! Nome de usuário já cadastrado")
                        Invalido = True
                if Invalido == False:
                    DBinsert_usuario(nome,senha)
                    print("Usuário cadastrado com sucesso!")
                    input("                                      <APERTE ENTER>")
            except:
                print("ERRO! Não foi possível cadastrar o usuário")
                input("                                      <APERTE ENTER>")
        apagarTerminal()
    return Id_usuario