class Person:
    def __init__(self, name, country):
        self.name = name 
        self.country = country
    def greet(self):
        if self.country == "India":
            print(f"Namaste, I'm {self.name}!")
        else:
            print(f"Hello, I'm {self.name}!")
def greet2(person):
    print(f"Hello, I'm {person.name} from {person.country}!")
    p4 = Person("Pratyaksh", "USA")
    return p4
p3 = Person("Vanshika", "India")
x = greet2(p3) #Hello, I'm Vanshika from India!
print(x.name) #Pratyaksh
print(x.country) # USA 

def greet3(person):
    person.name = "Krishna"
    print(person.name) 
     
