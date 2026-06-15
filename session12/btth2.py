saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình 

Mời chọn chức năng:''').strip()
    match choice:
        case "1":
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")
                stt = 1
                for acc in saving_accounts:
                    print(f"{stt}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | "
                          f"Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | "
                          f"Lại suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                    stt += 1

        case "2":
            print("\n--- MỞ SỔ TIẾT KIỆM MỚI ---")
            account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    print("Mã sổ tiết kiệm đã tồn tại!")
                    break
            else:
                customer_name = input("Nhập tên khách hàng: ").strip()
                
                if customer_name == "":
                    print("Tên khách hàng không được để trống")
                    continue
                    
                str_balance = input("Nhập số tiền gửi: ").strip()
                str_term = input("Nhập kỳ hạn gửi theo tháng: ").strip()
                
                if not str_balance.isdigit() or not str_term.isdigit():
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue
                    
                balance = int(str_balance)
                term_months = int(str_term)
                if balance <= 0 or term_months <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue
                    
                str_rate = input("Nhập lãi suất năm: ").strip()
                
                is_float = False
                parts = str_rate.split('.')
                if len(parts) == 1 and parts[0].isdigit():
                    is_float = True
                elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    is_float = True
                    
                if not is_float or float(str_rate) <= 0:
                    print("Lãi suất không hợp lệ!")
                    continue
                    
                interest_rate = float(str_rate)
                
                new_account = {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": balance,
                    "term_months": term_months,
                    "interest_rate": interest_rate,
                    "status": "active"
                }
                saving_accounts.append(new_account)
                print(f"Mở sổ tiết kiệm {account_id} thành công!")

        case "3":
            print("\n--- CẬP NHẬT THÔNG TIN SỔ TIẾT KIỆM ---")
            account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
  
                    if acc["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                        
                    new_name = input("Nhập tên khách hàng mới: ").strip()
                    if new_name == "":
                        print("Tên khách hàng không được để trống")
                        break
                        
                    str_balance = input("Nhập số tiền gửi mới: ").strip()
                    str_term = input("Nhập kỳ hạn mới theo tháng: ").strip()
                    if not str_balance.isdigit() or not str_term.isdigit():
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break
                    balance = int(str_balance)
                    term_months = int(str_term)
                    if balance <= 0 or term_months <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break
                        
                    str_rate = input("Nhập lãi suất năm mới: ").strip()
                    is_float = False
                    parts = str_rate.split('.')
                    if len(parts) == 1 and parts[0].isdigit():
                        is_float = True
                    elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                        is_float = True
                        
                    if not is_float or float(str_rate) <= 0:
                        print("Lãi suất không hợp lệ!")
                        break
                        
                    acc["customer_name"] = new_name
                    acc["balance"] = balance
                    acc["term_months"] = term_months
                    acc["interest_rate"] = float(str_rate)
                    print(f"Cập nhật thông tin sổ {account_id} thành công!")
                    break
            else:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "4":
            print("\n--- TẤT TOÁN SỔ TIẾT KIỆM ---")
            account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    acc["status"] = "closed"
                    print(f"Tất toán sổ tiết kiệm {account_id} thành công! Trạng thái hiện tại: closed.")
                    break
            else:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "5":
            print("\n--- TÍNH LÃI DỰ KIẾN KHI ĐẾN HẠN ---")
            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    if acc["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                        
                    interest = acc["balance"] * acc["interest_rate"] / 100 * acc["term_months"] / 12
                    total_received = acc["balance"] + interest
                    
                    print(f"Sổ tiết kiệm: {account_id} | Chủ sổ: {acc['customer_name']}")
                    print(f"-> Tiền lãi dự kiến nhận được: {interest:,.1f} VND")
                    print(f"-> Tổng số tiền nhận được khi đến hạn: {total_received:,.1f} VND")
                    break
            else:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "6":
            print("\n--- KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---")
            account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    if acc["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                        
                    str_real_months = input("Nhập số tháng thực gửi: ").strip()
                    
                    if not str_real_months.isdigit() or int(str_real_months) <= 0:
                        print("Số tháng thực gửi không hợp lệ!")
                        break
                        
                    real_months = int(str_real_months)
                    
                    if real_months < acc["term_months"]:
                        applied_rate = 0.5
                        print("[LƯU Ý] Khách hàng rút trước hạn. Áp dụng mức lãi suất không kỳ hạn: 0.5%/năm.")
                    else:
                        applied_rate = acc["interest_rate"]
                        print("[XÁC NHẬN] Khách hàng rút đúng hạn hoặc quá hạn. Áp dụng lãi suất gốc của sổ.")
                        
                    interest_received = acc["balance"] * applied_rate / 100 * real_months / 12
                    total_received = acc["balance"] + interest_received
                    
                    print(f"-> Tiền lãi thực nhận: {interest_received:,.1f} VND")
                    print(f"-> Tổng tiền thực nhận (Gốc + Lãi): {total_received:,.1f} VND")
                    break
            else:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "7":
            print("Cảm ơn bạn đã sử dụng hệ thống TechBank CLI. Hẹn gặp lại!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")