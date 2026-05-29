qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:
    print("\n======= QUẢN LÝ SẢN PHẨM =======")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    try:
        choose = int(input("Nhập lựa chọn: "))
    except:
        print("Vui lòng nhập số!")
        continue

    if choose <= 0:
        print("Vui lòng nhập lại!")
        continue

    match choose:

        case 1:
            print(f"Laptop: {qty_laptop}")
            print(f"Phone: {qty_phone}")
            print(f"Tablet: {qty_tablet}")

        case 2:
            product = int(input("Chọn (1-Laptop, 2-Phone, 3-Tablet): "))

            while True:
                amount = int(input("Nhập số lượng: "))
                if amount < 0:
                    print("Không hợp lệ!")
                    continue
                break

            if product == 1:
                qty_laptop += amount
            elif product == 2:
                qty_phone += amount
            elif product == 3:
                qty_tablet += amount

        case 3:
            product = int(input("Chọn (1-Laptop, 2-Phone, 3-Tablet): "))

            while True:
                amount = int(input("Nhập số lượng: "))
                if amount < 0:
                    print("Không hợp lệ!")
                    continue
                break

            if product == 1:
                if amount > qty_laptop:
                    print("Không đủ hàng")
                else:
                    qty_laptop -= amount

            elif product == 2:
                if amount > qty_phone:
                    print("Không đủ hàng")
                else:
                    qty_phone -= amount

            elif product == 3:
                if amount > qty_tablet:
                    print("Không đủ hàng")
                else:
                    qty_tablet -= amount

        case 4:
            if qty_laptop < 10:
                print("Laptop sắp hết")
            if qty_phone < 10:
                print("Phone sắp hết")
            if qty_tablet < 10:
                print("Tablet sắp hết")

        case 5:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ!")