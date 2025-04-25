def telaAlterar():

    from conectBanco import DBselect,DBselect_dia,DBalter_dia
    from pTelaInserir import telaInserir
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
            print("ERRO! Digite uma data já inserida:\n(Digite 0 para inserir um novo dia)")
            data = input(">")
            if data == 0:
                telaInserir()

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
        print()
        print("INSIRA SEU DADO ALTERADO DE CONSUMO DE ÁGUA (L):")
        consumo_agua = int(input("> "))
        DBalter_dia(data,"consumo_agua",consumo_agua)
        print("ALTERADO COM SUCESSO!")
        classificacaoDia(myresult[1],consumo_agua,myresult[3],myresult[4],myresult[5])
   

    

telaAlterar()

