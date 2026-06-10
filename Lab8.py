#OOPS
#All the datatype in python like integer, float, set , dictionary, list are classes in python 
#whatever variable you create of these class are called objects of that class
#Basic Structure of a class
#Attribute is a variable that belongs to an object
#Method is a function that belongs to an object 
'''class Car: 
    color = "Blue" #attribute
    model = "sports" #attribute
    def calculate_speed(self, distance, time): #method
        speed = distance / time 
        return speed 
    
#creating an object of the class
my_car = Car() 

print(type(my_car)) #<class '__main__.Car'>
print(my_car.color) #Blue
print(my_car.model) #sports
print(my_car.calculate_speed(100, 2)) #50.0 '''

'''constructor method is a special method that is called when an object of the class is created
constructor method is defined using __init__() method
constructor method is used to initialize the 
attributes of the class when we don't know the values of the attributes at the time of creating the class ''' 
#self
'''self is a special keyword that is used to refer to the current instance of the class
self is used to access the attributes and methods of the class in python'''

class Atm:
    def __init__(self, balance): #constructor method
        self.balance = balance #attribute 
        self.pin = "" #attribute
    def menu(self): #method
        print("Welcome to the ATM")
        print("1. Create PIN")
        print("2. Check Balance")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Exit") 
        user_input = input("Enter your choice: ") 
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.check_balance()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.deposit()
        elif user_input == "5":
            print("Thank you for using the ATM")
        else:
            print("Invalid choice") 
    
    
    def create_pin(self): #method
        new_pin = input("Enter new PIN: ") 
        self.pin = new_pin 
        print("PIN created successfully") 
        self.menu()
    
    def deposit(self): #method
        temp = input("Enter PIN: ")
        if temp == self.pin:
            amount = float(input("Enter amount to deposit: ")) 
            self.balance += amount 
            print("Deposit successful. Your new balance is: ", self.balance)
        else:
            print("Incorrect PIN") 

    def withdraw(self): #method 
        temp = input("Enter PIN: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: ")) 
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount 
                print("Withdrawal successful. Your new balance is: ", self.balance) 
        else: 
            print("Incorrect PIN")  
        
    def check_balance(self): #method
        temp = input("Enter PIN: ")
        if temp == self.pin:
            print("Your balance is: ", self.balance)
        else:
            print("Incorrect PIN") 

my_atm = Atm(1000) 
my_atm.menu()  

    
    