import mysql.connector

myconn = mysql.connector.connect(host='localhost',user='root',password="",database="company")

cur=myconn.cursor()

sql="insert into employee1(ename,eid,dept,designation,mobile,email,place) values(%s,%s,%s,%s,%s,%s,%s)"

name=input("enter employee name:")
eid=int(input("enter emp id:"))
dept=input("enter dept name:")
designation=input("enter designation:")
mobile=input("enter mobile.no:")
email=input("enter ur email id:")
place=input("enter ur work place:")

val=(name,eid,dept,designation,mobile,email,place)

try:
    cur.execute(sql,val)
    myconn.commit()
    print("data inserted")

except Exception as e:
    print("can not process")
    myconn.rollback()

print(cur.rowcount,"record inserted")
myconn.close()
