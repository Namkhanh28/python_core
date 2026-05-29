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
    choice =  input( '''
==================================================
         HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY
==================================================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
==================================================
Mời bạn chọn chức năng (1-5): ''')
    match choice :
        case '1':
            print('Danh sách sản phẩm hiện tại')
            for i,value in enumerate(product_list):
                print(f'{i+1}.Mã sản phẩm :{value['product_id']} | tên sản phẩm :')
        case '2':
        case '5':
            print('Thoát chương trình ')