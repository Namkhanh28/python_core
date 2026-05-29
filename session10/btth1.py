cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
while True:
    choice =  input( '''
==================================================
          SHOPEE CART MANAGEMENT SYSTEM
==================================================
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
==================================================
Mời bạn chọn chức năng (1-5): ''')
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    
    match choice:
        case 1:
            total_money = 0
            quantity_product = 0
            print("-- CHI TIẾT GIỎ HÀNG --")
            print(f"{"STT":<5}| {"Mã sp":<6}| {"Tên sản phẩm":<25}| {"SL":<4}| {"Đơn giá":<15}| {"Thành tiền":<15}")
            print("-"*75)
            for index, item in enumerate(cart_items, start=1):
                print(f"{index:<5}| {item[0]:<6}| {item[1]:<25}| {item[2]:<4}| {f"{item[3]:,}đ":<15}| {f"{item[3] * item[2]:,}đ" :<15} ")
                total_money += item[3] * item[2]
                quantity_product += item[2]
            print("-"*75)
            
            print(f"Tổng số lượng sản phẩm trong giỏ: {quantity_product}")
            print(f"TỔNG TIỀN CẦN THANH TOÁN {total_money:,}đ")
            
        case 2:
            id_input = input("Nhập vào mã sản phẩm bạn cần: ").strip().upper()
            is_found = False
            for index, value in enumerate(cart_items):
                if value[0] == id_input:
                    value[2] += int(input("Bạn muốn thêm bao nhiêu sản phẩm vào giỏ hàng: "))
                    is_found = True
                    break
                
            if is_found == False:
                new_cart = []
                name_product = input("Tên sản phẩm: ")
                quantity_input = int(input("Số lượng: "))
                if quantity_input <= 0:
                    print("Không thể nhập <= 0")
                    continue
                price_input = int(input("Đơn giá: "))
                if price_input <= 0:
                    print("Không thể nhập <= 0")
                    continue
                new_cart  = [id_input, name_product, quantity_input, price_input]
                cart_items.append(new_cart)
                
        case 3:
            id_input = input("Nhập vào mã sản phẩm bạn cần cập nhật: ").strip().upper()
            is_found = False
            for index, value in enumerate(cart_items):
                if value[0] == id_input:
                    is_found = True
                    value[2] = int(input("Bạn muốn cập nhật bao nhiêu sản phẩm vào giỏ hàng: "))
                    break
            if not is_found:
                print("Mã sản phẩm không tồn tại")
                continue
                
        case 4:
            id_input = input("Nhập vào mã sản phẩm bạn cần xóa: ").strip().upper()
            is_found = False
            for index, value in enumerate(cart_items):
                if value[0] == id_input:
                    is_found = True
                    cart_items.pop(index)
                    print(f"Đã xóa sp có mã {id_input}")
                    break
            if not is_found:
                print("Mã sản phẩm không tồn tại")
                continue
            
        case 5:
            print("Cảm ơn vì đã sử dụng!!!")
            break
        
        case _:
            print("Lỗi cú pháp!!!!")
            