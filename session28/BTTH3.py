class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ''

    def calculate_revenue(self):
        self.total_revenue = self.price * self.quantity_sold - self.discount
        if self.total_revenue < 0:
            self.total_revenue = 0

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = 'Thấp'
        elif self.total_revenue < 20000000:
            self.revenue_type = 'Trung bình'
        elif self.total_revenue < 50000000:
            self.revenue_type = 'Khá'
        else:
            self.revenue_type = 'Cao'


class ProductManager:
    def __init__(self):
        self.products = []

    # 1. Thêm sản phẩm
    def add_product(self):
        id = input("Nhập mã sản phẩm: ")
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá sản phẩm: "))
        quantity_sold = int(input("Nhập số lượng bán: "))
        discount = float(input("Nhập giảm giá: "))

        new_product = Product(id, name, price, quantity_sold, discount)
        new_product.calculate_revenue()
        new_product.classify_revenue()

        self.products.append(new_product)
        print("✅ Thêm sản phẩm thành công!")

    # 2. Hiển thị
    def show_all(self):
        if not self.products:
            print("Danh sách đang trống")
            return

        print("\nDanh sách sản phẩm:")
        for p in self.products:
            print(f"{p.id:<7}|{p.name:<15}|{p.price:<10}|{p.quantity_sold:<10}|{p.total_revenue:<15}|{p.revenue_type}")

    # 3. Cập nhật
    def update_product(self):
        update_id = input("Nhập ID cần sửa: ")
        for p in self.products:
            if update_id == p.id:
                p.price = float(input("Giá mới: "))
                p.quantity_sold = int(input("Số lượng mới: "))
                p.discount = float(input("Giảm giá mới: "))

                p.calculate_revenue()
                p.classify_revenue()

                print("✅ Cập nhật thành công!")
                return
        print("❌ Không tìm thấy sản phẩm")

    # 4. Xóa
    def delete_product(self):
        delete_id = input("Nhập ID cần xóa: ")
        for p in self.products:
            if delete_id == p.id:
                choice = input("Bạn có chắc muốn xóa? (Y/N): ")
                if choice.upper() == 'Y':
                    self.products.remove(p)
                    print("✅ Đã xóa sản phẩm")
                else:
                    print("Đã hủy thao tác")
                return
        print("❌ Không tìm thấy sản phẩm")

    # 5. Tìm kiếm
    def search_product(self):
        keyword = input("Nhập tên cần tìm: ")
        found = False

        for p in self.products:
            if keyword.lower() in p.name.lower():
                print(f"{p.id:<7}|{p.name:<15}|{p.price:<10}|{p.quantity_sold:<10}|{p.total_revenue:<15}|{p.revenue_type}")
                found = True

        if not found:
            print("❌ Không tìm thấy sản phẩm")

    # 6. Thống kê
    def statistic(self):
        total = 0
        for p in self.products:
            total += p.total_revenue

        print("💰 Tổng doanh thu:", total)


# ===== MAIN =====
def main():
    manager = ProductManager()

    while True:
        choice = input('''
================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
Nhập lựa chọn: 
''')

        match choice:
            case '1':
                manager.show_all()
            case '2':
                manager.add_product()
            case '3':
                manager.update_product()
            case '4':
                manager.delete_product()
            case '5':
                manager.search_product()
            case '6':
                manager.statistic()
            case '7':
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()