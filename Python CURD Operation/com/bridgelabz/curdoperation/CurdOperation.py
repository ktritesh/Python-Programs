import mysql.connector

mydb = mysql.connector.connect(  #making connection with db
  host="localhost",
  user="root",
  password="riteshkt",
  database="mydatabase"
)

# print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
print("mydatabase db is created in mySql \n")

mycursor.execute("SHOW DATABASES") #to show db in mysql
print("List of database in Mysql is")
for db in mycursor:
  print(db) #list of databases will be shown

#create table name = customers
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
print("\nTables in mydatabase")
for tables in mycursor:
  print(tables)

#Insert data into the table = customer
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ('vikash', 'Mountain 21')
#mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted. \n")

#Update data in customer table
sql = "UPDATE customers SET address = 'Hinjewadi' WHERE name = 'Vikash'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#Retrive data from customers database
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
print("Data inside the customer table is following")
for records in myresult:
  print(records)

# Delete data from customer table
sql = "DELETE FROM customers WHERE address = 'Hinjewadi'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) are deleted successfully")