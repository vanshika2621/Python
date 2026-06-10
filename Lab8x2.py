#create one class called fraction and define two attributes numerator and denominator and one method called display that will print the fraction in the form of numerator/denominator
#also create a constructor method that will initialize the attributes of the class 
#Basic Structure of a class
class Fraction:
    def __init__ (self, numerator, denominator): 
        self.numerator = numerator 
        self.denominator = denominator 

    def display(self):
        print(f"{self.numerator}/{self.denominator}") 
#creating an object of the class
my_fraction = Fraction(1, 2)
my_fraction.display() #1/2

#
