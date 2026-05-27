#Single Inheritance
class parent:
    
    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent", self.__num)

class child(parent):
    def __init__(self):
        super().__init__() #Calling the parent class constructor
        self.__var = 10

    def show(self):
        print("Child", self.__var)  

#TYPES OF INHERITANCE
''' 
1.Single Inheritance: A child class inherits from a single parent class.
2.**Multiple Inheritance(Diamond Problem): A child class inherits from multiple parent classes.(most imp)
3.Multilevel Inheritance: A child class inherits from a parent class, which in turn
inherits from another parent class. 
4.Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
5.Hybrid Inheritance: A combination of two or more types of inheritance. 


'''
#Multiple Inheritance 
class Father:
    def skill1(self):
        print("Father:  skill" )

class Mother:
    def skill2(self):
        print("Mother's skill")

class Child(Father, Mother):
    def skills(self):
        print("Child Inherits both skills")

    obj = child()
    obj.skill1()
    obj.skill2()
    obj.skills() 

#EXample 2 
#Method resolution order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
#In multiple inheritance, if a method is called on an instance of a child class, Python will first
class Phone: #parent
    def __init__(self,price,brand,camera):
        print("INSIDE PHONE CONSTRUCTOR")
        self.__price = price
        self.brand = brand 
        self.camera = camera

    def buy(self):
        print("Phone Buy method")   

class Product: 
    def review(self):
        print("product Buy method ") 

class Smartphone(Phone, Product): #child
    pass 

s = Smartphone(20000, "samsung", 16)
print(s.buy())
print(s.review()) 


#example 3 
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self ):
        return 30
    def m2(self):
        return 20

class C(B):
    def m2(self):
        return 20 
    
obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m1()+ obj3.m1() + obj3.m1()) 

#