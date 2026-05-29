print("==== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ====")

name = input("Nhập họ tên bệnh nhân: ").strip()
patient_id = input("Nhập mã bệnh án: ").strip().upper()
department = input("Nhập khoa/phòng khám: ").strip()

print("     PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("="*40)

print(f"Họ tên bệnh nhân : {name}")
print(f"Mã bệnh án       : {patient_id}")
print(f"Khoa khám        : {department}")

print("Tiếp nhận thành công!")


