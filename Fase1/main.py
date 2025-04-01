#Fase 1 - Sistema de clssificação de sutentabilidade pessoal diário

#Tela de início
print("-------------------------------------------------------------")
print(" Sistema de classificação de sustentabilidade pessoal diário ")
print("-------------------------------------------------------------")
print()

# Entrada da data
data = input('Qual a data de hoje? ')

# Input dos consumos
consumo_agua = int(input('Quantos L de água você consumiu hoje?: '))
consumo_energia = float(input('Quantos KWh de energia elétrica você consumiu hoje? '))
geracao_residuos = float(input('Quantos KG de resíduos não recicláveis você gerou hoje? '))
residuos_reciclados = float(input('Qual sua porcentagem (%) de resíduos reciclados hoje? '))

print() #Pula uma linha

# Input dos transportes
print('Qual meio de transporte você usou hoje? (Responda com SIM ou NÃO)')
transporte_publico = input('Transporte público: ').upper()
bicicleta = input('Bicicleta: ').upper()
caminhada = input('Caminhada: ').upper()
carro = input('Carro (Combustivel fóssil): ').upper()
carro_eletrico = input('Carro elétrico: ').upper()
carona_compartilhada = input('Carona compartilhada (Combustível fóssil): ').upper()

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
if residuos_reciclados > 50:
    print('Alta sustentabilidade na geração de resíduos recicláveis.')
elif 20 <= residuos_reciclados <= 50:
    print('Moderada sustentabilidade na geração de resíduos recicláveis.')
else:
    print('Baixa sustentabilidade na geração de resíduos recicláveis.')

print("- ",end="")

# Sustentabilidade de meio de transporte
if ((bicicleta == 'SIM') or (transporte_publico == 'SIM') or (carro_eletrico == 'SIM') or (caminhada == 'SIM')) and ((carona_compartilhada == 'SIM') or (carro == 'SIM')): 
#Verifica se tem Alta sustentabilidade E Baxa Sustentabilidade = Moderada Sustentabilidade
    print('Moderada sustentabilidade para meio de transporte.')
elif (bicicleta == 'SIM') or (transporte_publico == 'SIM') or (caminhada == 'SIM') or (carro_eletrico == 'SIM'):
#Verifica se tem Alta sustentabilidade
    print('Alta sustentabilidade para meio de transporte.')
elif (carona_compartilhada == 'SIM') or (carro == 'SIM'):
#Verifica se tem Baixa sustentabilidade
    print('Baixa sustentabilidade para meio de transporte.')
