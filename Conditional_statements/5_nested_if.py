print('select a food category 1:veg,2:non_veg:')
choice=int(input())
if(choice==1):
    print('you have selected veg category')
    menu=int(input('select menu 1:meals 2:Idli 3:dosa:'))
    if(menu==1):
        print("you have selected meals")
    elif(menu==2):
        print("you have selected idli")
    elif(menu == 3):
        print("you have selected dosa")
    else:
        print('menu not available')
elif(choice==2):
    print('you have selected non_veg')
    opt=int(input('select option 1:chicken 2:matton 3:kabab:'))
    if(opt==1):
        print("you have selected chicken")
    elif(opt == 2):
        print("you have selected matton")
    elif(opt==3):
        print("you have selected kabab")
    else:
        print("option not avilable")

else:
    print('invalid category')