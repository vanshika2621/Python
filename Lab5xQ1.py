'''List Comprehension is a concise way to create lists. It consists of brackets
containing an expression followed by a for clause, then zero or more for or if clauses.
The expressions can be anything, you can put in all kinds of objects in lists. ''' 

#List Comprehension
#newlist = [expression for item in iterable if condition == True]
L1 = [1,2,3,4,5]
L2 = [x for x in L1 if x%2 == 0]
print(L2)

''' List comprehension provides a concise way to create lists 
Avantages of List Comprehension:
1.More time and space efficient than traditional for loop.
2. Require fewer lines of code to create a new list.
3. It transforms iterative statements into a formula.'''

#Append using list comprehension
L4 = [i for i in range(1,11)]
print(L4)

#scalar multiplication on a vector using list comprehension
L5 = [1,2,3,4,5]
s = 4
L6 = [i*s for i in L5]
print(L6) 

#square of every element in a list using list comprehension
L7 = [1,2,3,4,5]
L8 = [i**2 for i in L7]
print(L8) 

#All the numbers divisible by 5 and range 1 to 50 using list comprehension
L9 = [i for i in range(1,51) if i%5 == 0] 
print(L9)

#Find all the languages starting with 'P' from a list of languages using list comprehension
languages = ['c','java','Python','perl','php', 'javascript']
L10 = [i for i in languages if i.startswith('P') or i.startswith('p')] 
print(L10)

#append fruits in basket which are not present in basket from my_fruit which starts with 'a' using list comprehension
basket = ['apple','banana','guava','cherry','orange']
my_fruit = ['apple', 'kiwi', 'grapes', 'banana', 'avocado']
L11 = [i for i in my_fruit if (i.startswith('a')  or i.startswith("A")) and i not in basket]
basket.extend(L11)
print(basket)

#print 3x3 matrix using list comprehension 
matrix = [[i for i in range(1,4)] for j in range(3)]
print(matrix)  

#Multiply the similar indexes of two given lists using list comprehension 
L12 = [1,2,3,4]
L13 = [5,6,7,8] 
L14 = [[i* j for i in L12] for j in L13]
print(L14) 

#make pair of elements of two lists having same indexes 
L15 = [(i,j) for i in L12 for j in L13 if L12.index(i) == L13.index(j)]
print(L15) 
#can also use zip function 
list(zip(L12,L13))

# change in orginial but copy doesn't change 
a = [1,2,3,4]
b = a.copy() #shallow copy
print(a)
print(b)

a.append(5)
print(a)
print(b)

