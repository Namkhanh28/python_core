product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True:
    choice=(input('''===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4):  '''))
    match choice:
        case '1':
            if product_list==[]:
                print("Danh sách sản phẩm đang trống")
                continue
            print("Danh sách sản phẩm hiện tại:")
            for i,value in enumerate(product_list):
                print(f"{i+1}.Mã  : {value['product_id']} | Tên sp: {value['product_name']} | Giá: {value['price']} | Số lượng: {value['quantity']}")
        case '2':
            found=False
            input_id=input("Nhập mã sản phẩm: ")
            for i in product_list:
                if i.get('product_id').upper()==input_id.upper():
                    print("MA bi trung")
                    found=True
                    break
            if not found:
                input_name=input("Nhap ten san pham :")
                input_price=int(input("Nhap gia san pham: "))
                input_quantity=int(input("Nhap so luong san pham: "))
                if input_price<0 or input_quantity<0:
                    print("Gia va so luong khong the it hon 0")
                    continue    
                new_product={
                    "product_id": input_id,
                    "product_name":input_name,
                    "price": input_price,
                    "quantity":input_quantity
                }
                product_list.append(new_product)
        case '3':
            input_id = input("Nhập mã sản phẩm cần cập nhật: ")
            found = False
            for i in product_list:
                if i.get('product_id').upper() == input_id.upper():
                    print("Đã tìm thấy sản phẩm, tiến hành cập nhật...")
                    found = True
                    input_name = input("Nhập tên sản phẩm mới: ")
                    input_price = int(input("Nhập giá sản phẩm mới: "))
                    input_quantity = int(input("Nhập số lượng sản phẩm mới: "))
                if input_price < 0 or input_quantity < 0:
                    print("Giá và số lượng không thể nhỏ hơn 0")
                    break
                i['product_name'] = input_name
                i['price'] = input_price
                i['quantity'] = input_quantity
                print(f"Cập nhật thành công: Mã {i['product_id']} | Tên sp: {i['product_name']} | Giá: {i['price']} | Số lượng: {i['quantity']}")
                break
            if not found:
                print("Không tìm thấy sản phẩm với mã đã nhập")
        case '4':
            input_id = input("Nhập giá trị muốn xóa ")
            input_id = input_id.upper().trip()
            check = False
            for i ,product in enumerate(product_list):
                if(product['product_id'] == product_id): 
                    product_list.pop(i)
                    break
            if not check:
                print("không timg thấy sp")
        case '5':
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")