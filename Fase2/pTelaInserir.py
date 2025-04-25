def telaInserir():

    from conectBanco import DBinsert_dados,DBselect
    from pTelaClassificar import classificacaoDia

    #TELA INSERIR
    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                         INSERIR
-------------------------------------------------------------------------------------------
    """)
    #INSERINDO DADOS

    print("INSIRA A DATA DE HOJE (DD/MM/AAAA):")
    data = str(input("> "))
    print()

    dataValida = False
    while dataValida == False:
        for x in DBselect():
            if x[1] != data:
                dataValida = True
                break
        if dataValida == False:
            print("ERRO! Digite uma data ainda não inserida:")
            data = input(">")
    
    print("INSIRA SEUS DADOS DE CONSUMO DE ÁGUA (L):")
    consumo_agua = int(input("> "))
    print()

    print("INSIRA SEUS DADOS DE CONSUMO DE ENERGIA (KwH):")
    consumo_energia = int(input("> "))
    print()

    print("INSIRA A QUANTIDADE DE RESÍDUOS GERADOS (Kg):")
    input("> ")
    print()

    print("INSIRA A PORCENTAGEM DE RESÍDUOS RECICLADOS (%):")
    porcentagem_reciclagem = int(input("> "))
    print()

    print('QUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (SIM/NÃO)')
    meios_transporte = ['','','','','','']

    meios_transporte[0] = input('TRANSPORTE PÚBLICO: ').upper()
    meios_transporte[1] = input('BICICLETA: ').upper()
    meios_transporte[2] = input('CAMINHADA: ').upper()
    meios_transporte[3] = input('CARRO (Combustivel fóssil): ').upper()
    meios_transporte[4] = input('CARRO ELÉTRICO: ').upper()
    meios_transporte[5] = input('CARONA COMPARTILHADA (Combustível fóssil): ').upper()

    string_meios_transporte = ','.join(meios_transporte)

    #MOSTRANDO A CLASSIFICAÇÃO DIÁRIA
    
    classificacaoDia(data,consumo_agua,consumo_energia,porcentagem_reciclagem,meios_transporte)

    #INSERIR NO BANCO DE DADOS

    DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)
    
    input("\n <APERTE ENTER>")