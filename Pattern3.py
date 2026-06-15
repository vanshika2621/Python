''' Pattern 
1
121
12321
1234321
123454321 '''

for i in range(1,6):
    for j in range(1,i):
        print(j,end="")
    for k in range(i-1, 0 , -1):
        print(k, end="")
    print() 