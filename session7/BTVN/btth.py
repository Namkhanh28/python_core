raw_input = "   nGuyen vaN aN  ;  2006   "

# tao menu
while True:
    print()
    print("\n ===== HỆ THỐNG XỬ LÝ THANH VIEN ===== ")
    print("1. Hiển thị chuỗi dữ lieu goc")
    print("2. Chuẩn hoa Ho ten va tinh Tuổi")
    print("3. Tao Ma ID va Email tự động")
    print("4. Thoat chương trình")
    print("======================================")
    print()
    choice = input("Nhập lựa chọn của bạn (1-4): ")
    print()

    if choice == "1":
        print(f"Chuoi du lieu hien tai: \n {raw_input}")

    elif choice == "2":
        data_revert = raw_input.strip().split(";");
        print("data_revert: ",data_revert) 
        full_name = data_revert[0].strip().title()
        birth_date = data_revert[1].strip()
        age = 2026 - int(birth_date)
        print("")
        print("ho va ten: ",full_name)
        print("name sinh: ",age)
    elif choice == "3":
        data_revert = raw_input.strip().split(";");
        full_name = data_revert[0].strip().title()
        birth_date = data_revert[1].strip()
        sur_name = full_name.split(" ")[0]
        mid_name = full_name.split(" ")[1]
        main_name = full_name.split(" ")[2]
        Email = sur_name[0].lower()+mid_name[0].lower()+main_name.lower()+"@company.com"
        main_id = main_name.upper() + birth_date[-2:]
        print("======================================")
        print(" HỆ THỐNG XỬ LÝ THÀNH VIÊN ")
        print("======================================")
        print("Họ và tên:", full_name)
        print("ID: ", main_id)
        print("Email: ", Email)
        print("======================================")
    elif choice == "4":
        print("Chuong trinh da dung!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")  