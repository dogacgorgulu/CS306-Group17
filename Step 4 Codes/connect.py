import mysql.connector
from mysql.connector import errorcode
from config import _password


def connectionCreator():
    try:
        cnx = mysql.connector.connect(user="root", password=_password, database="CS306")
        print("Connection established with the database")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        cnx.close()
        return None
