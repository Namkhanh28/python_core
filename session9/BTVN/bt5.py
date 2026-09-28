order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    choice = input('''
===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Gán tài xế cho đơn hàng
3. Cập nhật trạng thái giao hàng
4. Hủy đơn hàng
5. Thoát chương trình

''')
    if choice =='1':
        print('=======Danh sách đơn hàng=======')
        if len(order_list)==0:
            print("HIỆN TẠI CHƯA CÓ ĐƠN HÀNG NÀO")
            break
        for i,product in enumerate(order_list,start=1):
            print(f"{i} ,{product}")
    elif choice =='2':
        
    elif choice =='3':
        pass
    elif choice =='4':
        pass
    elif choice =='5':
        print("Thoát chương trình")
        break
    else :
        print(" Lựa chọn không hợp lệ")
