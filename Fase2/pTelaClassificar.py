def telaClassficar():

    from conectBanco import DBselect
    print("""
    -------------------------------------------------------------------------------------------
    |                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
    -------------------------------------------------------------------------------------------

                                        CLASSIFICAR
    -------------------------------------------------------------------------------------------
    """)

    myresult = DBselect()

    for x in myresult:
        data = x[1]
        consumo_agua = x[2]
        consumo_energia = x[3]
        porcentagem_reciclagem = x[4]
        string_meio_transporte = x[5]
        meios_transporte = string_meio_transporte.split(",")
        print()
        print(f"                                       DIA {data}")
        print()
        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ÁGUA: ",end="")
    
        if consumo_agua < 150:
            print('Alta sustentabilidade')
        elif 150 <= consumo_agua <= 200:
            print('Moderada sustentabilidade.')
        else:
            print('Baixa sustentabilidade.')

        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ENERGIA: ",end="")
    
        if consumo_energia < 5:
            print('Alta sustentabilidade.')
        elif 5 <= consumo_energia <= 10:
            print('Moderada sustentabilidade.')
        else:
            print('Baixa sustentabilidade.')

        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE RECICLAGEM: ",end="")
    
        if porcentagem_reciclagem > 50:
            print('Alta sustentabilidade.')
        elif 20 <= porcentagem_reciclagem <= 50:
            print('Moderada sustentabilidade.')
        else:
            print('Baixa sustentabilidades.')

        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ",end="")
    
        if ((meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM')) and ((meios_transporte[5] == 'SIM') or (meios_transporte[3] =='SIM')): 
            print('Moderada sustentabilidade.')
        elif (meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM'):
            print('Alta sustentabilidade.')
        elif (meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM'):
            print('Baixa sustentabilidade.')

    print()

    print("                       MÉDIA DA CLASSIFICAÇÃO DE TODOS OS DIAS:")
    print()
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ÁGUA: ")
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ENERGIA: ")
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE RECICLAGEM: ")
    print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ")

    input("<aperte enter>")