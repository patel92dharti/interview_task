import random
li=[]
class Game:
    global li
    def user_details(self,name,age,number,email):
        self.name=name
        self.age=age
        self.number=number
        self.email=email
        print("*"*50)
        print(f"Hello {self.name},\nYour Age is {self.age}.\nYour Number is {self.number}.\nYour Email ID is {self.email}.")
    
    def number_choice(self):
        self.number=random.randint(1,10)
    def input_number(self):
        n=int(input("Enter Your Choice Number: "))
        if n==self.number:
            li.append(n)
            print("Your Number is Matched with Computer")
        else:
            print("Your Number does Not Matched with Computer")
    def result(self):
        print(len(li))
        if (len(li)) >=1:
            print("Congratulations!!!!!!!")
            print("Your Are Winner")
        else:
            print("Your Are Looser.......")
            print("Sorry Please Try Again")
         
                
            
obj=Game()   

while True:
    print("*"*50)
    print("Welcome to Housie Game")
    print("1. Start To Play")
    print("2. Game Rules")
    print("3. Exit")

    choice=int(input("Enter Your Choice Number: "))
    if choice==1:
        print("*"*50)
        name=input("Enter your Name: ")
        age=int(input("Enter Your Age: "))
        number=int(input("Enter Your Number: "))
        email=input("Enter Your Email: ")
        obj.user_details(name,age,number,email)
        
        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()
        
        obj.input_number()
        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()

        obj.input_number()

        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()

        obj.input_number()
        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()

        obj.input_number()

        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()

        obj.input_number()

        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()

        obj.input_number()

        print("*"*50)
        print("Choicse Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()
        obj.input_number()

        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()

        obj.input_number()

        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()
        obj.input_number()

        print("*"*50)
        print("Choice Your Number beetween 1 to 10")
        print("*"*50)
        obj.number_choice()
        obj.input_number()
        obj.result()
        

        

    elif choice==2:
        print("*"*50)
        print("--------Rules--------")
        print("1.We have to give you 10 chance for Play the game.")
        print("2.if You give correct Ans then You are Winer......")
        print("3.if You give Wronge Ans then You are Looser........")

        
    else:
        print("Good Bye")
        break
    
