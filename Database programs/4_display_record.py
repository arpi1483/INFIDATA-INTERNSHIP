import mysql.connector

myconn = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password="",
                                 database="company")

cur = myconn.cursor()

try:
    #reading the employee table
    cur.execute("select * from employee1 where eid=101")

    #fetching the rows from the cursor object
    result=cur.fetchall()

    #printing the result
    for x in result:
        print(x)

except Exception as e:
    print("can not process:",e)

myconn.close()