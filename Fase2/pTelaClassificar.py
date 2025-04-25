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

    #TRANSFORMAR VARIAVEIS MEDIA EM UMA LISTA
    media_agua = 0
    media_energia = 0
    media_reciclagem = 0
    media_trasporte = 0

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
            media_agua += 1
        elif 150 <= consumo_agua <= 200:
            print('Moderada sustentabilidade.')
        else:
            print('Baixa sustentabilidade.')
            media_agua -= 1

        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ENERGIA: ",end="")
    
        if consumo_energia < 5:
            print('Alta sustentabilidade.')
            media_energia += 1
        elif 5 <= consumo_energia <= 10:
            print('Moderada sustentabilidade.')
        else:
            print('Baixa sustentabilidade.')
            media_energia -= 1

        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE RECICLAGEM: ",end="")
    
        if porcentagem_reciclagem > 50:
            print('Alta sustentabilidade.')
            media_reciclagem += 1
        elif 20 <= porcentagem_reciclagem <= 50:
            print('Moderada sustentabilidade.')
        else:
            print('Baixa sustentabilidades.')
            media_reciclagem -= 1

        print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ",end="")
    
        if ((meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM')) and ((meios_transporte[5] == 'SIM') or (meios_transporte[3] =='SIM')): 
            print('Moderada sustentabilidade.')
        elif (meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM'):
            print('Alta sustentabilidade.')
            media_trasporte += 1
        elif (meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM'):
            print('Baixa sustentabilidade.')
            media_trasporte -=1

    print()

    print("                       MÉDIA DA CLASSIFICAÇÃO DE TODOS OS DIAS:")
    print()
    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ÁGUA: ",end="")

    if media_agua == len(myresult):
        print('Alta sustentabilidade')
    elif media_agua == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')
    
    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ENERGIA: ",end="")

    if media_energia == len(myresult):
        print('Alta sustentabilidade')
    elif media_energia == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE RECICLAGEM: ",end="")

    if media_reciclagem == len(myresult):
        print('Alta sustentabilidade')
    elif media_reciclagem == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ",end="")

    if media_trasporte == len(myresult):
        print('Alta sustentabilidade')
    elif media_trasporte == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    input("\n                                    <APERTE ENTER>")
telaClassficar()