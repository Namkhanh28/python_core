import os
from abc import ABC, abstractmethod
class BaseAccount(ABC):
    bank_name = "Vietcombank"
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self._account_holder = " ".join(account_holder.strip().upper().split())
        self.__balance = float(balance)
    @property
    def balance(self):
        return self.__balance
    @property
    def account_holder(self):
        return self._account_holder
    @account_holder.setter
    def account_holder(self, name):
        self._account_holder = " ".join(name.strip().upper().split())
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    def __add__(self, other):
        try:
            return self.balance + other.balance
        except AttributeError:
            return NotImplemented
    def __lt__(self, other):
        try:
            return self.balance < other.balance
        except AttributeError:
            return NotImplemented
    def _increase_amount(self, amount):
        self.__balance += amount
        return self.__balance
    def _decrease_amount(self, amount):
        self.__balance -= amount
        return self.__balance
    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10
    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name
class SavingAccount(BaseAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def deposit(self, amount):
        return self._increase_amount(amount)
    def withdraw(self, amount):
        penalty = amount * 0.02
        total_amount = penalty + amount
        if self.balance >= total_amount:
            self._decrease_amount(total_amount)
            print(f"Rút tiền thành công!")
            print(f"Số tiền rút: {amount:,.0f} VND. Phí phạt (2%): {penalty:,.0f} VND")
            return True
        else:
            print("Số dư không đủ để thanh toán cả gốc lẫn phí phạt!")
            return False
    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate
        self._increase_amount(interest_earned)
        return interest_earned
class CreditAccount(BaseAccount):
    def __init__(self, account_number, account_holder, credit_limit, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.credit_limit = credit_limit
    def deposit(self, amount):
        return self._increase_amount(amount)
    def withdraw(self, amount):
        if not (self.balance - amount >= -self.credit_limit):
            print("Lỗi: Vượt quá hạn mức thấu chi cho phép!")
            return False
        self._decrease_amount(amount)
        print(f"Rút tiền thành công! Số tiền: {amount:,.0f} VND")
        return True
class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5000000:
            return amount * 0.01
        return 0
class HybridAccount(SavingAccount, DigitalPremiumMixin):
    pass
class VNPayGateway:
    def execute_pay(self, account, amount):
        print(f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}...")
        return True
class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        print(f"[Hệ thống Viettel Money]: Đang xác thực giao dịch...")
        return True
def process_payment(payment_gateway, account, amount):
    try:
        if payment_gateway.execute_pay(account, amount):
            account.withdraw(amount)
    except AttributeError:
        print("Lỗi hệ thống: Cổng thanh toán không hợp lệ hoặc chưa được tích hợp phương thức `execute_pay`!")
def main():
    accounts = []
    current_account = None
    while True:
        print("===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nạp / Rút tiền (Đa hình)")
        print("4. Tích lũy / Áp dụng lãi suất định kỳ")
        print("5. Kiểm tra gộp tài khoản & So sánh (Overloading)")
        print("6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        choice = input("Chọn chức năng (1-7): ").strip()
        if choice == "1":
            print("--- CHỌN LOẠI TÀI KHOẢN ---")
            print("1. Savings Account (Tài khoản Tiết kiệm)")
            print("2. Credit Account (Tài khoản Tín dụng)")
            print("3. Hybrid Account (Tài khoản Đa năng)")
            type_choice = input("Chọn loại tài khoản (1-3): ").strip()
            acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
            if not BaseAccount.validate_account_number(acc_num):
                print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
                continue
            name = input("Nhập tên chủ tài khoản: ")
            if type_choice == "1":
                rate = float(input("Nhập lãi suất năm (ví dụ 0.06): "))
                bal = float(input("Nhập số dư ban đầu: "))
                current_account = SavingAccount(acc_num, name, rate, bal)
                accounts.append(current_account)
                print(f"Mở tài khoản Tiết kiệm thành công! Chủ tài khoản: {current_account.account_holder}")
            
            elif type_choice == "2":
                limit = float(input("Nhập hạn mức tín dụng (ví dụ 20000000): "))
                current_account = CreditAccount(acc_num, name, limit, 0)
                accounts.append(current_account)
                print(f"Mở tài khoản Tín dụng thành công! Chủ tài khoản: {current_account.account_holder}")
            
            elif type_choice == "3":
                rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
                bal = float(input("Nhập số dư ban đầu: "))
                current_account = HybridAccount(acc_num, name, rate, bal)
                accounts.append(current_account)
                print(f"Mở tài khoản Đa năng Hybrid thành công! Chủ tài khoản: {current_account.account_holder}")

        elif choice == "2":
            if not current_account:
                print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản trước.")
                continue
            print("\n--- THÔNG TIN TÀI KHOẢN ---")
            print(f"Loại tài khoản: {type(current_account).__name__}")
            print(f"Ngân hàng: {current_account.bank_name}")
            print(f"Số tài khoản: {current_account.account_number}")
            print(f"Chủ tài khoản: {current_account.account_holder}")
            print(f"Số dư: {current_account.balance:,.0f} VND")
            print("\n--- DANH SÁCH MRO ---")
            print(" -> ".join([cls.__name__ for cls in type(current_account).__mro__]))

        elif choice == "3":
            if not current_account:
                print("Chưa chọn tài khoản."); continue
            print("1. Nạp tiền | 2. Rút tiền")
            opt = input("Chọn giao dịch (1-2): ").strip()
            amount = float(input("Nhập số tiền: "))
            
            if opt == "1":
                current_account.deposit(amount)
                if hasattr(current_account, 'cashback_reward'):
                    bonus = current_account.cashback_reward(amount)
                    if bonus > 0:
                        current_account._increase_amount(bonus)
                        print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({bonus:,.0f} VND) vào tài khoản!")
                print(f"Nạp tiền thành công. Số dư hiện tại: {current_account.balance:,.0f} VND")
            elif opt == "2":
                current_account.withdraw(amount)

        elif choice == "4":
            if not current_account:
                print("Chưa chọn tài khoản."); continue
            if hasattr(current_account, 'apply_interest'):
                print(f"Số dư trước tính lãi: {current_account.balance:,.0f} VND")
                earned = current_account.apply_interest()
                print(f"Tiền lãi nhận được: +{earned:,.0f} VND")
                print(f"Số dư mới: {current_account.balance:,.0f} VND")
            else:
                print("Tài khoản này không hỗ trợ tính năng sinh lãi tiết kiệm!")

        elif choice == "5":
            if not current_account:
                print("Chưa chọn tài khoản."); continue
            other_accs = [a for a in accounts if a.account_number != current_account.account_number]
            if not other_accs:
                print("Cần tạo thêm tài khoản đối ứng ở Chức năng 1 để so sánh."); continue
            
            print(f"Tài khoản hiện tại (A): {current_account.account_holder} ({current_account.balance:,.0f} VND)")
            for i, acc in enumerate(other_accs):
                print(f"[{i}] STK: {acc.account_number} | {acc.account_holder} ({acc.balance:,.0f} VND)")
            
            idx = int(input("Chọn tài khoản đối ứng (B): "))
            target = other_accs[idx]
            
            print(f"[Kết quả So sánh (__lt__)]: Khẳng định A nhỏ hơn B là {current_account < target}")
            print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền 2 tài khoản là: {(current_account + target):,.0f} VND")
            
            print("\n[Thử nghiệm Bẫy số 3]: Cộng tài khoản với một chuỗi String...")
            bad_test = current_account + "Một chuỗi ký tự ngẫu nhiên"
            if bad_test == NotImplemented:
                print("-> Hệ thống xử lý bẫy bằng try-except hoàn hảo! Trả về NotImplemented thành công.")

        elif choice == "6":
            if not current_account:
                print("Chưa chọn tài khoản."); continue
            print("1. Cổng VNPay | 2. Cổng ViettelMoney | 3. Cổng Lỗi (Bẫy 4)")
            gate_opt = input("Chọn cổng: ").strip()
            bill = float(input("Nhập số tiền hóa đơn: "))
            
            if gate_opt == "1":
                process_payment(VNPayGateway(), current_account, bill)
            elif gate_opt == "2":
                process_payment(ViettelMoneyGateway(), current_account, bill)
            elif gate_opt == "3":
                class BrokenGateway: pass
                process_payment(BrokenGateway(), current_account, bill)

        elif choice == "7":
            print("Cảm ơn đã trải nghiệm")
            break

if __name__ == "__main__":
    main()