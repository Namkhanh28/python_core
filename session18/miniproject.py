orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]
def display(order_list):
    if len(orders)==0:
        print("Danh sách đơn hàng hiện đang trống")
        return
    else:
        print(f"{'Mã đơn hàng' :<10} | {'Đại lý':<20} | {'Đơn giá':<15}|{'Trạng thái':<10}")
        print("-" * 70)
        for order in order_list:
            print(f"{order['id']:<10}|{order['name']:<25}|{order['price']:>15,} | {order['status']:<10}")
        print("="*70 + "\n")
    
def add_order(order_list):
    print("\n--- THÊM MỚI ĐƠN HÀNG ---")
    order_id = input("Nhập mã ID đơn hàng muốn thêm").strip()
    if not order_id:
        print("Lỗi: Mã đơn hàng không được để trống. Vui lòng nhập lại!")
        continue
    for order in order_list:
        if order_id == orders['id']:
             find = False
            print("Đã có đơn hàng trong danh sách")
        else :
            find = True


           



def menu():
    while True:
        print('''
============= E-COMMERCE MANAGEMENT =============
1. Xem danh sách đơn hàng hiện có
2. Tạo mới đơn hàng đại lý
3.Cập nhật trạng thái đơn hàng
4. Tính tổng doanh thu và chiết khấu 
5, Thoát chương trình             
================================================
              
''')
        choice = input("Chọn chức năng (1-5)")
        match choice:
            case "1":
               display(orders)
            case "2":
                print("Tạo đơn")
            case "3":
                print("update")
            case '4':
                print("tính tổng doanh thu")
            case "5":
                print("Thoát chương trình")
menu()