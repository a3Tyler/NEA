# # # # # TESTIT SERVER PROGRAM # # # # #
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", username = input("Enter username : "), password = input("Enter password : "))

print(mydb)