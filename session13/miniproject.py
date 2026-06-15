parking_lot = [
    {"id": 1, "plate": "29A-12345", "type": 2, "entry_time": 8},
    {"id": 2, "plate": "38A-88888", "type": 1, "entry_time": 9}
]

while True:
    print("\n========================================================")
    print("            SMART PARKING MANAGEMENT SYSTEM            ")
    print("========================================================")
    print("1 Check-in (Nhận xe vào bãi)")
    print("2 Báo cáo tồn kho (Danh sách xe đang đỗ)")
    print("3 Tìm kiếm xe theo biển số")
    print("4 Check-out (Tính phí & Xuất bãi)")
    print("5 Thoát chương trình")
    print("========================================================")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            print("\n--- TIẾP NHẬN PHƯƠNG TIỆN (CHECK-IN) ---")
            plate = input("Nhập biển số xe: ").strip().replace(" ", "").upper()
            
            if plate == "":
                print("[Lỗi]: Biển số xe không được để trống!")
                continue
                
            is_duplicated = False
            for vehicle in parking_lot:
                if vehicle["plate"] == plate:
                    is_duplicated = True
                    break
            
            if is_duplicated:
                print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi! (ERR-01)")
                continue
            
            while True:
                str_type = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
                if str_type == "1" or str_type == "2":
                    vehicle_type = int(str_type)
                    break
                else:
                    print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)! (ERR-02)")
            
            while True:
                str_entry = input("Nhập giờ vào bãi (0-24): ").strip()
                if str_entry.isdigit():
                    entry_time = int(str_entry)
                    if 0 <= entry_time <= 24:
                        break
                print("[Lỗi]: Giờ vào phải là số nguyên nằm trong khoảng từ 0 đến 24!")
            
            new_vehicle = {
                "id": len(parking_lot) + 1,
                "plate": plate,
                "type": vehicle_type,
                "entry_time": entry_time
            }
            parking_lot.append(new_vehicle)
            print(f"[Thành công]: Xe [{plate}] đã được đăng ký vào bãi với ID: {new_vehicle['id']}.")

        case "2":
            if len(parking_lot) == 0:
                print("\n[Trạng thái]: Danh sách bãi xe hiện đang trống.")
            else:
                print("\n" + "="*60)
                print(f"{'ID':<6} | {'BIỂN SỐ':<15} | {'LOẠI XE':<12} | {'GIỜ VÀO'}")
                print("-"*60)
                for vehicle in parking_lot:
                    type_name = "Xe máy" if vehicle["type"] == 1 else "Ô tô"
                    print(f"{vehicle['id']:<6} | {vehicle['plate']:<15} | {type_name:<12} | {vehicle['entry_time']}h")
                print("="*60)
                print(f"-> Tổng số lượng xe đang đỗ: {len(parking_lot)}")

        case "3":
            print("\n--- TRUY VẤN THÔNG TIN PHƯƠNG TIỆN ---")
            search_plate = input("Nhập biển số xe cần tìm: ").strip().replace(" ", "").upper()
            
            found = False
            for vehicle in parking_lot:
                if vehicle["plate"] == search_plate:
                    type_name = "Xe máy" if vehicle["type"] == 1 else "Ô tô"
                    print("\n[Thông tin xe]")
                    print(f"ID: {vehicle['id']}")
                    print(f"Biển số: {vehicle['plate']}")
                    print(f"Loại xe: {type_name}")
                    print(f"Giờ vào: {vehicle['entry_time']}h")
                    found = True
                    break
            
            if not found:
                print("[Lỗi]: Không tìm thấy xe trong bãi! (ERR-04)")
        case "5":
            print("\nĐang thoát chương trình... Tạm biệt!")
            break

        case _:
            print("[Lỗi]: Lựa chọn không hợp lệ! (ERR-00)")