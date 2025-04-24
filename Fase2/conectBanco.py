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
    print(mydb)
    return mydb
DBconnect()

