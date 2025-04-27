def telaAlterar():

    from conectBanco import DBselect,DBselect_dia,DBalter_dia
    from pTelaClassificar import classificacaoDia

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
    while dataValida == False:
        for x in DBselect():
            if x[1] == data:
                
                dataValida = True
                break
        if dataValida == False:
            print("ERRO! Digite uma data já inserida:\n(Digite 0 para voltar para o menu)")
            data = input(">")
            if data == 0:
                return

    myresult = DBselect_dia(data)
    myresult[5] = myresult[5].split(",")

    #MOSTRAR CLASSIFICAÇÃO

    classificacaoDia(myresult[1],myresult[2],myresult[3],myresult[4],myresult[5])

    #MOSTRAR VALORES
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
        DBalter_dia(data,"consumo_agua",consumo_agua)

        print("\nCONSUMO DE ÁGUA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 2:
        print(f"ALTERANDO O CONSUMO DE ENERGIA DO DIA {data}")

        print("\nINSIRA SEU DADO ALTERADO DE CONSUMO DE ENERGIA (KwH):")
        consumo_energia = int(input("> "))
        DBalter_dia(data,"consumo_energia",consumo_energia)

        print("\nCONSUMO DE ENERGIA ALTERADO COM SUCESSO!")

    elif opcaoAlterar == 3:
        print(f"ALTERANDO A PORCENTAGEM DE RECICLAGEM DO DIA {data}")

        print("\nINSIRA SUA PORCENTAGEM ALTERADA DE RECICLAGEM (%):")
        porcentagem_reciclagem = int(input("> "))
        DBalter_dia(data,"porcentagem_reciclagem",porcentagem_reciclagem)

        print("\nPORCENTAGEM DE RECICLAGEM ALTERADA COM SUCESSO!")

    elif opcaoAlterar == 4:
        print(f"ALTERANDO OS MEIOS DE TRANSPORTE UTILIZADOS NO DIA {data}")

        print('\nQUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (SIM/NÃO)')

        meios_transporte = ['','','','','','']
        meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
        meios_transporte[1] = input('BICICLETA: ').upper()
        meios_transporte[2] = input('CAMINHADA: ').upper()
        meios_transporte[3] = input('CARRO (Combustivel fóssil): ').upper()
        meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
        meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()

        string_meios_transporte = ','.join(meios_transporte)

        DBalter_dia(data,"meios_transporte",string_meios_transporte)

        print("\nMEIOS DE TRANSPORTE UTILIZADOS ALTERADOS COM SUCESSO!")

    else:

        print("NENHUMA ALTERAÇÃO FEITA")
        return
    
    myresult = DBselect_dia(data)
    myresult[5] = myresult[5].split(",")

    classificacaoDia(myresult[1],myresult[2],myresult[3],myresult[4],myresult[5]) #PRINTA A NOVA CLASSIFICAÇÃO

    input("\n                                    <APERTE ENTER>")

