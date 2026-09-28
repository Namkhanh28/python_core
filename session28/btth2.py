class Employee:
    def __init__(self, id, name, salary_day, work_days, allowance):
        self.id = id
        self.name = name
        self.salary_day = salary_day
        self.work_days = work_days
        self.allowance = allowance
        self.total_income = 0
        self.income_type = ""
        self.calculate_income()
        self.classify_income()

    def calculate_income(self):
        self.total_income = (self.salary_day * self.work_days) + self.allowance
        return self.total_income

    def classify_income(self):
        if self.total_income < 9000000:
            self.income_type = "Thấp"
        elif 9000000 <= self.total_income < 15000000:
            self.income_type = "Trung bình"
        elif 15000000 <= self.total_income < 30000000:
            self.income_type = "Khá"
        elif self.total_income >= 30000000:
            self.income_type = "Cao"

    def fixed_income(self, salary_day: int, work_days: int, allowance: int):
        self.salary_day = salary_day
        self.work_days = work_days
        self.allowance = allowance
        self.calculate_income()
        self.classify_income()
class EmployeeManager:
    def __init__(self):
        self.employees = []
    def add_employee(self):
        while True:
            found = False 
            input_id = input("Nhập ID nhân viên mới: ").strip().upper()
            if input_id == "":
                print("ID không được để trống!")
                continue
            for employ in self.employees:
                if input_id == employ.id.upper():
                    found = True
                    break
            if found:
                print("Nhân viên đã tồn tại (Trùng ID)!")
                continue
            break
        while True:
            input_name = input("Nhập tên nhân viên mới: ").strip().title()
            if input_name == "":
                print("Tên nhân viên không được để trống!")
                continue
            break
        while True:
            try:
                input_salary_day = int(input("Nhập lương mỗi ngày: "))
                if input_salary_day < 0:
                    print("Lương ngày không thể ít hơn 0!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        while True:
            try:
                input_allowance = int(input("Nhập phụ cấp: "))
                if input_allowance < 0:
                    print("Phụ cấp không thể ít hơn 0!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        while True:
            try:
                input_work_days = int(input("Nhập ngày công (0-31): "))
                if not (0 <= input_work_days <= 31):
                    print("Ngày công phải nằm trong khoảng từ 0 đến 31 ngày!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
        new_employ = Employee(input_id, input_name, input_salary_day, input_work_days, input_allowance)
        self.employees.append(new_employ)
        print(f" Đã thêm thành công nhân viên {input_name}!")

    def show_all(self):
        if not self.employees:
            print("Danh sách nhân viên đang trống!")
            return
        print(f"{'Mã NV':<10} | {'Họ tên':<20} | {'Lương ngày':<12} | {'Ngày công':<10} | {'Phụ cấp':<10} | {'Tổng thu nhập':<13} | {'Loại TN':<10}")
        for employ in self.employees:
            print(f"{employ.id:<10} | {employ.name:<20} | {employ.salary_day:<12,} | {employ.work_days:<10} | {employ.allowance:<10,} | {employ.total_income:<13,} | {employ.income_type:<10}")
    def update_employee(self):
        if not self.employees:
            print("Danh sách trống, không thể cập nhật!")
            return
        input_id = input("Nhập mã nhân viên cần cập nhật: ").strip().upper()
        target_employee = None
        
        for employ in self.employees:
            if employ.id.upper() == input_id:
                target_employee = employ
                break
                
        if target_employee is None:
            print(f"Lỗi: Không tìm thấy nhân viên có mã {input_id}!")
            return
        print(f"Đang cập nhật thông tin cho nhân viên: {target_employee.name}")
        while True:
            try:
                new_salary = int(input("Nhập lương ngày mới: "))
                if new_salary < 0:
                    print("Lương ngày không thể nhỏ hơn 0!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên!")
        while True:
            try:
                new_work_days = int(input("Nhập số ngày công mới (0-31): "))
                if not (0 <= new_work_days <= 31):
                    print("Ngày công phải từ 0 đến 31!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên!")
                
        while True:
            try:
                new_allowance = int(input("Nhập phụ cấp mới: "))
                if new_allowance < 0:
                    print("Phụ cấp không thể nhỏ hơn 0!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên!")
        target_employee.fixed_income(new_salary, new_work_days, new_allowance)
        print(f" Cập nhật thành công cho nhân viên {target_employee.name}!")
    def delete_employee(self):
        if not self.employees:
            print("Danh sách trống, không có gì để xóa!")
            return
        input_id = input("Nhập mã nhân viên cần xóa: ").strip().upper()
        target_employee = None
        for employ in self.employees:
            if employ.id.upper() == input_id:
                target_employee = employ
                break 
        if target_employee is None:
            print(f"Lỗi: Không tìm thấy nhân viên có mã {input_id}!")
            return
        confirm = input(f"Bạn có chắc chắn muốn xóa nhân viên {target_employee.name} không? (Y/N): ").strip().upper()
        if confirm == 'Y':
            self.employees.remove(target_employee)
            print(" Xóa nhân viên thành công!")
        else:
            print(" Đã hủy thao tác xóa.")
    def search_employee(self):
        if not self.employees:
            print("Danh sách trống, không thể tìm kiếm!")
            return
        search_name = input("Nhập tên nhân viên cần tìm (tìm kiếm gần đúng): ").strip().lower()
        if search_name == "":
            print("Từ khóa tìm kiếm không được để trống!")
            return
            
        results = []
        for employ in self.employees:
            if search_name in employ.name.lower():
                results.append(employ)
        if not results:
            print(f"Không tìm thấy nhân viên phù hợp với từ khóa '{search_name}'.")
            return
            
        print(f"\n Kết quả tìm kiếm ({len(results)} nhân viên):")
        print(f"{'Mã NV':<10} | {'Họ tên':<20} | {'Lương ngày':<12} | {'Ngày công':<10} | {'Phụ cấp':<10} | {'Tổng thu nhập':<13} | {'Loại TN':<10}")
        for employ in results:
            print(f"{employ.id:<10} | {employ.name:<20} | {employ.salary_day:<12,} | {employ.work_days:<10} | {employ.allowance:<10,} | {employ.total_income:<13,} | {employ.income_type:<10}")
employ_manage = EmployeeManager()

while True:
    choice = input('''
================ MENU ================
1. Hiển thị danh sách nhân viên
2. Thêm nhân viên mới
3. Cập nhật nhân viên
4. Xóa nhân viên
5. Tìm kiếm nhân viên
6. Thoát
=====================================
Nhập lựa chọn của bạn: ''').strip()
    match choice:
        case "1":
            employ_manage.show_all()
        case "2":
            employ_manage.add_employee()
        case "3":
            employ_manage.update_employee()
        case "4":
            employ_manage.delete_employee()
        case "5":
            employ_manage.search_employee()
        case "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý nhân sự")
            break
        case _:
            print(" Vui lòng nhập từ 1 đến 6")