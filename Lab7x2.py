#MAP function 
#syntax: map(function, iterable, ...)
#finding the length of each word in a list

def myfunc(n):
    return len(n) 

x = map(myfunc, ["apple", "banana", "cherry"])
print(x)
print(list(x)) 

#using lambda function
x = map(lambda n: len(n), ["apple", "banana", "cherry"])
print(list(x)) 

#odd even 
y = list(map(lambda n: "even"if n%2 == 0 else "odd", [1,2,3,4,5,6])) 

#fetch name from a list of dictionary
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
names = list(map(lambda person: person["name"], people))

#FILTER 
#syntax : filter(function, iterable)
#filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers)

#fetch fruits who starts with letter "a " 

fruits = ["apple", "banana", "cherry", "avocado", "grape"]
z = list(filter(lambda x :x.startswith("a"), fruits))
print(z) 

#reduce function 
import functools
#syntax: functools.reduce(function, iterable[, initializer]) 
#find the product of all numbers in a list
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product)
#maximum number in a list
numbers = [1, 2, 3, 4, 5]
max_number = functools.reduce(lambda x, y: x if x > y else y, numbers)
print(max_number) 

