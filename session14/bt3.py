
students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]
def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for i, student in enumerate(student_list, start=1):
        print(f"{i}. Mã: {student['student_id']} | "
              f"Tên: {student['name']} | "
              f"Toán: {student['math_score']} | "
              f"Anh: {student['english_score']}")

def validate_score(score_input):
    if score_input.replace('.', '', 1).isdigit():
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        else:
            return False
    else:
        return False

def add_student(student_list):
    student_id = input("Nhập mã học viên: ").strip().upper()
    name = input("Nhập tên học viên: ").strip().title()

    while True:
        math = input("Nhập điểm Toán: ")
        if validate_score(math):
            math = float(math)
            break
        else:
            print("Điểm không hợp lệ (0-10)!")

    while True:
        eng = input("Nhập điểm Anh: ")
        if validate_score(eng):
            eng = float(eng)
            break
        else:
            print("Điểm không hợp lệ (0-10)!")

    student = {
        "student_id": student_id,
        "name": name,
        "math_score": math,
        "english_score": eng
    }

    student_list.append(student)
    print("Thêm học viên thành công!")

def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def update_score(student_list):
    student_id = input("Nhập mã học viên: ").strip().upper()
    student = find_student_by_id(student_list, student_id)

    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
    while True:
        math = input("Nhập điểm Toán mới: ")
        if validate_score(math):
            student["math_score"] = float(math)
            break
        else:
            print("Điểm không hợp lệ!")

    while True:
        eng = input("Nhập điểm Anh mới: ")
        if validate_score(eng):
            student["english_score"] = float(eng)
            break
        else:
            print("Điểm không hợp lệ!")

    print("Cập nhật thành công!")


def get_rank(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def evaluate_students(student_list):
    if len(student_list) == 0:
        print("Danh sách trống!")
        return

    for student in student_list:
        avg = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(avg)

        print(f"Mã: {student['student_id']} | "
              f"Tên: {student['name']} | "
              f"ĐTB: {avg:.2f} | "
              f"Xếp loại: {rank}")

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ =====
1. Hiển thị danh sách
2. Thêm học viên
3. Cập nhật điểm
4. Đánh giá học lực
5. Thoát
""")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ!")