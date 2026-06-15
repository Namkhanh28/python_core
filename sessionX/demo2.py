# Khởi tạo dữ liệu mẫu ban đầu (List of Dictionaries)
orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]

# -------------------------------------------------------------------------
# 1. HÀM HIỂN THỊ DANH SÁCH ĐƠN HÀNG
# -------------------------------------------------------------------------
def display_orders(order_list):
    """Duyệt qua danh sách đơn hàng để hiển thị dạng bảng căn lề thẳng hàng."""
    if not order_list:
        print("\n[THÔNG BÁO]: Danh sách đơn hàng hiện đang trống.")
        return
    
    print("\n" + "="*70)
    # Căn lề: id (10 ký tự), name (25 ký tự), price (15 ký tự, căn phải), status (10 ký tự)
    print(f"{'Mã ĐH':<10}{'Tên Đại Lý':<25}{'Giá Trị (VND)':>15}   {'Trạng Thái':<10}")
    print("-" * 70)
    
    for order in order_list:
        print(f"{order['id']:<10}{order['name']:<25}{order['price']:>15,}   {order['status']:<10}")
    print("="*70 + "\n")

# -------------------------------------------------------------------------
# 2. HÀM THÊM MỚI ĐƠN HÀNG
# -------------------------------------------------------------------------
def add_order(order_list):
    """Thu thập, validate dữ liệu và thêm đơn hàng mới vào danh sách gốc."""
    print("\n--- THÊM MỚI ĐƠN HÀNG ---")
    
    # Nhập và kiểm tra Mã đơn hàng
    while True:
        order_id = input("Nhập mã đơn hàng: ").strip()
        if not order_id:
            print("Lỗi: Mã đơn hàng không được để trống. Vui lòng nhập lại!")
            continue
        
        # Kiểm tra trùng mã (ERR-01)
        is_duplicate = False
        for order in order_list:
            if order['id'].upper() == order_id.upper():
                is_duplicate = True
                break
        
        if is_duplicate:
            print(f"[ERR-01]: Mã đơn hàng '{order_id}' đã tồn tại! Hủy thao tác.")
            return # Thoát hàm, không thêm nữa
        break # Mã hợp lệ, thoát vòng lặp nhập mã
            
    # Nhập và kiểm tra Tên đại lý
    while True:
        name = input("Nhập tên đại lý: ").strip()
        if not name:
            print("Lỗi: Tên đại lý không được để trống. Vui lòng nhập lại!")
            continue
        break

    # Nhập và kiểm tra Giá trị đơn hàng (Xử lý bẫy lỗi try-except)
    while True:
        try:
            price = int(input("Nhập giá trị đơn hàng (VND): "))
            if price <= 0:
                print("Lỗi: Giá trị đơn hàng phải lớn hơn 0. Vui lòng nhập lại!")
                continue
            break # Thỏa mãn điều kiện, thoát vòng lặp nhập tiền
        except ValueError:
            print("Lỗi: Giá trị đơn hàng phải là một số nguyên hợp lệ! Vui lòng nhập lại.")

    # Tạo dictionary đơn hàng mới (mặc định trạng thái Unpaid)
    new_order = {
        'id': order_id,
        'name': name,
        'price': price,
        'status': 'Unpaid'
    }
    
    # Thêm trực tiếp vào danh sách gốc
    order_list.append(new_order)
    print(f"Chúc mừng: Thêm mới đơn hàng '{order_id}' thành công!")

# -------------------------------------------------------------------------
# 3. HÀM CẬP NHẬT TRẠNG THÁI THANH TOÁN
# -------------------------------------------------------------------------
def update_order_status(order_list):
    """Tìm kiếm đơn hàng theo mã và cập nhật trạng thái từ Unpaid sang Paid."""
    print("\n--- CẬP NHẬT TRẠNG THÁI THANH TOÁN ---")
    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
    
    # Tìm kiếm đơn hàng trong danh sách
    found_order = None
    for order in order_list:
        if order['id'].upper() == order_id.upper():
            found_order = order
            break
            
    # Nếu không tìm thấy mã đơn hàng (ERR-03)
    if found_order is None:
        print(f"[ERR-03]: Không tìm thấy mã đơn hàng '{order_id}' trong hệ thống.")
        return

    # Nếu tìm thấy, kiểm tra trạng thái hiện tại
    if found_order['status'] == 'Paid':
        print(f"[ERR-04]: Đơn hàng '{order_id}' đã ở trạng thái 'Paid' từ trước.")
    elif found_order['status'] == 'Unpaid':
        found_order['status'] = 'Paid'
        print(f"Thành công: Đơn hàng '{order_id}' đã được chuyển sang trạng thái 'Paid'.")

# -------------------------------------------------------------------------
# 4. HÀM TÍNH TOÁN DOANH THU (CHỈ TÍNH VÀ RETURN TUPLE)
# -------------------------------------------------------------------------
def calculate_revenue(order_list):
    """
    Tính tổng doanh thu từ các đơn hàng 'Paid'.
    Trả về bộ giá trị (Tuple): (tổng doanh thu, phần trăm chiết khấu, tiền chiết khấu)
    """
    total_revenue = 0
    
    # Chỉ cộng dồn các đơn hàng đã thanh toán (Paid)
    for order in order_list:
        if order['status'] == 'Paid':
            total_revenue += order['price']
            
    # Áp dụng quy tắc chiết khấu
    if total_revenue >= 100000000: # Từ 100 triệu trở lên
        discount_percent = 5
    else:
        discount_percent = 0
        
    discount_amount = int(total_revenue * (discount_percent / 100))
    
    # Trả về một Tuple chứa 3 giá trị theo đúng yêu cầu đặc tả
    return (total_revenue, discount_percent, discount_amount)

# -------------------------------------------------------------------------
# 5. HÀM ĐIỀU PHỐI CHÍNH (MAIN)
# -------------------------------------------------------------------------
def main():
    """Hàm chạy chính, quản lý vòng lặp Menu và điều phối chức năng."""
    while True:
        print("\n" + "="*20 + " MENU QUẢN LÝ " + "="*20)
        print("1. Xem danh sách đơn hàng đại lý")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán đơn hàng")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")
        print("="*54)
        
        # Bắt lỗi try-except khi người dùng nhập lựa chọn menu
        try:
            choice = int(input("Mời bạn chọn chức năng (1-5): "))
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập các số nguyên từ 1 đến 5!")
            continue # Quay lại đầu vòng lặp menu
            
        # Rẽ nhánh xử lý dựa trên lựa chọn của người dùng
        if choice == 1:
            display_orders(orders)
        elif choice == 2:
            add_order(orders)
        elif choice == 3:
            update_order_status(orders)
        elif choice == 4:
            # Nhận giá trị trả về từ hàm tính toán (Tuple)
            total, percent, discount = calculate_revenue(orders)
            
            # In kết quả ra màn hình tại nơi gọi hàm (hàm main)
            print("\n--- BÁO CÁO DOANH THU & CHIẾT KHẤU ---")
            print(f"Tổng doanh thu thực tế (Paid) : {total:,} VND")
            print(f"Tỷ lệ chiết khấu áp dụng     : {percent}%")
            print(f"Số tiền chiết khấu           : {discount:,} VND")
            print("-" * 38)
        elif choice == 5:
            print("\nCảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break # Thoát vòng lặp while True, kết thúc chương trình
        else:
            print("Lỗi: Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 5.")

# Điểm kích hoạt chương trình chạy
if __name__ == "__main__":
    main()