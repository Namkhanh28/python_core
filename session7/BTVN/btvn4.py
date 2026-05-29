print("===== HỆ THỐNG CHUẨN HÓA MÃ ĐĂNG KÝ KHÓA HỌC =====")
amount = int(input("Nhập số lượng phiếu đăng ký: "))
if amount <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
    print("Chương trình kết thúc")
else:
    for i in range(1, amount + 1):
        print(f"\nNhập phiếu đăng ký thứ {i}")
        raw_data = input("Nhập dữ liệu: ")
        parts = raw_data.strip().split("|")
        
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()
        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirm_code = student_code + "_" + course_name.upper().replace(" ", "-")
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirm_code)