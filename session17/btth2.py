
product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def hien_thi_tem_nhan():
    print("--- DANH SÁCH TEM NHÃN ---")

    for product in product_list:
        parts = product.split("-")
        ma = parts[0]
        ten = parts[1]
        gia = int(parts[2])
        rating = float(parts[3])
        print(f"Mã: {ma:<10} | Tên: {ten:<20} | Giá: {gia:,} VND | Rating: {rating}*")


def sap_xep_san_pham():
    print("--- SẮP XẾP SẢN PHẨM ---")
    def lay_key(product):
        parts = product.split("-")
        gia = int(parts[2])
        rating = float(parts[3])

        return (-rating, gia) 

    product_list.sort(key=lay_key)

    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for i in range(len(product_list)):
        print(f"{i+1}. {product_list[i]}")


def tong_gia_tri_kho():
    print("--- TỔNG GIÁ TRỊ KHO ---")

    tong = 0

    for product in product_list:
        parts = product.split("-")
        gia = int(parts[2])
        tong = tong + gia

    print(f"Tổng giá trị các mặt hàng hiện tại là: {tong:,} VND.")

def menu():
    while True:
        print("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm
2. Sắp xếp sản phẩm thông minh
3. Tính tổng giá trị kho hàng
4. Đóng hệ thống
================================================
""")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            hien_thi_tem_nhan()
        elif choice == "2":
            sap_xep_san_pham()
        elif choice == "3":
            tong_gia_tri_kho()
        elif choice == "4":
            print("Đóng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

menu()