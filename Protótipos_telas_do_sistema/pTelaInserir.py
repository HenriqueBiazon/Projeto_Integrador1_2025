print("""
-------------------------------------------------------------------------------------------
|                        MONITORAMENTO DE SUSTENTABILIDADE PESSOAL                        |
-------------------------------------------------------------------------------------------

                                        INSERIR
-------------------------------------------------------------------------------------------
""")
print("INSIRA A DATA DE HOJE:")
input("> ")
print("INSIRA SEUS DADOS DE CONSUMO DE ÁGUA (L):")
input("> ")
print("INSIRA SEUS DADOS DE CONSUMO DE ENERGIA (KwH):")
input("> ")
print("INSIRA QUANTOS DE RESÍDUOS GERADOS (Kg):")
input("> ")
print("INSIRA A PORCENTAGEM DE RESÍDUOS RECICLADOS (%):")
input("> ")
print('QUAIS MEIOS DE TRANSPORTE VOCÊ USOU HOJE? (SIM/NÃO)')

meiosTransporte = ['','','','','','']
meiosTransporte[0] = input('Transporte público: ').upper()
meiosTransporte[1] = input('Bicicleta: ').upper()
meiosTransporte[2] = input('Caminhada: ').upper()
meiosTransporte[3] = input('Carro (Combustivel fóssil): ').upper()
meiosTransporte[4] = input('Carro elétrico: ').upper()
meiosTransporte[5] = input('Carona compartilhada (Combustível fóssil): ').upper()