
patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

CURRENT_YEAR = 2026
def find_patient_index(records, patient_id):

    search_id = patient_id.strip().upper()
    
    for i in range(len(records)):

        if records[i].startswith(search_id + "-"):
            return i
    return -1

def display_records(records):

    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        print("--------------------------------------------------------------------------")
        return
    for i in range(len(records)):
        parts = records[i].split("-")
        p_id = parts[0]
        p_name = parts[1]
        p_year = parts[2]
        p_diag = parts[3]
        
        print(f"{i + 1}. [{p_id}] {p_name:<18} | Năm sinh: {p_year} | Chẩn đoán: {p_diag}")
    print("--------------------------------------------------------------------------")

def add_patient(records):

    p_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if len(p_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return
        
    if find_patient_index(records, p_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    name_input = input("Nhập tên bệnh nhân: ").strip()
    if len(name_input) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    p_name = name_input.replace("-", " ").title()

    p_year_str = input("Nhập năm sinh: ").strip()
    while True:
        if p_year_str.isdigit():
            p_year_int = int(p_year_str)
            if 1900 <= p_year_int <= CURRENT_YEAR:
                break 
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        p_year_str = input("Nhập năm sinh: ").strip()

    diag_input = input("Nhập chẩn đoán: ").strip()
    if len(diag_input) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return
    p_diag = diag_input.replace("-", " ").capitalize()

    new_record = "-".join([p_id, p_name, str(p_year_int), p_diag])
    records.append(new_record)
    print("\nThêm hồ sơ bệnh nhân thành công!")

def update_diagnosis(records):

    p_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    
    if len(p_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return
        
    index = find_patient_index(records, p_id)
    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {p_id.upper()}!")
        return

    parts = records[index].split("-")
    print(f"\nTìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    
    new_diag_input = input("Nhập chẩn đoán mới: ").strip()
    if len(new_diag_input) == 0:
        print("Chẩn đoán mới không được để trống!")
        return

    clean_diag = new_diag_input.replace("-", " ").capitalize()

    parts[3] = clean_diag

    records[index] = "-".join(parts)
    print("Cập nhật chẩn đoán thành công!")

def generate_age_report(records):

    count_children = 0    
    count_adults = 0     
    count_elderly = 0      
    for r in records:
        parts = r.split("-")
        birth_year = int(parts[2])
        age = CURRENT_YEAR - birth_year
        
        if age < 16:
            count_children += 1
        elif age <= 60:
            count_adults += 1
        else:
            count_elderly += 1
            
    print(f"Trẻ em: {count_children} bệnh nhân")
    print(f"Trưởng thành: {count_adults} bệnh nhân")
    print(f"Người cao tuổi: {count_elderly} bệnh nhân")
    print("--------------------------------------")


while True:
    print("===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")
    
    choice = input("Chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            display_records(patient_records)
        case "2":
            add_patient(patient_records)
        case "3":
            update_diagnosis(patient_records)
        case "4":
            generate_age_report(patient_records)
        case "5":
            print("Thoat chuong trinh")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")