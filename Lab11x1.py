#INHERITANCE 
class User:
    def init__(self, name, email):
        self.name = name 
        self.email = email 
    def login(self):
        print(f"{self.name} has logged in with email {self.email}")

class student(User):
    def init__(self, name, email, student_id):
        super().init__(name, email)
        self.student_id = student_id 
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Student ID: {self.student_id}") 

u = User("Vanshika", "vanshikagiri2020@gmail.com")
u.login() #Vanshika has logged in with email
v = student("Vanshika", "vanshikagiri2020@gmail.com", "S12345")
v.login() #Vanshika has logged in with email 
v.display_info()
#Student Name: Vanshika
#Email: vanshikagiri2020@gmail.com 
#Student ID: S12345 

class Phone:
    def init__(self,price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print(f"Bought a {self.brand} phone for {self.price} with a {self.camera} camera")  

class Smartphone(Phone):
    def init__(self, price, brand, camera, os, ram):
        super().init(price, brand, camera)
        self.os = os
        self.ram = ram
    def buy(self):
        print(f"Bought a {self.brand} smartphone for {self.price} with a {self.camera} camera and {self.os} operating system")

p = Phone(10000, "Nokia", "12MP")
p.buy() #Bought a Nokia phone for 10000 with a 12MP camera
s = Smartphone(50000, "Apple", "12MP", "iOS", "8GB")
s.buy() #Bought a Apple smartphone for 50000 with a 12MP camera and iOS operating system

''' NOTE:
If the child class has it's own constructor,
it will override the parent class constructor. 
To call the parent class constructor, we can use super() function. '''  

'''NOTE:
Child class can't access the private members of the parent class.''' 

