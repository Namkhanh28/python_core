while True:
    print("--- BẮT ĐẦU CHƯƠNG TRÌNH ---")
    employee_number = input("Nhập số lượng nhân viên cần quản lý: ")
    number = int(employee_number)

    for i in range(number):
        print("----------------------------")
        print("Nhập thông tin cho nhân viên tiếp theo:")
        name = input("Nhập tên nhân viên: ")
        days = int(input("Nhập số ngày đi làm:"))
        print(f" Bạn vừa nhập: Nhân viên {name}")
        print(f"Số ngày là {days}")

        if days < 20:
            print("-> Đánh giá: Cần cải thiện chuyên cần")
        else:
            print("-> Đánh giá: Nhân viên chuyên cần tốt")

    print("----------------------------")
    answer = input("Bạn có muốn nhập tiếp cho đợt khác không? (y/n): ")
    
    if answer == "n":
        print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        break 