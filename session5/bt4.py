so_chi_nhanh = int(input("Nhập số lượng chi nhánh: "))

for chi_nhanh in range(1, so_chi_nhanh + 1):
    print(f"\nChi nhánh {chi_nhanh}:")
    
    for lop in range(1, 3):
        
        while True:
            so_hoc_vien = int(input(f"Nhập số học viên đi học của lớp {lop}: "))
            
            if so_hoc_vien < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break 

        if so_hoc_vien == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue 
        if so_hoc_vien >= 20:
            print(f"Chi nhánh {chi_nhanh} - Lớp {lop}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {chi_nhanh} - Lớp {lop}: Lớp cần được nhắc nhở theo dõi")

print("--- ĐÃ HOÀN THÀNH KIỂM TRA SĨ SỐ ---")