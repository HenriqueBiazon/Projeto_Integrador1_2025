def DBconnect():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Jppm2006",
        database="projeto_integrador_fase2"
        #host="BD-ACD",
        #user="BD180225117",
        #password="Tdtgj9",
        #database="BD180225117"
    )
    return mydb

def DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte):
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = 'INSERT INTO dados_sustentabilidade (data, consumo_agua, consumo_energia, porcentagem_reciclagem, meio_transporte) VALUES (%s,%s,%s,%s,%s)'
    values = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte)

    cursor.execute(sql,values)
    mydb.commit() 

def DBselect():
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = "SELECT * FROM dados_sustentabilidade"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    # X = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meio_transporte)

    return myresult

