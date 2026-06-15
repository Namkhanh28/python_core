patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def validate_gender(gender_input):  
    cleaned_gender = gender_input.strip().lower()
    if cleaned_gender == "nam" or cleaned_gender == "nu":
        return True
    return False

def find_patient_index(patient_list, patient_id):

    search_id = patient_id.strip().upper()
    for i in range(len(patient_list)):
        if patient_list[i][0] == search_id:
            return i
    return -1

def display_patients(patient_list):

    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
        
    for i in range(len(patient_list)):
        p = patient_list[i]
        print(f"{i + 1}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")

def add_patient(patient_list):

    patient_id = input("Nhập mã bệnh nhân: ")
    if len(patient_id.strip()) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    if len(name.strip()) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    gender = input("Nhập giới tính Nam/Nu: ")
    while not validate_gender(gender):
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
        gender = input("Nhập giới tính Nam/Nu: ")

    diagnosis = input("Nhập chẩn đoán bệnh: ")
    if len(diagnosis.strip()) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    final_id = patient_id.strip().upper()
    final_name = name.strip().title()
    final_gender = gender.strip().capitalize()
    final_diagnosis = diagnosis.strip().capitalize()

    new_p = [final_id, final_name, final_gender, final_diagnosis]
    patient_list.append(new_p)
    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):

    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ")
    
    if len(patient_id.strip()) == 0:
        print("Mã bệnh nhân không được để trống!")
        return
        
    index = find_patient_index(patient_list, patient_id)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id.strip().upper()}!")
        return

    p = patient_list[index]
    print(f"Tìm thấy bệnh nhân: {p[1]}")
    print(f"Chẩn đoán hiện tại: {p[3]}")
    
    new_diag = input("Nhập chẩn đoán mới: ")
    if len(new_diag.strip()) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    p[3] = new_diag.strip().capitalize()
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ")
    
    if len(keyword.strip()) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return
        
    clean_keyword = keyword.strip().lower()
    count = 0
    print("Kết quả tìm kiếm:")
    
    for p in patient_list:
        if clean_keyword in p[3].lower():
            count += 1
            print(f"{count}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")
            
    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
        
    print(f"Có tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")
def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1":
                display_patients(patients)
            case "2":
                add_patient(patients)
            case "3":
                update_diagnosis(patients)
            case "4":
                search_by_disease(patients)
            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
main()