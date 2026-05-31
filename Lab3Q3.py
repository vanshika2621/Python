'''3). Remove a particular character from a string 
ex: s = "banana" , remove = "a" ,Output: bnn''' 

s = "banana"
result = s.replace('a', "")
print(result)  

# using loop 
s = "banana"
remove = "a"
new_str = ""
for char in s:
    if char != remove:
        new_str += char
print(new_str)
