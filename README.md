# Projeto-integrador 01

--Projeto Integrador do primeiro semestre do curso de Engenharia de Software na PUC Campinas 2025--

*Integrantes do grupo:* Daniel Neves Papa, Gabriel Diniz Foresti Mian de Almeida, Henrique Biazon Ferreira, João Pedro Panza Mainieri, Lucas do Prado Bezerra e Thiago Gutieri Conte 

*O Projeto:* Consiste em um sistema feito em python para classificar e monitorar a sustentabilidade diária de uma pessoa, de acordo com os dados inseridos pelo usuário. O sistema tem como intuito facilitar o início da implementação da sustentabilidade na vida das pessoas, fazendo com que seja mais intuitivo para a população.

*Trello Link:* https://trello.com/invite/b/67e021ddf15cd8069a553fc4/ATTI2f2a6e935278925161b31f9af26054b923385483/sistema-de-sustentabilidade-pessoal

## FASE 01

Na Fase 01, nós desenvolvemos o básico do sistema, classificando cada uma das ações do usuário, são elas a data, o consumo de água, o consumo de energia elétrica, a porcentagem de resíduos reciclados e quais os meios de transporte utilizados no dia inserido, em 3 classificações: Alta sustentabilidade, Moderada sustentabilidade e Baixa sustentabilidade.
Pedimos uma entrada dos dados do usuário a partir de comandos input(), em seguida classificamos os dados nas classificações indicadas utilizando os comandos IF, ELIF e ELSE e e depois retornamos ao usuário sua classificação com o comando print()

*Dificuldades:* A nossa dificuldade nessa etapa foi pensar em um jeito de pedir inputs do usuário para saber quais meios de transporte foram utilizados por ele. Resolvemos nosso problema perguntando se ele usou cada um dos meios e pedindo uma resposta (SIM ou NÃO), com isso classificamos a sustentabilidade do usuário com comandos IF, ELIF e ELSE, além dos operadores OR, AND e ==.

    CÓDIGO DA CLASSIFICAÇÃO DOS MEIOS DE TRANSPORTE UTILIZADOS:

```python
        # Input dos transportes
        print('Qual meio de transporte você usou hoje? (Responda com SIM ou NÃO)')
        transporte_publico = input('Transporte público: ').upper()
        bicicleta = input('Bicicleta: ').upper()
        caminhada = input('Caminhada: ').upper()
        carro = input('Carro (Combustivel fóssil): ').upper()
        carro_eletrico = input('Carro elétrico: ').upper()
        carona_compartilhada = input('Carona compartilhada (Combustível fóssil): ').upper()

        # Classificação da Sustentabilidade de meio de transporte
        if ((bicicleta == 'SIM') or (transporte_publico == 'SIM') or (carro_eletrico == 'SIM') or (caminhada == 'SIM')) and ((carona_compartilhada == 'SIM') or (carro == 'SIM')): #Verifica se tem Alta sustentabilidade E Baxa Sustentabilidade = Moderada Sustentabilidade
            print('Moderada sustentabilidade para meio de transporte.')
        elif (bicicleta == 'SIM') or (transporte_publico == 'SIM') or (caminhada == 'SIM') or (carro_eletrico == 'SIM'):
        #Verifica se tem Alta sustentabilidade
            print('Alta sustentabilidade para meio de transporte.')
        elif (carona_compartilhada == 'SIM') or (carro == 'SIM'):
            print('Baixa sustentabilidade para meio de transporte.')
        #Verifica se tem Baixa sustentabilidade
```