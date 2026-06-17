''' Pattern6
1      1
12    21
123  321
12344321 '''

for i in range(0,6):
    for j in range(1,i):
        print(j,end="")
    for k in range(4, i-1, -1):
        print(" ", end = " ") 
    for p in range(i-1, 0 , -1):
        print(p, end="")

    print()