import mysql.connector


def conexionbd():
	return mysql.connector.connect(host="localhost", user="daniel", password="Dany4724+", database="Contabilidad")





