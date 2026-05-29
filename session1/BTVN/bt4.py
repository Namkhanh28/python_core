print("==== HỆ THỐNG NHẬP THÔNG TIN BỆNH NHÂN ====")

patient_id = input("Nhập mã bệnh nhân: ")
temp = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate= int(input("Nhập nhịp tim: "))

print("\n==== THÔNG TIN BỆNH NHÂN ====")
print(f"Mã bệnh nhân : {patient_id}")
print(f"Nhiệt độ     : {temp} °C")
print(f"Nhịp tim     : {heart_rate} bpm")

print("\n==== KIỂM TRA KIỂU DỮ LIỆU ====")
print("Kiểu nhiệt độ:", type(temp))
print("Kiểu nhịp tim:", type(heart_rate))