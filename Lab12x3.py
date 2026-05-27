#Multilevel Inhertance 

class Product: #grand parent
    def review(self):
        print("product Customer review")

class Phone(Product): #parent
    def __init__(self,price,brand,camera):
        print("INSIDE PHONE CONSTRUCTOR")
        self.__price = price
        self.brand = brand 
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone): #child
    pass

s = Smartphone(20000, "samsung", 16)
print(s.buy())


#Hierarchical Inheritance 
class Phone(Product): #parent
    def __init__(self,price,brand,camera):
        print("INSIDE PHONE CONSTRUCTOR")
        self.__price = price
        self.brand = brand 
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone): #child
    pass

class Featurephone(Phone):
    pass 

Smartphone(10000, "samsung", '13px').buy()
Featurephone(20000, "LeECo", "8px").buy() 
 

 
