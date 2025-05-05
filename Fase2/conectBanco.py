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

def DBinsert_dados(data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte, Id_usuario): #INSERE OS DADOS EM UMA NOVA LINHA DA TABELA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = 'INSERT INTO dados_sustentabilidade (data, consumo_agua, consumo_energia, porcentagem_reciclagem, meios_transporte,Id_usuario) VALUES (%s,%s,%s,%s,%s,%s)'
    values = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meios_transporte, Id_usuario)

    cursor.execute(sql,values)
    mydb.commit() 

def DBselect(Id_usuario): #SELECIONA A TABELA INTEIRA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'SELECT * FROM dados_sustentabilidade WHERE Id_usuario = "{Id_usuario}"'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    #myresult = myresult.pop(0)
    linhas = (cursor.rowcount)
    # X = (data, consumo_agua, consumo_energia, porcentagem_reciclagem, string_meio_transporte)

    return myresult,linhas
DBconnect()

def DBselect_dia(data, Id_usuario): #SELECIONA A LINHA EM UMA DATA ESPECÍFICA DE UM USUARIO ESPECÍFICO
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'SELECT * FROM dados_sustentabilidade WHERE data = "{data}" AND Id_usuario = "{Id_usuario}"'
    cursor.execute(sql)

    myresult = cursor.fetchall()
    myresult = myresult.pop(0)

    return list(myresult)

def DBalter_dia(data,paraAlterar,alteracao, Id_usuario):
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f"UPDATE dados_sustentabilidade SET {paraAlterar} = %s WHERE data = %s AND Id_usuario = %s"
    values = (alteracao, data, Id_usuario)
    cursor.execute(sql,values)
    mydb.commit()
    
def DBdelete_dia(data, Id_usuario):
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'DELETE FROM dados_sustentabilidade WHERE data = "{data}" AND Id_usuario = "{Id_usuario}"'

    cursor.execute(sql)
    mydb.commit()

def DBselect_usuario(nome, senha):
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'SELECT * FROM usuarios WHERE nome = "{nome}" AND senha = "{senha}"'
    cursor.execute(sql)

    myresult = cursor.fetchall()
    myresult = myresult.pop(0)

    return myresult

def DBinsert_usuario(nome, senha): #INSERE O USUARIO EM UMA NOVA LINHA DA TABELA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = 'INSERT INTO usuarios (nome, senha) VALUES (%s,%s)'
    values = (nome, senha)

    cursor.execute(sql,values)
    mydb.commit()

def DBselect_tabela_usuarios(): #SELECIONA A TABELA INTEIRA
    mydb = DBconnect()
    cursor = mydb.cursor()

    sql = f'SELECT * FROM usuarios'
    cursor.execute(sql)
    myresult = cursor.fetchall()

    return myresult