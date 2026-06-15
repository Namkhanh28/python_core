import logging

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

balance = 0

def add_balance():
    global balance

    print("\n--- NẠP TIỀN VÀO VÍ ---")

    while True:
        try:
            amount = int(input("Nhập số tiền cần nạp: "))

            if amount <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(
                    f"InvalidAmountError: Attempted to process {amount} VND."
                )
                continue

            balance += amount
            print(f"Nạp tiền thành công: +{amount:,} VND")
            print(f"Số dư hiện tại: {balance:,} VND")

            logging.info(
                f"Deposit successful: +{amount} VND. Current Balance: {balance}"
            )
            break

        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error(
                "ValueError: Invalid numeric input for deposit."
            )


def transfer_money():
    global balance
    print("\n--- CHUYỂN TIỀN ---")
    while True:
        recipient_phone = input("Nhập số điện thoại người nhận: ")

        if not recipient_phone.isdigit() or len(recipient_phone) != 10:
            print("Lỗi: Số điện thoại phải gồm 10 chữ số.")
            logging.error(
                f"InvalidPhoneNumberError: Attempted to transfer to {recipient_phone}."
            )
            continue

        try:
            amount = int(input("Nhập số tiền cần chuyển: "))

            if amount <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(
                    f"InvalidAmountError: Attempted to process {amount} VND."
                )
                continue

            if amount > balance:
                print("Giao dịch thất bại: Số dư của bạn không đủ.")
                print(f"Số dư hiện tại: {balance:,} VND")
                logging.error(
                    f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {balance} VND."
                )
                continue

            balance -= amount
            print(f"Chuyển tiền thành công tới số điện thoại {recipient_phone}.")
            print(f"Số tiền đã chuyển: {amount:,} VND")
            print(f"Số dư còn lại: {balance:,} VND")

            if amount >= 10000000:
                logging.warning(
                    f"High value transaction detected: {amount} VND to {recipient_phone}"
                )

            logging.info(
                f"Transfer successful: -{amount} VND to {recipient_phone}. Current Balance: {balance}"
            )
            break

        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error(
                "ValueError: Invalid numeric input for transfer."
            )


def read_logs():
    print("\n--- 5 SỰ KIỆN GẦN NHẤT TRONG HỆ THỐNG ---")
    try:
        with open("momo_transactions.log", "r") as log_file:
            lines = log_file.readlines()
            if not lines:
                print("Chưa có lịch sử giao dịch nào trong hệ thống.")
                return
            for line in lines[-5:]:
                print(line.strip())
    except FileNotFoundError:
        print("Chưa có lịch sử giao dịch nào trong hệ thống.")


def check_balance():
    global balance
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,} VND")
    logging.info(
        f"Balance checked. Current Balance: {balance}"
    )

def main():
    while True:
        choice = input('''
========== VÍ MOMO GIẢ LẬP ==========
1. Nạp tiền vào ví
2. Chuyển tiền
3. Xem lịch sử hệ thống
4. Xem số dư tài khoản
5. Thoát chương trình 
===============================================
Chọn chức năng (1-5): ''')
        match choice:
            case "1":
                add_balance()
            case "2":
                transfer_money()
            case "3":
                read_logs()
            case "4":
                check_balance()
            case "5":
                print("Cảm ơn bạn đã sử dụng dịch vụ")
                logging.info(
                    "System shutdown."
                )
                return
            case _:
                print("Lựa chọn không hợp lệ!")

main()