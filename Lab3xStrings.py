#Strings
for i in 'delhi':
    print('Dehradun')

#common Functions
'''
len :- Returns length of string
max:- Print the element which has max ascii value
min:- Print the element which has min ascii value
sorted:- Sort the elements in ascending order to print in descending order use reverrse=True
'''
s='Vanshika123'
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))
print(sorted(s,reverse=True))

s='Hello World'
print(s.capitalize()) #Capitalizes first letter of string
print(s.title()) #Capitalizes first letter of each word
print(s.upper()) #Converts all letters to uppercase
print(s.lower()) #Converts all letters to lowercase
print(s.count('o')) #Counts number of occurrences of a substring
print(s.find('o')) #Return the index of first occurence if the given substring is not found it rerturns -1
print(s.index('o')) #Return the index of first occurence if the given substring is not found it gives error 

#startswith() and endswith()
print(s.startswith("py")) #Returns True if string starts with given substring else False
print(s.endswith('ld')) #Returns True if string ends with given substring else False

#format
name = "Vanshika Giri"
age = 18 
print("Hi my name is {} and my age is {}".format(name,age)) #Positional Formatting
print("Hi my name is {n} and my age is {a}".format(a=age,n=name)) #Keyword Formatting 
print(f"Hi my name is {name} and my age is {age}") #f-String Formatting 
print("Hi my name is %s and my age is %d"%(name,age)) #Old Style Formatting

#isalnum / isalpha / isdigit / islower / isupper / isspace / istitle / isidentifier
s1="Vanshika123"
s2="Vanshika"
s3="12345"      
print(s1.isalnum()) #Returns True if all characters are alphanumeric
print(s2.isalpha()) #Returns True if all characters are alphabetic
print(s3.isdigit()) #Returns True if all characters are digits
print(s2.islower()) #Returns True if all characters are lowercase
print(s2.isupper()) #Returns True if all characters are uppercase
print("   ".isspace()) #Returns True if all characters are whitespace       
print("Vanshika Giri".istitle()) #Returns True if string follows title case
print("var_1".isidentifier()) #Returns True if string is a valid identifier

#uppercase / lowercase / swapcase
s="Hello World"
print(s.uppercase()) #Converts all characters to uppercase
print(s.lowercase()) #Converts all characters to lowercase
print(s.swapcase()) #Swaps the case of all characters

#split / join
s4 = "Welcome to Dehradun"
print(s4.split()) #Splits the string into a list of substrings based on whitespace
print('-'.join(['Welcome', 'to', 'Dehradun'])) #Joins the list of strings into a single string with '-' as separatorm

#replace
s5 = "I love apples"
print(s5.replace("apples", "oranges")) #Replaces all occurrences of 'apples' with 'oranges'

#strip / lstrip / rstrip
s6 = "   Hello World   "
print(s6.strip()) #Removes leading and trailing whitespace
print(s6.lstrip()) #Removes leading whitespace
print(s6.rstrip()) #Removes trailing whitespace 

