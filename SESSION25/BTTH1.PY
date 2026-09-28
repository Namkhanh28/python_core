class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self._account_name = None
        self.account_name = account_name  # gọi setter
        self.__balance = 0  # private

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, new_name):
        cleaned = new_name.strip()
        if cleaned == "":
            print("Tên tài khoản không được để trống")
        else:
            self._account_name = cleaned.upper()

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return

        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return

        self.__balance -= total
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")

    def display_info(self):
        print("Ngân hàng:", BankAccount.bank_name)
        print("Số tài khoản:", self.account_number)
        print("Tên chủ tài khoản:", self.account_name)
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")

current_account = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- MỞ TÀI KHOẢN MỚI ---")
        while True:
            acc_num = input("Nhập số tài khoản 10 chữ số: ")
            if BankAccount.validate_account_number(acc_num):
                break
            else:
                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

        name = input("Nhập tên chủ tài khoản: ")
        current_account = BankAccount(acc_num, name)

        print("Mở tài khoản thành công!")
        print("Số tài khoản:", acc_num)
        print("Tên chủ tài khoản:", current_account.account_name)

    elif choice == "2":
        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        else:
            print("\n--- THÔNG TIN TÀI KHOẢN ---")
            current_account.display_info()

    elif choice == "3":
        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            continue

        print("\n--- GIAO DỊCH ---")
        print("1. Nạp tiền")
        print("2. Rút tiền")

        t = input("Chọn (1-2): ")

        try:
            amount = float(input("Nhập số tiền: "))
        except:
            print("Dữ liệu không hợp lệ")
            continue

        if t == "1":
            current_account.deposit(amount)
            print(f"Số dư mới: {current_account.balance:,} VND")
        elif t == "2":
            current_account.withdraw(amount)
            print(f"Số dư mới: {current_account.balance:,} VND")

    elif choice == "4":
        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            continue

        new_name = input("Nhập tên mới: ")
        current_account.account_name = new_name
        print("Tên hiện tại:", current_account.account_name)

    elif choice == "5":
        print("\n--- ĐỔI PHÍ GIAO DỊCH ---")
        print(f"Phí hiện tại: {BankAccount.transaction_fee:,} VND")

        try:
            new_fee = int(input("Nhập phí mới: "))
            if new_fee < 0:
                print("Phí giao dịch không được âm")
            else:
                BankAccount.update_transaction_fee(new_fee)
                print(f"Đã cập nhật phí: {new_fee:,} VND")
        except:
            print("Dữ liệu không hợp lệ")
    
    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng!")
        break

    else:
        print("Lựa chọn không hợp lệ")