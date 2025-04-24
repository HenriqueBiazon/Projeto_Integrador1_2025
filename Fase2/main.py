#Fase 2 - Implementação do banco de dados

from conectBanco import DBconnect
from pTelaMenu import telaMenu

#Fase 1 - Sistema de clssificação de sutentabilidade pessoal diário

#Tela de início

telaMenu()

#TESTE PARA SELECIONAR NO MYSQL



# Entrada da data
data = input('Qual a data de hoje? ')


# Input dos consumos
consumo_agua = int(input('Quantos L de água você consumiu hoje?: '))
consumo_energia = float(input('Quantos KWh de energia elétrica você consumiu hoje? '))
geracao_residuos = float(input('Quantos KG de resíduos não recicláveis você gerou hoje? '))
porcentagem_reciclagem = float(input('Qual sua porcentagem (%) de resíduos reciclados hoje? '))

print() #Pula uma linha

# Input dos transportes
print('Qual meio de transporte você usou hoje? (Responda com SIM ou NÃO)')

meiosTransporte = ['','','','','','']
meiosTransporte[0] = input('Transporte público: ').upper()
meiosTransporte[1] = input('Bicicleta: ').upper()
meiosTransporte[2] = input('Caminhada: ').upper()
meiosTransporte[3] = input('Carro (Combustivel fóssil): ').upper()
meiosTransporte[4] = input('Carro elétrico: ').upper()
meiosTransporte[5] = input('Carona compartilhada (Combustível fóssil): ').upper()

# Apresentar resultados + Classificação de sustentabilidade
print()
print(f"Classificação da sustentabilidade do dia {data}:")
print()

print("- ",end="") #Começa cada linha com um -, e depois escreve a classificação

# Classificação da sustentabilidade da água
if consumo_agua < 150:
    print('Alta sustentabilidade no consumo de água diário.')
elif 150 <= consumo_agua <= 200:
    print('Moderada sustentabilidade no consumo de água diário.')
else:
    print('Baixa sustentabilidade no consumo de água diário.')

print("- ",end="")

# Sustentabilidade no consumo de energia
if consumo_energia < 5:
    print('Alta sustentabilidade no consumo de energia.')
elif 5 <= consumo_energia <= 10:
    print('Moderada sustentabilidade no consumo de energia.')
else:
    print('Baixa sustentabilidade no consumo de energia.')

print("- ",end="")

# Sustentabilidade na geração de resíduos recicláveis
if porcentagem_reciclagem > 50:
    print('Alta sustentabilidade na geração de resíduos recicláveis.')
elif 20 <= porcentagem_reciclagem <= 50:
    print('Moderada sustentabilidade na geração de resíduos recicláveis.')
else:
    print('Baixa sustentabilidade na geração de resíduos recicláveis.')

print("- ",end="")

# Sustentabilidade de meio de transporte
if ((meiosTransporte[1] == 'SIM') or (meiosTransporte[0] == 'SIM') or (meiosTransporte[4] == 'SIM') or (meiosTransporte[2] == 'SIM')) and ((meiosTransporte[5] == 'SIM') or (meiosTransporte[3] == 'SIM')): 
#Verifica se tem Alta sustentabilidade E Baxa Sustentabilidade = Moderada Sustentabilidade
    print('Moderada sustentabilidade para meio de transporte.')
elif (meiosTransporte[1] == 'SIM') or (meiosTransporte[0] == 'SIM') or (meiosTransporte[4] == 'SIM') or (meiosTransporte[2] == 'SIM'):
#Verifica se tem Alta sustentabilidade
    print('Alta sustentabilidade para meio de transporte.')
elif (meiosTransporte[5] == 'SIM') or (meiosTransporte[3] == 'SIM'):
#Verifica se tem Baixa sustentabilidade
    print('Baixa sustentabilidade para meio de transporte.')

string_meiosTransporte = ','.join(meiosTransporte)
print(string_meiosTransporte)

def DBselect():
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = "SELECT * FROM dados_sustentabilidade"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


def DBinsert():
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = "INSERT INTO dados_sustentabilidade (consumo_agua, consumo_energia, porcentagem_reciclagem, meio_transporte) VALUES (%s,%s,%s,%s)"
    values = (consumo_agua,consumo_energia,porcentagem_reciclagem,string_meiosTransporte)
    cursor.execute(sql,values)
    mydb.commit()

    print(cursor.rowcount, "INSERTED")

DBinsert()
DBselect()