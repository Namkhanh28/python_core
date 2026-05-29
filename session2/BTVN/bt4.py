print("=== HỆ THỐNG ĐÁNH GIÁ PHẪU THUẬT ===")

age_input = input("Nhập tuổi: ")
bp_input = input("Nhập huyết áp tâm thu (mmHg): ")
sugar_input = input("Nhập đường huyết (mg/dL): ")

age = int(age_input)
systolic_bp = int(bp_input)
blood_sugar = int(sugar_input)

if not (age_input.isdigit() and bp_input.isdigit() and sugar_input.isdigit()):
    print("Dữ liệu nhập vào không hợp lệ (phải là số nguyên)!")
    exit()
if age < 0 or systolic_bp < 0 or blood_sugar < 0:
    print(" Dữ liệu nhập vào không hợp lệ (không được là số âm)!")
    exit()
if age < 75:
    if 90 <= systolic_bp <= 140:
        if blood_sugar < 150:
            print(" ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print(" TỪ CHỐI PHẪU THUẬT: Đường huyết ≥ 150 mg/dL")
    else:
        print(" TỪ CHỐI PHẪU THUẬT: Huyết áp không trong khoảng 90-140 mmHg")
else:
    print(" TỪ CHỐI PHẪU THUẬT: Tuổi ≥ 75")