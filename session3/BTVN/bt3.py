print("===== HỆ THỐNG NHẬP HỒ SƠ NHÂN VIÊN =====")
for i in range(1,4,1):
    print("\nĐang xử lý nhân viên số:", i)
    employee_id = input("Hãy nhập mã nhân viên của bạn: ")
    employee_name = input("Nhập tên nhân viên: ")
    department_name = input("Nhập phòng ban: ")
    if employee_id== "" or employee_name == "":
        print("----------------------------------")
        print("Mã nhân viên hoặc Họ và tên không hợp lệ!")
        print("----------------------------------")
        continue
    print("-------------------------------")
    print("PHIẾU HỒ SƠ ĐIỆN TỬ")
    print("--------------------------------")
    print("Mã nhân viên :", employee_id)
    print("Họ và tên    :", employee_name)
    print("Phòng ban    :", department_name)
    print("--------------------------------")

print("===== ĐÃ HOÀN THÀNH NHẬP HỒ SƠ =====")