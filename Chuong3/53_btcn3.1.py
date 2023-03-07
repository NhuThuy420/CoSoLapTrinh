import math


a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
if (a+b)>c:
    (a+c)>b
    (b+c)>a
    print ("Dien tich=",round(S,3))
else:
    print("Khong hop le")