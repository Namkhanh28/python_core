print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")

name = input("Nhập họ tên bệnh nhân: ")

if name == "":
    print("LỖI: Tên không hợp lệ!")
age = int(input("Nhập tuổi bệnh nhân: "))
if age < 0 or age > 150:
    print("LỖI: Tuổi nằm ngoài phạm vi con người (0-150)!")
    exit()
if age < 6:
    result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif age >= 80:
    result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print("\n--- PHIẾU KHÁM BỆNH ---")
print(f"Tên: {name}")
print(f"Tuổi: {age}")
print(f"Kết quả: {result}")