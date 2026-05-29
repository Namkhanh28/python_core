print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")
# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    total_budget = 0
    print("Đang xử lý nhân viên số", employee_number)
    # Nhập mức lương
    salary = int(input(" Nhập mức lương (VNĐ): "))
    total_budget = total_budget + salary
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")
# Lỗi mắc phải ở trên là khởi tạo biến  total_budget = 0 trong vòng lặp for ,khiến biến này reset lại nhiều lần nên nó sẽ không thể cộng dồn mức lương của cả 3 nhân viên 
# vì vậy phải khởi tạo bên ngoài vòng lặp 

print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")
total_budget = 0
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input(" Nhập mức lương (VNĐ): "))
    total_budget = total_budget + salary
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")