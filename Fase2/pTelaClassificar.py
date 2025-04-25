def classificacaoDia(data,consumo_agua,consumo_energia,porcentagem_reciclagem,meios_transporte):
                
                medias = [0,0,0,0]

                print()
                print(f"-------------------CLASSIFICAÇÃO DA SUSTENTABILIDADE DO DIA {data}:--------------------")
                print()
                print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ÁGUA: ",end="")
                
                if consumo_agua < 150:
                    print('Alta sustentabilidade')
                    medias[0] += 1
                elif 150 <= consumo_agua <= 200:
                    print('Moderada sustentabilidade.')
                else:
                    print('Baixa sustentabilidade.')
                    medias[0] -= 1

                print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE ENERGIA: ",end="")
            
                if consumo_energia < 5:
                    print('Alta sustentabilidade.')
                    medias[1] += 1
                elif 5 <= consumo_energia <= 10:
                    print('Moderada sustentabilidade.')
                else:
                    print('Baixa sustentabilidade.')
                    medias[1] -= 1

                print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE RECICLAGEM: ",end="")
            
                if porcentagem_reciclagem > 50:
                    print('Alta sustentabilidade.')
                    medias[2] += 1
                elif 20 <= porcentagem_reciclagem <= 50:
                    print('Moderada sustentabilidade.')
                else:
                    print('Baixa sustentabilidades.')
                    medias[2] -= 1

                print(f"CLASSIFICAÇÃO DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ",end="")
            
                if ((meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM')) and ((meios_transporte[5] == 'SIM') or (meios_transporte[3] =='SIM')): 
                    print('Moderada sustentabilidade.')
                elif (meios_transporte[5] == 'SIM') or (meios_transporte[3] == 'SIM'):
                    print('Baixa sustentabilidade.')
                    medias[3] -=1
                #elif (meios_transporte[1] == 'SIM') or (meios_transporte[0] == 'SIM') or (meios_transporte[4] == 'SIM') or (meios_transporte[2] == 'SIM'):
                else:
                    print('Alta sustentabilidade.')
                    medias[3] += 1
                return medias

def telaClassificar():

    from conectBanco import DBselect

    print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------
          
                                        CLASSIFICAR
-------------------------------------------------------------------------------------------""")

    myresult = DBselect()
    
    for x in myresult:
        data = x[1]
        consumo_agua = x[2]
        consumo_energia = x[3]
        porcentagem_reciclagem = x[4]
        string_meio_transporte = x[5]
        meios_transporte = string_meio_transporte.split(",")

        medias += classificacaoDia(data,consumo_agua,consumo_energia,porcentagem_reciclagem,meios_transporte)

    print()
    print("                       MÉDIA DA CLASSIFICAÇÃO DE TODOS OS DIAS:")
    print()
    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ÁGUA: ",end="")

    if medias[0] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[0] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')
    
    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE ENERGIA: ",end="")

    if medias[1] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[1] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE RECICLAGEM: ",end="")

    if medias[2] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[2] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    print(f"CLASSIFICAÇÃO MÉDIA DE SUSTENTABILIDADE DE MEIO DE TRANSPORTE: ",end="")

    if medias[3] == len(myresult):
        print('Alta sustentabilidade')
    elif medias[3] == -len(myresult):
        print('Baixa sustentabilidade.')
    else:
        print('Moderada sustentabilidade.')

    input("\n                                    <APERTE ENTER>")