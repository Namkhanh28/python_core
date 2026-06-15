
ten_khach_hang = input("Tên khách hàng: ")
ten_san_pham = input("Tên sản phẩm: ")
don_gia = int(input("Đơn giá: "))
so_luong = int(input("Số lượng: "))


thanh_tien = don_gia * so_luong

if thanh_tien >= 100000:
    tien_giam = thanh_tien * 0.1
    thanh_toan = thanh_tien - tien_giam
else:
    tien_giam = 0
    thanh_toan = thanh_tien

print("\n===== HÓA ĐƠN =====")
print(f"Khách hàng: {ten_khach_hang}")
print(f"Sản phẩm: {ten_san_pham}")
print(f"Đơn giá: {don_gia} VNĐ")
print(f"Số lượng: {so_luong}")
print(f"Thành tiền: {thanh_tien} VNĐ")
print(f"Giảm giá: {tien_giam:.0f} VNĐ")
print(f"Thanh toán: {thanh_toan:.0f} VNĐ")
print("==================")