a=int(input("Tieu thu="))
if   a<=100:
    b=a*550
elif a<=150:
    b=100*550+(a-100)*750
elif a<=200:
    b=100*550+50*750+(a-150)*950
else: 
    b=100*550+50*750+50*950+(a-200)*1350
T=float((1/10)*b)
print("Phai tra=",float(b+T))
          