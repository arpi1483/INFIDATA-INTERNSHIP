l=int(input('enter length'))
b=int(input('enter breadth'))
h=int(input('enter height'))
while(True):
    choice=int(input('enter ur choice 1:Area, 2:Volume, 3:exit'))
    if(choice==1):
        Area=l*b
        print('area of the rectangle is', Area)
    elif(choice==2):
        Vol=l*b*h
        print('vol if the rectangle is', Vol)
    elif(choice==3):
        exit(0)
    else:
        print('invalid')