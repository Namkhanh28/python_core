
print("==== KIOSK KHÁM BỆNH TỰ ĐỘNG ====")

patient_name = input("Nhập họ tên bệnh nhân: ")
patient_id = input("Nhập mã bệnh nhân (VD: BN001): ")
age = int(input("Nhập tuổi (ví dụ: 25): "))
temperature =float( input("Nhập nhiệt độ (°C, ví dụ: 37.5): "))
heart_rate =int(input("Nhập nhịp tim (bpm, ví dụ: 80): "))
weight = float(input("Nhập cân nặng (kg, ví dụ: 60.5): "))


print("====PHIẾU KHÁM BỆNH ĐIỆN TỬ======")
print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Mã bệnh nhân: {patient_id}")
print(f"Tuổi: {age}")
print(f"Nhiệt độ: {temperature} °C")
print(f"Nhịp tim : {heart_rate} bpm")
print(f"Cân nặng : {weight} kg")

print("-=========================")
print(" Tiếp nhận thành công!")
print("-=========================")


print("patient_name:", type(patient_name))
print("patient_id:", type(patient_id))
print("age:", type(age))
print("temperature:", type(temperature))
print("heart_rate:", type(heart_rate))
print("weight:", type(weight))