# ===============================
# 1. KHỞI TẠO DICTIONARY
# ===============================

# Dictionary lưu thông tin sinh viên
student = {
    "id": "SV001",
    "name": "Nguyen Van A",
    "age": 20,
    "major": "CNTT"
}

print("Student:", student)


# ===============================
# 2. TRUY CẬP GIÁ TRỊ
# ===============================

print("\n--- Truy cập ---")
print("Tên:", student["name"])
print("Tuổi:", student.get("age"))  # an toàn hơn


# ===============================
# 3. THÊM PHẦN TỬ
# ===============================

print("\n--- Thêm ---")
student["gpa"] = 3.5
print(student)


# ===============================
# 4. CẬP NHẬT GIÁ TRỊ
# ===============================

print("\n--- Cập nhật ---")
student["age"] = 21
print(student)


# ===============================
# 5. XÓA PHẦN TỬ
# ===============================

print("\n--- Xóa ---")
student.pop("major")   # xóa theo key
print(student)

# xóa phần tử cuối
student.popitem()
print(student)


# ===============================
# 6. DUYỆT DICTIONARY
# ===============================

print("\n--- Duyệt ---")

# duyệt key
for key in student:
    print("Key:", key)

# duyệt value
for value in student.values():
    print("Value:", value)

# duyệt cả key và value
for key, value in student.items():
    print(key, ":", value)


# ===============================
# 7. KIỂM TRA KEY
# ===============================

print("\n--- Kiểm tra ---")
if "name" in student:
    print("Có key name")


# ===============================
# 8. ĐỘ DÀI
# ===============================

print("\n--- Độ dài ---")
print("Số phần tử:", len(student))


# ===============================
# 9. SAO CHÉP DICTIONARY
# ===============================

print("\n--- Sao chép ---")
student_copy = student.copy()
print("Bản sao:", student_copy)


# ===============================
# 10. XÓA TOÀN BỘ
# ===============================

print("\n--- Xóa toàn bộ ---")
student_copy.clear()
print(student_copy)


# ===============================
# 11. DICTIONARY LỒNG
# ===============================

print("\n--- Dictionary lồng ---")

students = {
    "SV001": {"name": "A", "age": 20},
    "SV002": {"name": "B", "age": 21}
}

print(students)
print("Tên SV001:", students["SV001"]["name"])