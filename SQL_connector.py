import mysql.connector 

db = mysql.connector.connect(host="localhost",
                     user="root",
                     password="root",
                     db="sama")

cu = db.cursor()

cu.execute("SELECT * FROM ab")

myresult = cu.fetchall()

for x in myresult:
  print(x)

db.close()