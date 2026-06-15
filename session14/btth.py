grade_book = [
{"stt" : 1, "id": "SV01", "name": "Nguyễn Van A", "info": (8.5, 7.0)},
{"stt" : 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]
def display_grades (book):
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<5} | {'Tên Học Sinh':<30} | {"Điểm Toán":<10} | {"Điểm Anh":<10} | ĐTB")
    print('-'*70)
    for i in book:
        math = i["info"][0]
        eng = i["info"][1]
        avg = (math+eng)/2
        print(f"{i["id"]:<5} | {i["name"]:<30} | {math:<10} | {eng:<10} | {avg}")
    print('-'*70)

def add_student(book):
    while True:
        student_id = input("Nhập mã học sinh mới: ")

        existed = False
        for student in book:
            if student["id"] == student_id:
                existed = True
                break

        if existed:
            print(f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác.")
        else:
            break

    student_name = input("Nhập tên học sinh: ")
    math_score = float(input("Nhập điểm Toán: "))
    english_score = float(input("Nhập điểm Anh: "))

    new_student = {
        "id": student_id,
        "name": student_name,
        "info": (math_score, english_score)
    }

    book.append(new_student)

    print(f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!")

def update_scores(book):
    student_id = input("Nhập mã học sinh cần cập nhật: ")

    found = False

    for student in book:
        if student["id"] == student_id:
            new_math = float(input("Nhập điểm Toán mới: "))
            new_english = float(input("Nhập điểm Anh mới: "))
            student["info"] = (new_math, new_english)

            print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
            found = True
            break

    if not found:
        print("Không tìm thấy học sinh!")

def delete_student(book):
    student_id = input("Nhập mã học sinh cần xóa: ")

    found = False

    for student in book:
        if student["id"] == student_id:
            book.remove(student)
            print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!")
            found = True
            break

    if not found:
        print("Không tìm thấy học sinh!")

while True:
    choice = input(''' === HỆ THỐNG QUẢN LÝ ĐIEM SỐ ===
1. Xem bảng điểm học sinh
2. Them ho so học sinh moi
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
Chọn chức năng (1-5): ''')
    match choice:
        case '1':
            display_grades(grade_book)
        case '2':
            add_student(grade_book)
        case '3':
            update_scores(grade_book)
        case '4':
            delete_student(grade_book)
        case '5':
            print('Thoat chương trình')
            break
        case _:
            print('Lựa chon khong hợp le')  