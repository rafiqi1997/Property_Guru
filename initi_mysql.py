import mysql.connector


try :
    
    mydb = mysql.connector.connect( host="localhost", user="root", password="rafiqi10106")

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE property_guru")

except :
    
    mydb = mysql.connector.connect( host="localhost", user="root", password="rafiqi10106", database = "property_guru")

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE Property ( id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Type VARCHAR(255) , Price VARCHAR(255), Address VARCHAR(255), PSF VARCHAR(255), Tenure VARCHAR(255), Furnishing VARCHAR(255), Developer VARCHAR(255), Link VARCHAR(255))")
