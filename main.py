import admin as aa
from user import User

uhh = User(str, str, str, str, str, str)
Loop=True
while Loop:
    inp = int(input("LOGIN AS Admin(press 1)\nLOGIN AS User(press2)\nExit(press 3) \t Enter your choice:- "))
    if inp == 1:
        Username = input("USERNAME: ")
        Password = input("PASSWORD: ")
        if aa.admin_keys[Username] == Password:
            print("*****You have successfully logged in*****")
            admin_crawler = True
            while admin_crawler:
                adm_choice = int(input("1.ADD NEW FOOD ITEM\n2.EDIT FOOD ITEM\n3.VIEW MENU\n4.REMOVE FOOD ITEM\n5.LOGOUT\t Choose the options: "))
                if adm_choice == 1:
                    aa.add_new_item()
                elif adm_choice == 2:
                    aa.edit_from_item()
                elif adm_choice == 3:
                    aa.show_menu()
                elif adm_choice == 4:
                    aa.show_menu()
                    aa.remove_item()
                elif adm_choice == 5:
                    print("LOGGED OFF")
                    admin_crawler = False
                else:
                    print("This is the wrong selection. Please select valid option")
        else:
            print("Username or Password is invalid")
    elif inp == 2:
        print("Welcome to the user panel")
        signup=True
        while signup:
            opt=int(input(" For Sign in(press 1)\n For Sign up(press 2) \nExit(press 3) \t Enter your choice:- "))
            if opt == 1:
                username = input("Enter the username here: ")
                password = input("Enter the password here: ")
                if User.login(username, password):
                    print(f"You are logged in successfully {username}")
                    user_crawler = True
                    while user_crawler:
                        usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Update Profile 4.Logout"))
                        if usr_choice == 1:
                            uhh.place_order()
                        elif usr_choice == 2:
                            print(f"Here is your order history, {username}")
                            uhh.orders_history()
                        elif usr_choice == 3:
                            uhh.update_profile()
                        elif usr_choice == 4:
                            user_crawler = False
                            print("You're Successfully logged out")
                        else:
                            print("You choose the invalid option")
                else:
                    print("These are the wrong credentials! SORRY!!!")
            elif opt == 2:
                print("*****Please fill the Profile*******")
                usnm=input("Enter the username here: ")
                pwd=input("Enter the password here: ")
                flnm=input("Enter the Full Name here: ")
                phno=int(input("Enter the Phone Number here: "))
                emid = input("Enter your Email here: ")
                add = input("Enter your Address here: ")
                print("*******Successfully signed up**********")
                call=User(usnm,flnm,phno,emid,add,pwd)
            else:
                signup=False
            
    else:
        Loop=False
        exit()




