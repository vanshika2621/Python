#private membera/Attribute

class Atm:
    def __init__(self, balance): #constructor method
        self.__balance = balance #attribute 
        self.__pin = "" #private attribute
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
    
    def get_balance(self): #GETTER 
        return self.__balance
    
    def set_balance(self, new_balance): #SETTER
        if new_balance is int :
            self.__balance = new_balance 
        else:
            print("SAALEEE!!! ")


    def create_pin(self): #method
        new_pin = input("Enter new PIN: ") 
        self.__pin = new_pin 
        print("PIN created successfully") 
        self.menu()
    
    def deposit(self): #method
        temp = input("Enter PIN: ")
        if temp == self.__pin:
            amount = float(input("Enter amount to deposit: ")) 
            self.__balance += amount 
            print("Deposit successful. Your new balance is: ", self.__balance)
        else:
            print("Incorrect PIN") 

    def withdraw(self): #method 
        temp = input("Enter PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to withdraw: ")) 
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.__balance -= amount 
                print("Withdrawal successful. Your new balance is: ", self.__balance) 
        else: 
            print("Incorrect PIN")  
        
    def check_balance(self): #method
        temp = input("Enter PIN: ")
        if temp == self.__pin:
            print("Your balance is: ", self.__balance)
        else:
            print("Incorrect PIN") 

my_atm = Atm(1000) 
my_atm.menu() 

#nothin in python is truly private. We can access private members using name mangling.
print(my_atm._Atm__balance) #1000
print(my_atm._Atm__pin) #" " 

baroda = Atm(2000)
baroda.set_balance(5000)
print(baroda.get_balance()) #5000 

#storing objects in a list
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def __str__(self):
        return f"{self.name} is {self.age} years old"
s1 = Student("Vanshika", 20)
s2 = Student
("Pratyaksh", 21)
students = [s1, s2]
for student in students:
    print(student)

#storing objects in a dictionary
student_dict = {"Vanshika": s1, "Pratyaksh": s2}
print(student_dict["Vanshika"]) #Vanshika is 20 years old
print(student_dict["Pratyaksh"]) #Pratyaksh is 21 years old

#sir 
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am", self.name, "and I am", self.age, "years old")


c1 = Customer("Kshitij", 26)
c2 = Customer("Nitish", 27)
c3 = Customer("Anshuman", 28)

L = [c1, c2, c3]

for i in L:
    i.intro()