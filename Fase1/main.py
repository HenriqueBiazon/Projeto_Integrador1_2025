D = str(input('Qual a data de hoje? '))
A = int(input('Quanto de agua voce consumiu hoje(aproximadamente em litros)?: '))
E = float(input('Quantos KWh de energia eletrica voce consumiu hoje? '))
R = float(input('Quantos kg de residuos nao reciclaveis voce gerou hoje? '))
RR = float(input('Qual sua porcentagem de residuos reciclaveis hoje? '))
print('Qual meio de transporte voce usou hoje?(responda com sim ou nao) ')
Tp = str(input('transporte publico: '))
B = str(input('Bicicleta: '))
C = str(input('caminhada: '))
Ca = str(input('Carro: '))
Ce = str(input('Carro eletrico: '))
Cc = str(input('Carona compartilhada: '))
if ((B == 'sim') or (Tp == 'sim') or (C == 'sim') or (Ce == 'sim')) and ((Ca == 'sim') or (Cc == 'sim')):
    print ('Sustentabilidade moderada para meio de transporte')
elif (B == 'sim') or (Tp == 'sim') or (C == 'sim') or (Ce == 'sim'):
    print('Alta sustentabilidade para meio de transporte')
elif (Ca == 'sim') or (Cc == 'sim'):
    print('baixa sustentabilidade para meio de transporte')
# verificacao da sustentabilidade da agua
if A < 150:
    print('alta sustentabilidade no consumo de agua diario')
elif 150 <= A <= 200:
    print('moderado sustentabilidade no consumo de agua diario')
elif A > 200:
    print('baixo sustentabilidade no consumo de agua diario')
#sustentabilidade no consumo de energia
if E < 5:
    print('alta sustentabilidade no consumo de energia')
elif 5 <= E <= 10:
    print('moderado sustentabilidade no consumo de energia')
elif E > 10:
    print('baixo sustentabilidade no consumo de energia')
#sustentabilidade na geracao de residuos reciclaveis
if RR > 50:
    print('alta sustentabilidade na geracao de residuos reciclaveis')
elif 20 <= RR <= 50:
    print('moderado sustentabilidade na geracao de residuos reciclaveis')
elif RR < 20:
    print('baixo sustentabilidade na geracao de residuos reciclaveis')
    