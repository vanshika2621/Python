#WAP to turn string into title without title  keep the spaces too
a = str(input("Enter a String: "))
b = a.split()
for i in range(0,len(b)):
    if b[i][0].islower() :
        b[i] = b[i][0].upper() + b[i][1:]
    

print("String is : ", " ".join(b))