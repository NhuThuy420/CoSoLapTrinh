a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
list= [a,b,c]
max=a
min=a
for i in list:
    if max < i :
       max=i
    if min > i :
       min=i
print("SLN=",max)
print("SBN=",min)        