def telaInserir():
    #TELA INSERIR
    print("""
    -------------------------------------------------------------------------------------------
    |                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
    -------------------------------------------------------------------------------------------

                                            INSERIR
    -------------------------------------------------------------------------------------------
    """)
    print()
    #INSERINDO DADOS

    print("INSIRA A DATA DE HOJE (DD/MM/AAAA):")
    data = str(input("> "))
    print()
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

    string_meios_transporte = "[" + ','.join(meios_transporte) + "]"

    #MOSTRANDO A CLASSIFICAÇÃO DIÁRIA

    print()
    print(f"    -----------------------CLASSIFICAÇÃO DA SUSTENTABILIDADE DO DIA {data}:------------------------")
    print()

    print("- CONSUMO DE ÁGUA: ",end="")

    # Classificação da sustentabilidade da água
    if consumo_agua < 150:
        print('Alta sustentabilidade.')
    elif 150 <= consumo_agua <= 200:
        print('Moderada sustentabilidade.')
    else:
        print('Baixa sustentabilidade.')

    print("- CONSUMO DE ENERGIA: ",end="")

    # Sustentabilidade no consumo de energia
    if consumo_energia < 5:
        print('Alta sustentabilidade.')
    elif 5 <= consumo_energia <= 10:
        print('Moderada sustentabilidade.')
    else:
        print('Baixa sustentabilidade.')

    print("- RECICLAGEM DE RESÍDUOS: ",end="")

    # Sustentabilidade na geração de resíduos recicláveis
    if porcentagem_reciclagem > 50:
        print('Alta sustentabilidade.')
    elif 20 <= porcentagem_reciclagem <= 50:
        print('Moderada sustentabilidade.')
    else:
        print('Baixa sustentabilidade.')

    print("- USO DE MEIOS DE TRANSPORTE: ",end="")

    # Sustentabilidade de meio de transporte
    if ((meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM')) and ((meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM')): 
    #Verifica se tem Alta sustentabilidade E Baxa Sustentabilidade = Moderada Sustentabilidade
        print('Moderada sustentabilidade.')
    elif (meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM'):
    #Verifica se tem Alta sustentabilidade
        print('Alta sustentabilidade.')
    elif (meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM'):
    #Verifica se tem Baixa sustentabilidade
        print('Baixa sustentabilidade.') 

    from conectBanco import DBinsert_dados

    #INSERIR NO BANCO DE DADOS

    DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)
