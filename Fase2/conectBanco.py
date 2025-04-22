def DBconnect():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="BD-ACD",
        user="BD180225117",
        password="Tdtgj9",
        database="BD180225117"
    )
    print(mydb)
    return mydb


