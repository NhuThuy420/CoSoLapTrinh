HoTen=input("Ho ten:")
DonGiaNgayCong=int(input("Don gia ngay cong:"))
SoNgayCong=int(input("So ngay cong:"))
HeSoPhuCap=float(input("He so phu cap:"))
TamUng=int(input("Tam ung:"))
Luong= DonGiaNgayCong*SoNgayCong*HeSoPhuCap
ThucLinh=Luong-TamUng
print("Ho ten:",HoTen)
print("Luong:",Luong)
print("TamUng:",TamUng)
print("ThucLinh:",ThucLinh)
print("Nhan vien",HoTen,",Co Tien Luong=",round(Luong,1),",Tam Ung=",TamUng,"va Thuc linh=",round(ThucLinh,1))