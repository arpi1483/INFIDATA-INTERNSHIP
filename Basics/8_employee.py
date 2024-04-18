name=input('enter the employee name:')
eid=int(input('enter the eid:'))
basic_salary=float(input('enter the basic salary:'))
da=(basic_salary*40)/100
hra=(basic_salary*20)/100
gross_salary=basic_salary+da+hra
print('da 40% of basic salary:',da)
print('hra 40% of basic salary:',hra)
print('gross salary 40% of basic salary:',gross_salary)
