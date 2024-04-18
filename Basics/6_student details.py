name=input('enter the student name:')
sid=int(input('enter the student id:'))
branch=input('enter the brach of student:')
email=input('enter the email of student:')
test1=float(input('enter the test1 marks:'))
test2=float(input('enter the test2 marks:'))
test3=float(input('enter the test3 marks:'))
avg=(test1+test2+test3)/3
print('name of student is',name)
print('sid of student is',sid)
print('branch of student is',branch)
print('email of student is',email)
print('avg of t1 t2  and t3 is',avg)
print('Name \t sid \t branch \t email \t\t test1 \t test2 \t test3 \t Avg')
print('__________________________________________________________________')
print(name,"\t",sid,"\t",branch,"\t",email,"\t",test1,"\t",test2,"\t",test3,"\t",avg)


