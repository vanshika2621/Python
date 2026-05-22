class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address 
    def edit_profile(self, new_name, new_age, new_city, new_state, new_pincode):
        self.name = new_name
        self.age = new_age
        self.address.new_address(new_city, new_state, new_pincode)

class Address:
    def __init__(self, city, state, pincode):
        self.city = city 
        self.state = state 
        self.pincode = pincode
    def new_address(self, new_city, new_state, new_pincode):
        self.city = new_city 
        self.state = new_state 
        self.pincode = new_pincode


add = Address("Roorkee", "Uttarakhand", 247667)
cust1 = Customer("Vanshika", 20, add)
print(cust1.name) #Vanshika
print(cust1.age) #20
print(cust1.address.city) #Roorkee
print(cust1.address.state) #Uttarakhand
print(cust1.address.pincode) #247667 

#INHERITANCE 


