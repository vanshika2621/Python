a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area =", area)
