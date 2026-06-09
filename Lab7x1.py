#define a function g of x 
def g(x):
    def h(x):
        x = x+1
    x = x+1 
    print("in g(x): x - ", x)
    h(x)
    return x

x= 3
z = g(x)
print(z) 

#functions are 1st class citizens 
#lambda function: 
''' Lambda fucntion is small ananomous function, it can take any number of arguements and but 
can only have one expression. It is used when we need a small function for a short period of time. It is also used when we want to pass a function as an argument to another function. 
 It'''
#syntax: lambda arguments: expression 
#example:
a = lambda a,b: a+b 
x = lambda x : x**2
b = lambda x: x/3
c = lambda x: x%2 == 0
print(a(2,3))
print(x(5)) 
print(b(9))
print(c(4))

#Diffrence between a normal function and a lambda function:
''' A normal function is defined using the def keyword and has a name, 
while a lambda function is defined using the lambda keyword and does not have a name.
Lambda function is not used for reuseablity 
we use it along higher order function (function which returns a function itself)
A normal function can have multiple expressions and statements, while a lambda function can only have one expression.
A normal function can be called multiple times, while a lambda function is usually used for a short period of time and is not called multiple times.
A normal function can be assigned to a variable, while a lambda function cannot be assigned to a variable. ''' 

#to check whether a string's 1st function is "a"
check = lambda s: s[0] == "a"
print(check("apple"))
print(check("banana")) 

#write a lambda function of check if a number is even or odd
check2 = lambda v: "Even" if v%2 == 0  else "odd"
print(check2(4))
print(check2(7)) 

#function 
def square(x):
    return x**2
def transform(f, L):
    output = []
    for i in L:
        output.append(f(i))
    print(output)

L =[1,2,3,4,5]
transform(square, L) 

#doing same using lambda function 
transform(lambda x: x**2, L) 

def return_sum(func ,L):
    result = 0
    for i in L:
        if func(i):
            result += i
    return result 
L = [11,14,21,23,56,78,45,29,28]

X = lambda x: x%2 == 0
Y = lambda x: x%2 != 0 
Z = lambda x: x%3 == 0 
print(return_sum(X, L))
print(return_sum(Y, L)) 










