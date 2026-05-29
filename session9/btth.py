branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] 
target_achieved = [True, True, False, True, False] 

while True:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): ''')

    if choice.isdigit():
        choice = int(choice)
    else:
        print("Hãy nhập 1 số dương 1-4")
        continue
    
    match choice:
        case 1:
            print("--- BÁO CÁO DOANH THU TỔNG HỢP ---")
            print(f"{"Tên cơ sở":<30}| {"Doanh thu":<15}| {"Trạng thái":<10}")
            print("-" * 65)
            for i in range(len(branch_names)):
                print(f"{branch_names[i]:<30}| {daily_revenues[i]:<15}| {"Đạt" if target_achieved[i] else "Không đạt":<10}")
            print("-" * 65)
            print(f"=> TỔNG DOANH THU TOÀN VÙNG: {sum(daily_revenues)} VNĐ")
            
        case 2:
            max_revenue = max(daily_revenues)
            min_revenue = min(daily_revenues)
            index_max = daily_revenues.index(max_revenue)
            index_min = daily_revenues.index(min_revenue)
            max_branch = branch_names[index_max]
            min_branch = branch_names[index_min]
            
            print(f"Cơ sở có doanh thu CAO NHẤT: {max_branch} ({max_revenue} VNĐ) ")
            print(f"Cơ sở có doanh thu THẤP NHẤT: {min_branch} ({min_revenue} VNĐ) ")
        
        case  3:
            failed_branches = []
            for i, fail in enumerate(target_achieved):
                if fail  == False:
                    failed_branches.append(branch_names[i])
                    
            print("--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC ---")
            print(failed_branches)
            
        case 4:
            print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
            break
            
        case _:
            print("Lựa chọn không hợp lệ")