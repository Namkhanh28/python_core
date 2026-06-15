# # Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
# patient_diagnoses = ["Sốt Xuất Huyết"]
# def add_diagnosis(raw_diagnosis, current_list):
#     # chuẩn hóa tên bệnh
#     raw_diagnosis.strip()
#     raw_diagnosis.title()
#     # Thêm chẩn đoán vào danh sách bệnh án
#     current_list.extend(raw_diagnosis)
#     return current_list
# new_diagnosis = "  viEm phE QUan  "
# updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
# print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)

# raw_diagnosis.strip(),raw_diagnosis.title() đang sử dụng sai cách, chuỗi của Python vốn bất biến nên khi muốn thay đổi cần phải có 1 biến để chứa chuỗi mới sau thay đổi 

patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list
new_diagnosis = "  viEm phE QUan  "
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)
