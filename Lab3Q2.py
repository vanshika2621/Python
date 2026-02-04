''' Extract username from an email entered by user '''

e = "Vanshikagiri2020@gmail.com "
username = e.split('@')
print("Username is: ", username[0])

#using loop 
e = "" 
e = str(input("Enter your email: "))
username = ""
for char in e:
    if char == '@':
        break
    else:
        username += char

print("Username is: ", username) 

#using slicing
e = ""
e = str(input("Enter your email: "))
at_index = e.index('@')
username = e[:at_index]
print("Username is: ", username)
