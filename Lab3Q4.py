''' count numbers of words without using split

s = input("Enter a long string : ")
s1= 1
for i in s:
    if i == " ":
        s1 += 1


print("Number of words: ", s1) 


'''
'''count numbers of words without using  Without using any in-built function '''
s = input("Enter a long string : ") 
flag = False
count = 0 
for i in s:
    if i != " " and  not flag:
        count += 1
        flag = True
    elif i == " ":
        flag = False 


print("Number of words: ", count) 