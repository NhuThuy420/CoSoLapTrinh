Toan=int(input())
Ly=int(input())
Hoa=int(input())
ĐTB=(Toan*2+Ly*3+Hoa)/6
if ĐTB<3:
    print("Kem")
elif (ĐTB>=3 and ĐTB<5):
    print("Yeu")
elif (ĐTB>=5 and ĐTB<6):
    print("Trung binh")
elif (ĐTB>=6 and ĐTB<7):
    print("Trung binh Kha")
elif (ĐTB>=7 and ĐTB<8):
    print("Kha")
elif (ĐTB>=8 and ĐTB<9):
    print("Gioi")
else:
    print("Xuat xac")