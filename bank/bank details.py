def create_account():
    global cname,cid,branch,bal
    cname=input('enter the name:')
    cid=int(input('enter the cid:'))
    branch=input('enter the branch name:')
    bal=float(input('enter the balance:'))
def deposite():
    global dep,bal
    dep=int(input('enter the deposit:'))
    bal=bal+dep
    print('the balance is:',bal)
def withdraw():
    global wd,bal
    wd=int(input('enter the amount to withdraw:'))
    if(wd<=bal):
        bal-=wd
        print('the amount can be withdrawed:',bal)
    else:
        print('insufficient balance')
def display():

    print('the name is:', cname)
    print('the id is:', cid)
    print('the branch is:', branch)
    print('the balance is:', bal)
print('Welcome to online banking')
while(True):
    choice=int(input('enter your choice:1:create_account ,2:deposite,3:withdraw,4:display:'))
    if(choice==1):
        create_account()
    elif(choice==2):
        deposite()
    elif(choice==3):
        withdraw()
    elif(choice==4):
        display()
    else:
        print('invalid choice')


