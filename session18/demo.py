# =========================
# DANH SACH SINH VIEN
# =========================

students = [
     {
        "id": "SV001",
        "name": "Nguyen Van An",
        "math_score": 9.0,
        "physics_score": 8.5,
        "chemistry_score": 9.5
    },
    {
        "id": "SV002",
        "name": "Tran Thi Binh",
        "math_score": 7.5,
        "physics_score": 7.2,
        "chemistry_score": 7.8
    },
    {
        "id": "SV003",
        "name": "Le Van Cuong",
        "math_score": 4.5,
        "physics_score": 5.0,
        "chemistry_score": 4.8
    }
]


# =========================
# HAM TINH DIEM TRUNG BINH
# =========================

def calculate_average(math, physics, chemistry):
    return round((math + physics + chemistry) / 3, 2)


# =========================
# HAM XEP LOAI
# =========================

def classify_student(avg):
    if avg < 5:
        return "Yeu"
    elif avg < 7:
        return "Trung binh"
    elif avg < 8:
        return "Kha"
    else:
        return "Gioi"


# =========================
# NHAP DIEM HOP LE
# =========================

# def input_score(subject):
#     while True:
#         try:
#             score = float(input(f"Nhap diem {subject}: "))

#             if 0 <= score <= 10:
#                 return score

#             print("Diem phai nam trong khoang 0 - 10")

#         except:
#             print("Vui long nhap so hop le")


# =========================
# HIEN THI DANH SACH
# =========================

def display_students():

    if len(students) == 0:
        print("\nDanh sach rong")
        return

    print("\n{:<10}{:<25}{:<10}{:<10}{:<10}{:<10}{:<15}".format(
        "Ma SV",
        "Ho Ten",
        "Toan",
        "Ly",
        "Hoa",
        "DTB",
        "Xep Loai"
    ))

    print("-" * 90)

    for student in students:
        print("{:<10}{:<25}{:<10}{:<10}{:<10}{:<10}{:<15}".format(
            student["id"],
            student["name"],
            student["math"],
            student["physics"],
            student["chemistry"],
            student["average"],
            student["rank"]
        ))


# =========================
# KIEM TRA TRUNG MA
# =========================

def is_duplicate_id(student_id):

    for student in students:
        if student["id"] == student_id:
            return True

    return False


# =========================
# THEM SINH VIEN
# =========================

def add_student():

    while True:
        student_id = input("Nhap ma sinh vien: ").strip()

        if student_id == "":
            print("Ma sinh vien khong duoc rong")
            continue

        if is_duplicate_id(student_id):
            print("Ma sinh vien da ton tai")
            continue

        break

    while True:
        name = input("Nhap ho ten: ").strip()

        if name == "":
            print("Ten khong duoc rong")
        else:
            break

    # math = input_score("Toan")
    # physics = input_score("Ly")
    # chemistry = input_score("Hoa")
        math = float(input("Nhập điểm Toán "))
        physics = float(input("Nhập điểm Toán "))
        chemistry = float(input("Nhập điểm Toán "))

    avg = calculate_average(math, physics, chemistry)

    rank = classify_student(avg)

    student = {
        "id": student_id,
        "name": name,
        "math": math,
        "physics": physics,
        "chemistry": chemistry,
        "average": avg,
        "rank": rank
    }

    students.append(student)

    print("Them sinh vien thanh cong")


# =========================
# TIM SINH VIEN THEO MA
# =========================

def find_student_by_id(student_id):

    for student in students:
        if student["id"] == student_id:
            return student

    return None


# =========================
# CAP NHAT DIEM
# =========================

def update_student():

    student_id = input("Nhap ma sinh vien: ")

    student = find_student_by_id(student_id)

    if student is None:
        print("Khong tim thay sinh vien")
        return

    print("Nhap diem moi")

    student["math"] = input_score("Toan")
    student["physics"] = input_score("Ly")
    student["chemistry"] = input_score("Hoa")

    student["average"] = calculate_average(
        student["math"],
        student["physics"],
        student["chemistry"]
    )

    student["rank"] = classify_student(
        student["average"]
    )

    print("Cap nhat thanh cong")


# =========================
# XOA SINH VIEN
# =========================

def delete_student():

    student_id = input("Nhap ma sinh vien can xoa: ")

    student = find_student_by_id(student_id)

    if student is None:
        print("Khong tim thay sinh vien")
        return

    confirm = input(
        "Ban co chac muon xoa? (y/n): "
    )

    if confirm.lower() == "y":
        students.remove(student)
        print("Da xoa thanh cong")
    else:
        print("Huy thao tac")


# =========================
# TIM KIEM
# =========================

def search_student():

    print("\n1. Tim theo ma")
    print("2. Tim theo ten")

    choice = input("Lua chon: ")

    if choice == "1":

        student_id = input("Nhap ma sinh vien: ")

        student = find_student_by_id(student_id)

        if student:
            print(student)
        else:
            print("Khong tim thay")

    elif choice == "2":

        keyword = input(
            "Nhap ten can tim: "
        ).lower()

        found = False

        for student in students:

            if keyword in student["name"].lower():

                print(student)

                found = True

        if not found:
            print("Khong tim thay")


# =========================
# THONG KE HOC LUC
# =========================

def statistics():

    gioi = 0
    kha = 0
    trung_binh = 0
    yeu = 0

    for student in students:

        if student["rank"] == "Gioi":
            gioi += 1

        elif student["rank"] == "Kha":
            kha += 1

        elif student["rank"] == "Trung binh":
            trung_binh += 1

        else:
            yeu += 1

    print("\n===== THONG KE =====")

    print("Gioi:", gioi)
    print("Kha:", kha)
    print("Trung binh:", trung_binh)
    print("Yeu:", yeu)


# =========================
# MENU
# =========================

def menu():

    while True:

        print("\n===== QUAN LY SINH VIEN =====")

        print("1. Hien thi danh sach")
        print("2. Them sinh vien")
        print("3. Cap nhat diem")
        print("4. Xoa sinh vien")
        print("5. Tim kiem sinh vien")
        print("6. Thong ke hoc luc")
        print("7. Thoat")

        choice = input("Nhap lua chon: ")

        if choice == "1":
            display_students()

        elif choice == "2":
            add_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            search_student()

        elif choice == "6":
            statistics()

        elif choice == "7":
            print("Tam biet!")
            break

        else:
            print("Lua chon khong hop le")


# =========================
# CHAY CHUONG TRINH
# =========================

menu()