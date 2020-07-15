from flask import Flask
from flask import request
import mysql.connector
  
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rafiqi10106",
  database="property_guru"
)

mycursor = mydb.cursor()

@app.route('/postjson', methods = ['POST'])

def postJsonHandler():
    
    print (request.is_json)
    content = request.get_json()
    py_data = content['Property']
    length = len(py_data)
    print(py_data)
    for i in py_data :
        sqlQuery = "INSERT INTO Property(Name,Type,Price,Address,PSF,Tenure,Furnishing,Developer,Link) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (i['Name'],i['Type'],i['Price'],i['Address'],i['Price Per Square Feet'],i['Tenure Status'],i['Furnishing'],i['Developer'],i['Link'])
        mycursor.execute(sqlQuery, data)
        mydb.commit()
    
    return "Data Inserted"

    '''
    try:
        # convert json data to python dictionary
        _json = request.json
        _name = _json['name']
        _address = _json['address']
        #_last_name = _json['last_name']
        #_class = _json['class']
        #_age = _json['age']
        #_address = _json['address']
        #_status = _json['status']
 
	    
        # insert record in database
        #sqlQuery = "INSERT INTO customer(roll_no, first_name, last_name, class, age, address, status) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        sqlQuery = "INSERT INTO customer(name,address) VALUES(%s,%s)"
        #data = (_roll_no, _first_name, _last_name, _class, _age, _address, _status,)
        data = (_name,_address)
        #conn = mysql.connect()
        #cursor = conn.cursor()
        mycursor.execute(sqlQuery, data)
        mydb.commit()
        res = jsonify('Student created successfully.')
        res.status_code = 200
 
        return res
        
        else:
            return not_found()
    
    except Exception as e:
        print(e)
        
    
    #finally:
    #    mycursor.clos() 
    #    mydb.close()
    '''


    
@app.route('/')
def mainpage():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Property")
    myresult = mycursor.fetchall()

    print(myresult[0])
    
    row = []

    for i in myresult:
        row.append("<tr>")
        row.append("<td>" + str(i[0]) + "</td>")
        row.append("<td>" + str(i[1]) + "</td>")
        row.append("<td>" + str(i[2]) + "</td>")
        row.append("<td>" + str(i[3]) + "</td>")
        row.append("<td>" + str(i[4]) + "</td>")
        row.append("<td>" + str(i[5]) + "</td>")
        row.append("<td>" + str(i[6]) + "</td>")
        row.append("<td>" + str(i[7]) + "</td>")
        row.append("<td>" + str(i[8]) + "</td>")
        row.append("<td>" + str(i[9]) + "</td>")
        row.append("</tr>")
    
    table_row = "".join(row)

    header = "<th><b>ID</b></th><th><b>Name</b></th><th><b>Type</b></th><th><b>Price</b></th><th><b>Address</b></th><th><b>PSF</b></th><th><b>Tenure</b></th><th><b>Furnishing</b></th><th><b>Developer</b></th><th><b>Link</b></th>"
  
    return ''' <table border = 1><tr>''' + header + '''</tr><tr>''' + table_row + '''</tr></table> '''
  

app.run(host='127.0.0.1', port= 5000)


