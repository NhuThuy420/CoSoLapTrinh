M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<=100:
    a=S*M1
elif S<=150:
    a=100*M1+(S-100)*M2
else:
    a=100*M1+50*M2+(S-150)*M3
print("Phai tra=",a)