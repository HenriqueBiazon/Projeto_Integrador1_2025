# Projeto-integrador 01

--Projeto Integrador do primeiro semestre do curso de Engenharia de Software na PUC Campinas 2025--

*Integrantes do grupo:* Daniel Neves Papa, Gabriel Diniz Foresti Mian de Almeida, Henrique Biazon Ferreira, João Pedro Panza Mainieri, Lucas do Prado Bezerra e Thiago Gutieri Conte 

*O Projeto:* Consiste em um sistema feito em Python para classificar e monitorar a sustentabilidade diária de uma pessoa, de acordo com os dados inseridos pelo usuário. O sistema tem como intuito facilitar o início da implementação da sustentabilidade na vida das pessoas, fazendo com que seja mais intuitivo para a população.

*Trello Link:* https://trello.com/invite/b/67e021ddf15cd8069a553fc4/ATTI2f2a6e935278925161b31f9af26054b923385483/sistema-de-sustentabilidade-pessoal

---

## FASE 01

Na Fase 01, nós desenvolvemos o básico do sistema, classificando cada uma das ações do usuário, são elas a data, o consumo de água, o consumo de energia elétrica, a porcentagem de resíduos reciclados e quais os meios de transporte utilizados no dia inserido, em 3 classificações: Alta sustentabilidade, Moderada sustentabilidade e Baixa sustentabilidade.  
Pedimos uma entrada dos dados do usuário a partir de comandos `input()`, em seguida classificamos os dados nas classificações indicadas utilizando os comandos `if`, `elif` e `else` e depois retornamos ao usuário sua classificação com o comando `print()`.

*Dificuldades:* A nossa dificuldade nessa etapa foi pensar em um jeito de pedir inputs do usuário para saber quais meios de transporte foram utilizados por ele. Resolvemos nosso problema perguntando se ele usou cada um dos meios e pedindo uma resposta (SIM ou NÃO), com isso classificamos a sustentabilidade do usuário com comandos `if`, `elif` e `else`, além dos operadores `or`, `and` e `==`.

Exemplo do código de classificação dos meios de transporte utilizados:

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
if ((bicicleta == 'SIM') or (transporte_publico == 'SIM') or (carro_eletrico == 'SIM') or (caminhada == 'SIM')) and ((carona_compartilhada == 'SIM') or (carro == 'SIM')):
    print('Moderada sustentabilidade para meio de transporte.')
elif (bicicleta == 'SIM') or (transporte_publico == 'SIM') or (caminhada == 'SIM') or (carro_eletrico == 'SIM'):
    print('Alta sustentabilidade para meio de transporte.')
elif (carona_compartilhada == 'SIM') or (carro == 'SIM'):
    print('Baixa sustentabilidade para meio de transporte.')
```

---

## FASE 02

Na Fase 02, implementamos a integração do sistema com um banco de dados MySQL. Criamos uma tabela para armazenar os dados de sustentabilidade de cada usuário, permitindo salvar, alterar e excluir registros. Utilizamos comandos SQL como `INSERT INTO`, `UPDATE` e `DELETE FROM` para manipulação dos dados.  
Além disso, desenvolvemos funções em Python para realizar essas operações de forma automatizada, garantindo a persistência das informações inseridas pelo usuário.

*Dificuldades:* Aprendemos a conectar o Python ao MySQL usando a biblioteca `mysql-connector-python`. Tivemos que lidar com possíveis erros de conexão e garantir que as operações fossem realizadas de forma segura. O desafio principal foi garantir a integridade dos dados e tratar possíveis exceções durante as operações no banco.

---

## FASE 03

Na Fase 03, focamos na criação de telas interativas para o usuário, tornando o sistema mais amigável e intuitivo. Implementamos menus para navegação, telas para inserção, alteração, exclusão e classificação dos dados.  
Também adicionamos um sistema de login para garantir que cada usuário só tenha acesso aos seus próprios dados.

Outro ponto importante foi a implementação de um sistema de criptografia para proteger as informações sensíveis dos usuários, como nome e senha, utilizando a biblioteca `sympy` e uma cifra baseada em matrizes.

*Dificuldades:* Aprendemos a criar fluxos de navegação mais claros e organizados para o usuário. Implementamos criptografia personalizada para aumentar a segurança dos dados. O desafio foi garantir que a criptografia e a descriptografia funcionassem corretamente para todos os caracteres necessários.

---

## Como executar o projeto

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
2. Configure o banco de dados MySQL conforme as instruções do arquivo `DataBase.sql`.
3. Execute o arquivo principal:
   ```
   python main.py
   ```

---

## Estrutura do Projeto

- `main.py`: Arquivo principal de execução do sistema.
- `Telas.py`: Contém as funções das telas e menus do sistema.
- `conectBanco.py`: Funções para conexão e manipulação do banco de dados.
- `criptografia.py`: Funções de criptografia e descriptografia dos dados.
- `requirements.txt`: Dependências do projeto.
- `DataBase.sql`: Script para criação das tabelas no banco de dados.

---

## Possíveis melhorias futuras

- Adicionar relatórios e gráficos de desempenho sustentável do usuário. (Tabelas)
- Melhorar o sistema de autenticação e segurança.

---