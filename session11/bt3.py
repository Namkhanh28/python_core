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
                product_list['product_id']=input_id
                product_list['product_name']=input_name
                product_list['price']=price
                product_list['quantity']=input_quantity
                print(f"{i+1}.Mã  : {value['product_id']} | Tên sp: {value['product_name']} | Giá: {value['price']} | Số lượng: {value['quantity']}")

        case '5':
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")