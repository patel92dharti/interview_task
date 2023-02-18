List=[]
class Travel_Agency:
    global List
      
    def welcome_travel(self):
        print("-----------Welcome To Travel Agency-----------")
        print("Popular destinations : ")
        print("1. Ahmedabad")
        print("2. Surat")
        print("3. Udaipur")
        print("4. Jaipur")
        print("5. Mumbai")
        print("6. Pune")
        print("Do You want Membership ? [y/n]: ")
        self.choice=input()
class Check_membership(Travel_Agency):
    def membership(self):
        if self.choice.lower()=="y":
            print("----------Sign-up Registration Form---------")

        elif self.choice.lower()=="n":
            print("Thank You")
        
        else:
            print("Invalid Input")
class Registration(Check_membership):
    def form(self):
        if self.choice.lower()=="y":
            

            self.name=input("Name : ")
            List.append(self.name)
            self.contact=int(input("Contact : "))
            List.append(self.contact)

            self.gender=input("Gender :")
            List.append(self.gender)
            self.user=input("E-mail/user-name : ")
            List.append(self.user)
            self.password=input("Password : ")
            List.append(self.password)
            self.address=input("Address: ")
            List.append(self.address)
            self.pin=int(input("Pin : "))
            List.append(self.pin)
            print(">>>>>>>>>>>Thank You For Registration")
    
class LOGIN_WINDOW(Registration):

    def input_user(self):
        if self.choice.lower()=="y":
            print("----Login----")
            self.user_name=input("user-name : ")
            self.password_us=input("password : ")
    def check_user(self):
        if self.choice.lower()=="y":
            if self.user_name in List:
                if self.password_us in List:
                    print("ACEESS GRANT")
            else:
                print("ACESS DENIED")
obj=LOGIN_WINDOW()
obj.welcome_travel()
obj.membership()
obj.form()
obj.input_user()
obj.check_user()
