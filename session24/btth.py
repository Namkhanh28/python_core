class Drink:
    def __init__(self, input_id, input_name, price):
        self.input_id = input_id
        self.input_name = input_name
        self.__price = price      
        self.is_available = True    
    @property
    def price(self):
        return self.__price
    def toggle_available(self):
        self.is_available = not self.is_available
menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]
def show_menu_list():
    print(f"{'Mã món':<8} | {'Tên món':<18} | {'Giá bán':<8} | {'Trạng thái'}")
    for drink in menu:
        status = "Đang bán" if drink.is_available else "Ngừng bán"
        print(f"{drink.input_id:<8} | {drink.input_name:<18} | {drink.price:<8} | {status}")
def add_new_drink():
    input_id = input("Nhập mã món: ").strip().upper()
    for drink in menu:
        if drink.input_id == input_id:
            print("Mã món đã tồn tại trong hệ thống")
            return
    input_name = input("Nhập tên món: ").strip()
    try:
        price = int(input("Nhập giá bán: "))
        if price <= 0:
            print("Giá bán không hợp lệ")
            return
    except ValueError:
        print("Giá bán không hợp lệ!")
        return
    new_drink = Drink(input_id, input_name, price)
    menu.append(new_drink)
    print(f"Thành công: Đã thêm món {input_name} vào thực đơn!")
def update_status():
    input_id = input("Nhập mã món cần cập nhật: ").strip().upper()
    for drink in menu:
        if drink.input_id == input_id:
            drink.toggle_available()
            status_text = "Đang bán" if drink.is_available else "Ngừng bán"
            print(f"Đã cập nhật trạng thái món {drink.input_id}.")
            print(f"Trạng thái hiện tại: {status_text}")
            return
    print("Không tìm thấy món có mã này")
while True:
    print("=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("==============================================")
    choice = input("Chọn chức năng (1-4): ").strip()
    match choice:
        case "1":
            show_menu_list()
        case "2":
            add_new_drink()
        case "3":
            update_status()
        case "4":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 4.")