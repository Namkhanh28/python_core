# ===============================
# 1. KHỞI TẠO TUPLE
# ===============================

# Tuple chứa thông tin sản phẩm
product = ("SP001", "Áo polo", 299000)

# Tuple chứa nhiều số
numbers = (1, 2, 3, 4, 5)

# Tuple 1 phần tử (phải có dấu phẩy)
single = (10,)

print("Product:", product)
print("Numbers:", numbers)
print("Single element:", single)


# ===============================
# 2. TRUY CẬP PHẦN TỬ
# ===============================

print("\n--- Truy cập phần tử ---")
print("Mã sản phẩm:", product[0])
print("Tên sản phẩm:", product[1])
print("Giá:", product[2])


# ===============================
# 3. DUYỆT TUPLE
# ===============================

print("\n--- Duyệt tuple ---")
for item in product:
    print(item)


# ===============================
# 4. KIỂM TRA PHẦN TỬ
# ===============================

print("\n--- Kiểm tra phần tử ---")
if "Áo polo" in product:
    print("Có sản phẩm Áo polo")


# ===============================
# 5. ĐỘ DÀI TUPLE
# ===============================

print("\n--- Độ dài tuple ---")
print("Số phần tử:", len(product))


# ===============================
# 6. NỐI TUPLE
# ===============================

print("\n--- Nối tuple ---")
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print("Tuple sau khi nối:", t3)


# ===============================
# 7. NHÂN TUPLE
# ===============================

print("\n--- Nhân tuple ---")
t = ("A", "B")
print("Tuple sau khi nhân:", t * 3)


# ===============================
# 8. CHUYỂN ĐỔI TUPLE <-> LIST
# ===============================

print("\n--- Chuyển đổi ---")

# Tuple -> List (để sửa)
temp = list(product)
temp[2] = 350000  # thay đổi giá

# List -> Tuple
product = tuple(temp)

print("Tuple sau khi cập nhật:", product)


# ===============================
# 9. ĐẾM & TÌM KIẾM
# ===============================

print("\n--- Count & Index ---")

t = (1, 2, 2, 3, 2)
print("Số lần xuất hiện của 2:", t.count(2))
print("Vị trí đầu tiên của 2:", t.index(2))


# ===============================
# 10. UNPACKING TUPLE
# ===============================

print("\n--- Unpacking ---")

id, name, price = product
print("ID:", id)
print("Name:", name)
print("Price:", price)