order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    print("==================================================")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if user_choice == "1":
        print("\n--- DANH SÁCH ĐƠN HÀNG ---")
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
           
            for index, order_code in enumerate(order_list, start=1):
                print(f"{index}. {order_code}")
                
    elif user_choice == "2":
        raw_order_code = input("Nhập mã đơn hàng mới: ")
        
        clean_order_code = raw_order_code.strip().upper()
        
        if clean_order_code == "":
            print("Lỗi: Mã đơn hàng không được để trống!")
        else:
            order_list.append(clean_order_code)
            print(f"Thành công: Đã thêm đơn hàng '{clean_order_code}' vào hệ thống.")
            
    elif user_choice == "3":
        raw_order_code = input("Nhập mã đơn hàng cần xóa: ")
        
        clean_order_code = raw_order_code.strip().upper()
        
        if clean_order_code in order_list:
            order_list.remove(clean_order_code)
            print(f"Thành công: Đã xóa đơn hàng '{clean_order_code}' khỏi hệ thống.")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")
            
    elif user_choice == "4":
        print("\nThoát chương trình. Cảm ơn bạn đã sử dụng dịch vụ Grab Express!")
        break  

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")