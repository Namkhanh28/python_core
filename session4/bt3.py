
so_luong = int(input("Nhập số lượng hóa đơn trong ca: "))
max_hd = -1
min_hd = float('inf')

for i in range(1, so_luong + 1):
    gia_tri = int(input(f"Nhập giá trị hóa đơn {i}: "))

    if gia_tri > max_hd:
        max_hd = gia_tri

    if gia_tri < min_hd:
        min_hd = gia_tri

# In kết quả
print("\n===== KẾT QUẢ =====")
print("Hóa đơn lớn nhất:", max_hd)
print("Hóa đơn nhỏ nhất:", min_hd)