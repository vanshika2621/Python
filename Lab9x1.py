

class point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y 
    def __str__(self):
        return f"<{self.x}, {self.y}>" 
    
    #distance between two points
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5 
    #distance of a point from the origin
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5 
    #To find if a point lies on a line 
    
class line:
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c
    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0" 
    def is_point_on_line(line, point):
        if line.a * point.x + line.b * point.y + line.c == 0 :
            return "Lies on the line"
        else: 
            return "Not on the line"  
    def shortest_distance(line, point):
        return (abs(line.a *point.x + line.b * point.y + line.c)/((line.a)**2 + (line.b)**2)**0.5) 
            
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
print(x.country) #USA  



p = point(2,3)
p2 = point(4,5)
print(p.distance(p2)) #2.8284271247461903
print(p.distance_from_origin()) #3.605551275463989 
print(p) #<2, 3> 
l1= line(2,3,5) 
l1.is_point_on_line(p)
s = l1.shortest_distance(p)
print(s) 

p = Person("Vanshika", "India")
p.greet()
p.gender= "Female" 
#you can add attributes to an object even if they are not defined in the class 
print(p.gender) 

#reference variable is a variable that holds the reference to the object in memory
#creating another reference variable for the same object
p = Person("Vanshika", "India")
p2 = p
print(p) 
print(p2)
print(id(p))
print(id(p2)) #same se p and p2 are reference variables for the same object in memory



