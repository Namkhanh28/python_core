class Employee:
    def __init__(self,id,name,salary_per_day,works_day,bonus):
        self.id =id
        self.name =name
        self.salary_per_day = salary_per_day 
        self.works_day =works_day
        self.bonus=bonus
        self.total_salary = 0
        self.salary_type =''
        
    def calculate_salary(self):
        self.total_salary = self.salary_per_day*self.works_day + self.bonus
        if self.total_salary < 0 : self.total_salary = 0

    def classify_salary(self):
        if self.total_salary < 2000000 :
            self.salary_type ="Thấp"
        elif self.total_salary < 5000000:
            self.salary_type ="Trung bình"
        elif self.total_salary < 10000000:
            self.salary_type ="KHá"
        else :
            self.salary_type ="Cao"
        
class EmployeeManager:
    def __init__(self):
        self.employee_list=[]
    
    def find_employee_by_id(self,id):
        for employee in self.employee_list:
            if id == employee.id:
                return employee
        return None
    
    def add_employee(self):
        print("\n===== THÊM NHÂN VIÊN =====")
        id = input("Nhập ID mới:")
        if not id :
            print("Vui lòng nhập đủ thông tin")
        name =input("Nhập tên nhân viên")
        if not name:
            print("Vui lòng nhập đủ thông tin")
        salary_per_day = float(input("Nhập lương theo ngày "))
        if not salary_per_day :
            print("Vui lòng nhập đủ thông tin")
        works_day = int(input("Nhập số ngày làm "))
        if not works_day :
            print("Vui lòng nhập đủ thông tin")
        bonus = float(input("Nhập lương thưởng "))
        if not bonus :
            print("Vui lòng nhập đủ thông tin")
        new_employee = Employee(id,name,salary_per_day,works_day,bonus)
        new_employee.calculate_salary()
        new_employee.classify_salary()
        self.employee_list.append(new_employee)
        print("✅ Thêm sản phẩm thành công!")

    def show_all(self):
        if not self.employee_list:
            print("HIỆN TẠI KHÔNG CÓ NHÂN VIÊN")
            return
        print("====DANH SÁCH SẢN PHẨM===")
        for e in self.employee_list:
            print(f"{e.id:<7}|{e.name:<15}|{e.salary_per_day:<15}|{e.works_day:<15}|{e.total_salary:<15}|{e.salary_type}")
    def update_employee(self):
        id = input("Nhập ID nhân viên muốn sửa")
        emp = self.find_employee_by_id(id)
        if not emp:
            print("Không tìm thấy nhân viên")
            return
        emp.name =input("Nhập tên mới (nếu muốn )")
        emp.salary_per_day = float(input("Nhập lương theo ngày muốn đổi"))
        emp.works_day = int(input("Ngày làm mới: "))
        emp.bonus = float(input("Thưởng mới: "))

        emp.calculate_salary()
        emp.classify_salary()
        print("Cập nhật thông tin thầnh công ")
    def delete_employee(self):
        id = input("Nhập id người muốn xóa ")
        find_emp = self.find_employee_by_id(id)
        if not find_emp :
            print("Không timg thầy nhân viên")
        else :
            self.employee_list.remove(find_emp)
            print('Đã xóa thành công ')
    def search_employee(self):
        search = input("Nhập mã nhân viên muốn tìm: ")
        found = False

        for employee in self.employee_list:
            if search == employee.id:
                print(f"{employee.id:<7}|{employee.name:<15}|{employee.salary_per_day:<15}|{employee.works_day:<15}|{employee.total_salary:<15}|{employee.salary_type}")
                found = True
                break

        if not found:
            print("❌ Không tìm thấy nhân viên")
    def statistics(self):
        if not self.employee_list:
            print("Danh sách trống")
            return

        total = sum(e.total_salary for e in self.employee_list)
        max_salary = max(self.employee_list, key=lambda e: e.total_salary)
        min_salary = min(self.employee_list, key=lambda e: e.total_salary)

        print("\n===== THỐNG KÊ =====")
        print(f"Tổng lương: {total}")
        print(f"Cao nhất: {max_salary.name} - {max_salary.total_salary}")
        print(f"Thấp nhất: {min_salary.name} - {min_salary.total_salary}")


def main():
    manager = EmployeeManager()
    while True :
        choice = input('''
================ MENU ================

1. Hiển thị danh sách nhân viên

2. Thêm nhân viên mới

3. Cập nhật nhân viên

4. Xóa nhân viên

5. Tìm kiếm nhân viên

6. Thống kê lương

7. Thoát

======================================

Nhập lựa chọn của bạn:

''')
        match choice:
            case '1':
                manager.show_all()
            case '2':
                manager.add_employee()
            case '3':
                manager.update_employee()
            case '4':
                manager.delete_employee()
            case '5':
                manager.search_employee()
            case '6':
                manager.statistics()
            case '7':
                print("Thoát chương trình")
                break
            case _:
                print("LỰA CHỌN KHÔNG HỢP LỆ")
if __name__ == '__main__' :
    main()