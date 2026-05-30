#Polymorphism 
'''
1). Method overriding: When a child class has a method with the same name as the parent class method,
2). Method overloading: When a class has multiple methods with the same name but different parameters.
3). Operator overloading: When a class has multiple methods with the same name but different parameters
'''

# Method  overriding- PYTHON DOES NOT SUPPORT METHOD OVERLOADING BUT IT SUPPORTS METHOD OVERRIDING
class Shape():
    def area (self, radius):
        return 3.14 * radius * radius
    def area (self, length, breadth):
        return length * breadth
    
s = Shape()
print(s.area(5, 10)) #This will RUN, Called as it is the latest one and it will override the first method.
print(s.area(5)) #Throw ERROR 



