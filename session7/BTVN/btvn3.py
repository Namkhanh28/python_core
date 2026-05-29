raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()
    print()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    match choice:
        case "1":
            print("Dữ liệu gốc:", raw_data)

        case "2":
            employees = raw_data.strip().split("|")

            for employee in employees:
                data = employee.strip().split(";")

                employee_id = data[0].strip().upper()
                employee_name = data[1].strip().title()
                phone = data[2].strip().replace("-", "")
                department = data[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[-3:]
                else:
                    phone = "Invalid Format"

                print(f"Mã nhân viên: {employee_id}")
                print(f"Tên nhân viên: {employee_name}")
                print(f"Số điện thoại: {phone}")
                print(f"Văn phòng: {department}")
                print("-" * 30)

        case "3":
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
            found = False

            employees = raw_data.strip().split("|")

            for employee in employees:
                data = employee.strip().split(";")

                employee_id = data[0].strip().upper()
                employee_name = data[1].strip().title()
                phone = data[2].strip().replace("-", "")
                department = data[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[-3:]
                else:
                    phone = "Invalid Format"

                if employee_id == search_id:
                    found = True
                    print("Đã tìm thấy nhân viên")
                    print(f"Mã nhân viên: {employee_id}")
                    print(f"Tên nhân viên: {employee_name}")
                    print(f"Số điện thoại: {phone}")
                    print(f"Văn phòng: {department}")

            if not found:
                print("Không tìm thấy nhân viên")
        case "4":
            print("Chương trình đã dừng!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")