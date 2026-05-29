tong_san_pham = 0
so_thung_hop_le = 0

while True:
    so_luong = int(input("Nhập số lượng sản phẩm của thùng: "))
    
    if so_luong < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        continue
    elif so_luong == 0:
        print("Đã kiểm đếm xong!")
        break
    else:
        tong_san_pham += so_luong
        so_thung_hop_le += 1

print("Tổng số thùng hàng hợp lệ đã đếm:", so_thung_hop_le)
print("Tổng số lượng sản phẩm thu được:", tong_san_pham)
