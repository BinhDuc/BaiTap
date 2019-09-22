import quanlyuser,quanlyhoadon
quanlyuser.login_user()
print("+--------------MENU-----------------+")
print("|Chon THH de tao hang hoa           |")
print("|Chon XHH de xem hang hoa           |")
print("|Chon TLH de tao loai hang hoa      |")
print("|Chon XLH de xem loai hang hoa      |")
print("|Chon THD de tao hoa don            |")
print("|Chon IHD de xem thong tin hoa don  |")
print("|Chon TU de tao user                |")
print("|Chon XU de xem user                |")
print("|Chon D de xoa user                 |")
print("|Chon T de xem tong hang hoa ban ra |")
print("|Chon A de xem tong doanh thu       |")
print("|Chon E de thoat                    |")
print("+-----------------------------------+")

while True:
    x=input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x.upper() == 'TLH':
      quanlyhoadon.tao_loaihanghoa()
    if x.upper() == 'XLH':
      quanlyhoadon.xem_loaihanghoa()
    if x.upper() == 'THH':
      quanlyhoadon.tao_hanghoa()
    if x.upper() == 'XHH':
        quanlyhoadon.xem_hanghoa()
    if x.upper() == 'THD':
        quanlyhoadon.tao_hoadon()
    if x.upper() == 'IHD':
        quanlyhoadon.in_hoadon()
    if x.upper() == 'TU':
        quanlyhuser.tao_user()
    if x.upper() == 'XU':
        quanlyuser.xem_user()
    if x.upper() == 'D':
        quanlyuser.delete_user()
    if x.upper() == 'T':
        quanlyhoadon.tonghanghoabanra()
    if x.upper() == 'A':
        quanlyhoadon.tongdoanhthu()
    if x.upper() == 'E':
        print("Tam biet! Hen gap lai")
        break
