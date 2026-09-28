from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,employee_id, name ,salary_day,work_days,allowance,total_income, income_type):
        self.id= employee_id
        self.name= name
        self.salary_day= salary_day
        self.work_days= work_days
        self.allowance= allowance
        self.total_income= total_income
        self.income_type= income_type
    def display_info(self):
        print(f"{self.id} | {self.name} |{self.salary_day} | {self.work_days} |{self.allowance}|{self.total_income}|{self.income_type}", end=" | ")
    @abstractmethod
    def calculate_income(self):
        self.total_income = (self.salary_day + self.work_days)*self.allowance
        return self.total_income 
    def classify_income(self):
            if self.total_income < 9000000:
                self.income_type = "Thấp"
            elif self.total_income < 15000000:
                self.income_type = "Trung bình"
            elif self.total_income < 30000000:
                self.income_type = "Khá"
            else:
                self.income_type = "Cao"

class EmployeeManager(Employee):
    def __init__(self, employee_id, name, salary_day, work_days, allowance, total_income, income_type):
        super().__init__(employee_id, name, salary_day, work_days, allowance, total_income, income_type)



def main():
    employees =[
        
    ]
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
Nhập lựa chọn của bạn(1-6)
                       
''')
        match choice:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                print("Thoát chương trình!")
                break
            case _ :
                print("Vui lòng nhập đúng yêu cầu")
if __name__ == "___main___":
    main()