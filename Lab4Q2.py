#Lists addreessz: Lists stores address of it's element 

L =[1,2,"Hello",3.5]
print(id(L))
print(id(L[0]))
print(id(L[2]))
print(id(L[3]))

'''Characteristics of list:
1. Lists are ordered.
2. Lists are mutable.
3. Lists can contain duplicate elements.
4. Lists can contain elements of different data type.
5. Lists are dynamic.
6. Lists support various operations.
7. Lists can be nested.''' 

L1 = [1,2 ,[3,4],5] #Nested list
print(L1[2][0]) #Accessing element of nested list
L1[2][0] = 10 #Modifying element of nested list
print(L1)
 #append() method is used to add an element at the end of the list
L1.append(6)
print(L1)
#insert() method is used to add an element at a specific position in the list
L1.insert(2,7)
print(L1)

#extend() method is used to add multiple elements at the end of the list
L1.extend([8,9])
print(L1)

#Remove() method is used to delete an element from the list
L1.remove(7)
print(L1)
#pop() method is used to delete an element from the list and return it
print(L1.pop(2))
print(L1)
#del keyword is used to delete an element from the list
del L1[2]
print(L1)
#clear() method is used to delete all the elements from the list
L1.clear()
print(L1)

#reverse() method is used to reverse the order of the elements in the list, permanently
L2 = [1,2,3,4,5]
L2.reverse()
print(L2)
#sort() method is used to sort the elements in the list(gives permannat changes in the list)
L3 = [5,4,3,2,1]
L3.sort()
print(L3) 
#sorted() function is used to sort the elements in the list and return a new sorted list
L4 = [5,4,3,2,1]
L5 = sorted(L4)
print(L5)
