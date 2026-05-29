while True:
    employee_count = int(input("Nhập số lượng nhân viên "))
    if employee_count <= 0:
        break
    print("Hãy nhập lại thông tin")

for i in range(1, employee_count + 1):
    print()
    
    employee_name = input("Nhập tên nhân viên: ")
    working_days = int(input("Nhập số ngày làm việc: "))

    if working_days < 0 or working_days > 22:
        print("Dữ liệu không hợp lệ")
        continue 
        
    if working_days == 0:
        print("Nhân viên này nghỉ cả tháng")
        continue
        
    print(f"{employee_name}: ", end="")
    
    for j in range(working_days):
        print("*", end="")
    print()
    if working_days >= 18:
        print("Nhân viên làm nhiều ngày")
    elif working_days < 10:
        print("Nhân viên làm ít ngày")
    else:
        print("Nhân viên làm việc bình thường")