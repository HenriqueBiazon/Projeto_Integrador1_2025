def DBconnect():
    import mysql.connector # type: ignore
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

def DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte): #INSERE OS DADOS EM UMA NOVA LINHA DA TABELA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = 'INSERT INTO dados_sustentabilidade (data, consumo_agua, consumo_energia, porcentagem_reciclagem, meio_transporte) VALUES (%s,%s,%s,%s,%s)'
    values = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)

    cursor.execute(sql,values)
    mydb.commit() 

def DBselect(): #SELECIONA A TABELA INTEIRA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = 'SELECT * FROM dados_sustentabilidade'
    cursor.execute(sql)
    myresult = cursor.fetchall()

    # X = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meio_transporte)

    return myresult
DBconnect()

def DBselect_dados(data): #SELECIONA A LINHA EM UMA DATA ESPECÍFICA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'SELECT * FROM dados_sustentabilidade WHERE data = "{data}"'
    cursor.execute(sql)
    myresult = cursor.fetchall()

    return myresult

def DBalter_dia(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte):
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = 'ALTER TABLE dados_sustentabilidade (data, consumo_agua, consumo_energia, porcentagem_reciclagem, meio_transporte) VALUES (%s,%s,%s,%s,%s)'
    values = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)

    cursor.execute(sql,values)
    mydb.commit()
    
def DBdelete_dia(data):
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'DELETE FROM dados_sustentabilidade WHERE data = "{data}"'

    cursor.execute(sql)
    mydb.commit()