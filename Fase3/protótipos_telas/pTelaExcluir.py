def telaExcluir():

    from conectBanco import DBselect,DBselect_dia,DBdelete_dia
    from pTelaClassificar import classificacaoDia


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
    print()

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
    print(f"""
-------------------------------------------------------------------------------------------

                        TEM CERTEZA QUE DESEJA EXLUIR O DIA {data}                                           
-------------------------------------------------------------------------------------------
|                   1 - SIM                   |                  2 - NÃO                  |
-------------------------------------------------------------------------------------------
""")
    opcaoExcluir = int(input(">"))
    
    while 1 > opcaoExcluir > 2:
        print()
        print("ERRO! Escolha uma opção válida:")
        opcaoExcluir = input(">")
    print()
    if opcaoExcluir == 1:
        DBdelete_dia(data)
        print(f"DIA {data} EXCLUÍDO COM SUCESSO\n")
    else:
        print("VOLTANDO PARA A TELA DE MENU\n")
    input("                                    <APERTE ENTER>")