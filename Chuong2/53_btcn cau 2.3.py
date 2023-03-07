import math


a=int(input("Nhap canh ke thu nhat:"))
b=int(input("Nhap canh ke thu hai:"))
x=math.sqrt(a**2+b**2)
print(a)
print(b)
print("Canh huyen: ",x)
print("Canh ke thu nhat la:",a,",canh ke thu hai :",b,",co canh huyen=",round(x,2))