'''#Super keyword is used to call the parent class constructor 
#and methods in the child class. It is used to access the properties 
#and methods of the parent class from the child class.

1.super can access parent method 
2.super cannot be use outside the class 
3 super is used inside child class constructor to call the parent class constructor '''

class Phone:
    def __init__(self, price, brand, camera):
        print('Inside Phone Constructor')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print('Buying Phone')

class smartphone(Phone):
    def __init__(self, price, brand, camera):
        print('Inside Smartphone Constructor')
        super().__init__(price, brand, camera) #Calling the parent class constructor
    def buy(self):
        print('Buying a Smartphone')  #This will print as child buy will be given the priority as it will overwrite the parent buy
        
s = smartphone(20000, 'Samsung', 16, "Android", 8) 

print(s.buy()) 
print(s.brand)
print(s.camera)
print(s.os)
print(s.brand) 

'''NOTE: summary of inheritance:
1. If the child class has its own constructor, it will override the parent class constructor
2. To call the parent class constructor
3. A class can Inherit from other class using super() function.
4. Inheritance reduce code redundancy and increases code reusability.
5. You can even inherit the constructor, methods and properties of the parent class.
6. Parent has no access to the child class members but child has access to the parent class members.
7. Private property of parents are not accessible to the child class.
8. If the child class has its own method with the same name as the parent class method,
then the child class method will override the parent class method.
9. If the child class has its own constructor, it will override the parent class constructor
10.Super() function is used to call the parent class constructor 
and methods in the child class. It is used to access the properties 
and methods of the parent class from the child class.
11. super can access parent method 
12.super cannot be use outside the class''' 

