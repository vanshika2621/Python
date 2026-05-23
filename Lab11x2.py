class Parent:
    def __init__ (self, num):
        self.__name = num 


    def get_num(self): #GETTER
        return self.__name 
    

class child(Parent):
    def __init__(self):
        print("Child class constructor called")

son = child() #Child class constructor
print(son.get_num()) #AttributeError: 'child' object has no attribute '_Parent__name'
son.show() #AttributeError: 'child' object has no attribute 'show'

