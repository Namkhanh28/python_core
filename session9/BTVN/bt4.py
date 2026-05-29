order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    print("==================================================")
    
    main_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if main_choice == "1":
        print("\n--- DANH SÁCH ĐƠN HÀNG HIỆN TẠI ---")
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
                
    elif main_choice == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")
            print("---------------------------------------")
            
            sub_choice = input("Nhập lựa chọn cập nhật (1-4): ").strip()
            
            if sub_choice == "1":
                order_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                status = input("Nhập trạng thái đơn hàng (PENDING/DELIVERING/COMPLETED/CANCELLED): ").strip().upper()
                
                if order_code == "" or status == "":
                    print("Lỗi: Mã đơn hàng và trạng thái không được để trống!")
                else:
                    new_order = f"{order_code} - {status}"
                    order_list.append(new_order)
                    print(f"Thành công: Đã thêm đơn hàng '{new_order}' vào cuối danh sách.")
          
            elif sub_choice == "2":
                raw_position = input("Nhập vị trí đơn hàng cần sửa: ").strip()
                
                if not raw_position.isdigit():
                    print("Vị trí không hợp lệ! (Phải nhập ký tự số)")
                else:
                    index = int(raw_position) - 1
                    if 0 <= index < len(order_list):
                        new_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                        new_status = input("Nhập trạng thái mới: ").strip().upper()
                        
                        if new_code == "" or new_status == "":
                            print("Lỗi: Không được để dữ liệu trống khi sửa!")
                        else:
                            order_list[index] = f"{new_code} - {new_status}"
                            print(f"Thành công: Đã cập nhật đơn hàng tại vị trí {raw_position}.")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
            
            elif sub_choice == "3":
                raw_position = input("Nhập vị trí đơn hàng cần xóa: ").strip()
                
                if not raw_position.isdigit():
                    print("Vị trí không hợp lệ! (Phải nhập ký tự số)")
                else:
                    index = int(raw_position) - 1
         
                    if 0 <= index < len(order_list):
                        removed_order = order_list.pop(index)
                        print(f"Thành công: Đã xóa đơn hàng: {removed_order}")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
            
            elif sub_choice == "4":
                print("Quay trở lại Menu chính...")
                break 
                
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                
    elif main_choice == "3":
        count_pending = 0
        count_delivering = 0
        count_completed = 0
        count_cancelled = 0
        
        for order in order_list:
            if " - " in order:
       
                parts = order.split(" - ")
                status_part = parts[1]
                
                if status_part == "PENDING":
                    count_pending += 1
                elif status_part == "DELIVERING":
                    count_delivering += 1
                elif status_part == "COMPLETED":
                    count_completed += 1
                elif status_part == "CANCELLED":
                    count_cancelled += 1
                    
        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {count_pending}")
        print(f"DELIVERING: {count_delivering}")
        print(f"COMPLETED: {count_completed}")
        print(f"CANCELLED: {count_cancelled}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        print("=============================")
        
    elif main_choice == "4":
        print("\nThoát chương trình. Hệ thống vận hành Grab Express tạm dừng!")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")