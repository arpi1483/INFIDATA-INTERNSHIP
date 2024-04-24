import mysql.connector

#create the connection object
myconn = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="company"
)

#creating the cursor object
cur = myconn.cursor()

try:
    cur.execute("create table employee1(ename varchar(30),eid int(4) primary key,dept varchar(20),designation varchar(20),mobile varchar(20),email varchar(20),place varchar(20))")
    print("your table is created successfully")

except Exception as e:
    print("can not process",e)

myconn.close()