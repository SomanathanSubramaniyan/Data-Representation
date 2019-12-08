import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd


#def DBconnection(query,choice,code,param1):
try:
    connection = mysql.connector.connect(host='localhost',database='accidents', user='root', password='Somu@1975')
    cursor = connection.cursor(prepared=True)
    df = pd.read_sql_query("select * from accidents", connection)

except mysql.connector.Error as error :
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    elif error.errno == 1452:
        print("----------------------------------------------------")
        print("***ERROR***: Country Code " + " does not exist")
        print("----------------------------------------------------")
    elif error.errno == 2003:
        print("----------------------------------------------------")
        print("***ERROR***: mySQL server is down.")
        print("----------------------------------------------------")
    else:
        print("Undefined error")
        print(str(error))
