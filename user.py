
import admin as ad

#a=User(,,,,)#
#b=User(,,,)
#after a -login_info={"a":'a'}
#after b -login_info={"a":'a','b':'b'}

class User:
    login_info = {"Ranjith": "Ranjith"}
    profile = {"Ranjith":{"Name":"Ranjith","Phone Number":9025615550,"Email":"rk@gmail.com","Address":"16, Nehru Nagar, Pondicherry - 605014","Password":"RK@244199"}}

    def __init__(self, usrname, fullname, phoneno, email, address, password):
        self.usrname = usrname
        self.fullname = fullname
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.usrname] = self.password
        User.profile[self.usrname] = {"Name":self.fullname,"Phone Number":self.number,"Email":self.email,"Address":self.address,"Password":self.password}
        self.order_history = {}
        self.orders=1

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("You've successfully logged in.....")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False


    def place_order(self):
        print("What you want to order here in the MENU")
        print(ad.show_usrmenu())
        user_choice = int(input("If you want to order then select 1.YES 2.NO - "))
        if user_choice == 1:
            l1 = input("Enter the Food ID here: ")
            foodid=[]
            quan=[]
            price=[]
            total=[]
            x=0
            for word in l1:
                if word.isdigit():
                    foodid.append(int(word))
            for id in foodid:
                l2 = int(input(f"Enter the Quantity of item for Food ID-{id} here: "))
                quan.append(l2)           
            again_ask = input("Are you still want to order this Enter YES or NO:-  ")
            if again_ask == "YES":
                print("\n**********Your Cart is***********")
                for k in range(len(foodid)):
                    print(f'''{ad.menu[foodid[k]]["Name"]} ({ad.menu[foodid[k]]["Quantity"]}) [{ad.menu[foodid[k]]["Price"]}] x {(quan[k])} = {quan[k]*ad.menu[foodid[k]]["Price"]}''')
                    total.append(ad.menu[foodid[k]]["Price"]*quan[k])   
                print(f"It costs you {sum(total)}INR in total")
                for l in range(len(foodid)):
                    self.order_history[self.orders] = {
                                    "Item Name":ad.menu[foodid[l]]["Name"],
                                    "Price": ad.menu[foodid[l]]["Price"],
                                    "Quantity": quan[l]
                                    }
                    self.orders+=1
                for m in range(len(foodid)):      
                    final_stock = ad.menu[foodid[m]]["Stock"] - quan[m]
                    ad.menu[foodid[m]]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def update_profile(self):
        onm = input("Enter your Username:- ")
        print("*****Your Profile*******")
        print(User.profile[onm])
        nm = input("Enter your Name here: ")
        pn = int(input("Enter your Phone number here: "))
        em = input("Enter your Email here: ")
        ad = input("Enter your Address here: ")
        pd = input("Enter your Password here: ")
        User.profile[onm]["Name"] = nm
        User.profile[onm]["Phone Number"] = pn
        User.profile[onm]["Email"] = em
        User.profile[onm]["Address"] = ad
        User.profile[onm]["Password"] = pd
        print("*****Edited Profile successfully*****")
        print(User.profile[onm])
        User.login_info[onm]=pd
        
    def orders_history(self):
        oh=self.order_history
        for i in oh:
            print("Item Name:- ",oh[i]["Item Name"])
            print("Price:- ",oh[i]["Price"])
            print("Quantity:- ",oh[i]["Quantity"])
            print("\n")

        


       

