import mysql.connector
def DBconnect():
    mydb = mysql.connector.connect(
        #host="BD-ACD",
        #user="BD180225117",
        #password="Tdtgj9",
        #database="BD180225117"
        host="127.0.0.1",
        user="root",
        password="Jppm2006",
        database="projeto_integrador_fase2"
    )
    return mydb

##Tabela dados_sustentabilidade:
MYDB = DBconnect()
def DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte): #INSERE OS DADOS EM UMA NOVA LINHA DA TABELA
    cursor = MYDB.cursor()

    sql = 'INSERT INTO dados_sustentabilidade (data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte) VALUES (%s,%s,%s,%s,%s)'
    values = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)

    cursor.execute(sql,values)
    MYDB.commit() 

def DBselect(): #SELECIONA A TABELA INTEIRA
    cursor = MYDB.cursor()

    sql = "SELECT * FROM dados_sustentabilidade ORDER BY STR_TO_DATE(data, '%d/%m/%Y') ASC"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    return myresult

def DBselect_dia(data): #SELECIONA A LINHA EM UMA DATA ESPECÍFICA
    cursor = MYDB.cursor()

    sql = f'SELECT * FROM dados_sustentabilidade WHERE data = "{data}"'
    cursor.execute(sql)

    myresult = cursor.fetchall()
    myresult = myresult.pop(0)

    return list(myresult)

def DBalter_dia(data,paraAlterar,alteracao): #ALTERA OS DADOS DE UM DIA
    cursor = MYDB.cursor()

    sql = f"UPDATE dados_sustentabilidade SET {paraAlterar} = %s WHERE data = %s"
    values = (alteracao, data)
    cursor.execute(sql,values)
    MYDB.commit()

def DBdelete(data): #DELETA A CLASSIFICAÇÃO E OS DADOS
    cursor = MYDB.cursor()

    # First, delete from the referencing table to avoid foreign key constraint errors
    sql = f'DELETE FROM classificacao_sustentabilidade WHERE data = "{data}"'
    cursor.execute(sql)

    sql = f'DELETE FROM dados_sustentabilidade WHERE data = "{data}"'
    cursor.execute(sql)
    MYDB.commit()

##Tabela classificacao_sustentabilidade:

def DBinsert_classificacao(data,classificacao_agua, classificacao_energia,classificacao_reciclagem,classificacao_transporte): #INSERE AS CLASSIFICACOES EM UMA NOVA LINHA DA TABELA
    cursor = MYDB.cursor()

    sql = 'INSERT INTO classificacao_sustentabilidade (data,classificacao_agua, classificacao_energia,classificacao_reciclagem,classificacao_transporte) VALUES (%s,%s,%s,%s,%s)'
    values = (data,classificacao_agua, classificacao_energia,classificacao_reciclagem,classificacao_transporte)

    cursor.execute(sql,values)
    MYDB.commit()

def DBselect_classificacao_dia(data): #SELECIONA A LINHA EM UMA DATA ESPECÍFICA
    cursor = MYDB.cursor()

    sql = f'SELECT * FROM classificacao_sustentabilidade WHERE data = "{data}"'
    cursor.execute(sql)

    myresult = cursor.fetchall()
    myresult = myresult.pop(0)

    return list(myresult)

def DBalter_classificacao(data,classificacao_agua, classificacao_energia,classificacao_reciclagem,classificacao_transporte): #ALTERA A CLASSIFICACAO DE UM DIA
    cursor = MYDB.cursor()

    sql = f"UPDATE classificacao_sustentabilidade SET classificacao_agua = %s WHERE data = %s"
    values = (classificacao_agua, data)
    cursor.execute(sql,values)
    MYDB.commit()
    sql = f"UPDATE classificacao_sustentabilidade SET classificacao_energia = %s WHERE data = %s"
    values = (classificacao_energia, data)
    cursor.execute(sql,values)
    MYDB.commit()
    sql = f"UPDATE classificacao_sustentabilidade SET classificacao_reciclagem = %s WHERE data = %s"
    values = (classificacao_reciclagem, data)
    cursor.execute(sql,values)
    MYDB.commit()
    sql = f"UPDATE classificacao_sustentabilidade SET classificacao_transporte = %s WHERE data = %s"
    values = (classificacao_transporte, data)
    cursor.execute(sql,values)
    MYDB.commit()