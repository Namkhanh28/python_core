order_note = ""   # lưu ghi chú để dùng cho chức năng 4

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG =====")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại")
    print("4. Tìm kiếm & thay thế ghi chú")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ").strip()
    print()

    match choice:
        case "1":
            sender_name = input("Tên người gửi: ")
            sender_phone = input("SĐT người gửi: ")
            pickup_address = input("Địa chỉ lấy hàng: ")

            receiver_name = input("Tên người nhận: ")
            receiver_phone = input("SĐT người nhận: ")
            delivery_address = input("Địa chỉ giao hàng: ")

            note = input("Ghi chú giao hàng: ")
            order_note = note  

           
            sender_name = sender_name.strip().title()
            receiver_name = receiver_name.strip().title()

            pickup_address = " ".join(pickup_address.split())
            delivery_address = " ".join(delivery_address.split())

            note_clean = note.strip()

            print("\n--- BÁO CÁO ĐƠN HÀNG ---")
            print("Người gửi:", sender_name)
            print("Người nhận:", receiver_name)
            print("Địa chỉ lấy hàng:", pickup_address)
            print("Địa chỉ giao hàng:", delivery_address)
            print("Ghi chú:", note_clean)

            print("Độ dài ghi chú:", len(note_clean))
            print("Số từ:", len(note_clean.split()))
            print("Chữ thường:", note_clean.lower())
            print("Chữ hoa:", note_clean.upper())

        case "2":
            order_code = input("Nhập mã đơn hàng: ")

            original = order_code

            order_code = order_code.strip().upper()
            order_code = "-".join(order_code.split())

            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("Mã ban đầu:", original)
            print("Mã chuẩn hóa:", order_code)

        case "3":
            sender_phone = input("Nhập SĐT người gửi: ").strip()
            receiver_phone = input("Nhập SĐT người nhận: ").strip()

          
            if sender_phone.isdigit() and len(sender_phone) == 10:
                masked_sender = sender_phone[:3] + "*****" + sender_phone[-2:]
            else:
                masked_sender = "Invalid"

            
            if receiver_phone.isdigit() and len(receiver_phone) == 10:
                masked_receiver = receiver_phone[:3] + "*****" + receiver_phone[-2:]
            else:
                masked_receiver = "Invalid"

            print("SĐT người gửi:", masked_sender)
            print("SĐT người nhận:", masked_receiver)

        
        case "4":
            if order_note == "":
                print("Chưa có ghi chú! Hãy nhập đơn hàng trước.")
                continue

            keyword = input("Từ khóa cần tìm: ")
            replace_word = input("Từ thay thế: ")

            if keyword in order_note:
                count = order_note.count(keyword)
                new_note = order_note.replace(keyword, replace_word)

                print("Số lần xuất hiện:", count)
                print("Ghi chú sau thay thế:")
                print(new_note)
            else:
                print("Không tìm thấy từ khóa!")

      
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ!")