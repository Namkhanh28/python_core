students = [
    {"id": "SV001", "name": "Nguyen Van A", "math_score": 8.5, "physics_score": 7.0, "chemistry_score": 9.0},
    {"id": "SV002", "name": "Tran Thi B", "math_score": 7.8, "physics_score": 8.2, "chemistry_score": 7.5},
    {"id": "SV003", "name": "Le Van C", "math_score": 9.2, "physics_score": 8.8, "chemistry_score": 9.5}
]
def avg(student):
    avg_point = (student['math_score']+student['physics_score']+student['chemistry_score'])/3
    return avg_point
def classify(avg_point):

    if avg_point < 5:
        return "Yeu"

    elif avg_point < 7:
        return "Trung binh"

    elif avg_point < 8:
        return "Kha"

    else:
        return "Gioi"
def display(student_list):
        if len(student_list)==0:
            print("Không có sinh viên trong danh sách")
            return
        else :
               print(
        f"{'MÃ SV':<10}|"
        f"{'HỌ TÊN':<25}|"
        f"{'TOÁN':<10}|"
        f"{'LÝ':<10}|"
        f"{'HÓA':<10}|"
        f"{'ĐTB':<10}|"
        f"{'HỌC LỰC':<15}"
    )
               print('='*100)
               for student in student_list:
                   avg_score = avg(student)
                   rank = classify(avg_score)
                   print(
                f"{student['id']:<10}|"
                f"{student['name']:<25}|"
                f"{student['math_score']:<10}|"
                f"{student['physics_score']:<10}|"
                f"{student['chemistry_score']:<10}|"
                f"{ avg_score:<10}|"
                f"{ rank:<15}"
                   )

def add_student(student_list):
    while True:
        find = False
        new_id = input(
            "Nhập mã sinh viên mới: "
        ).strip().upper()

        if not new_id:
            print("Yêu cầu nhập lại thông tin")
            continue
        # Kiểm tra trùng mã
        for student in student_list:

            if new_id == student["id"]:
                find = True
                break

        if find:
            print("Sinh viên này đã tồn tại trong danh sách")
            continue
        new_name = input(
            "Nhập tên sinh viên: "
        ).strip()
        new_math_score = float(
            input("Nhập điểm Toán: ")
        )
        new_physics_score = float(
            input("Nhập điểm Lý: ")
        )
        new_chemistry_score = float(
            input("Nhập điểm Hóa: ")
        )
        new_student = {
            "id": new_id,
            "name": new_name,
            "math_score": new_math_score,
            "physics_score": new_physics_score,
            "chemistry_score": new_chemistry_score
        }
        student_list.append(new_student)
        print("Thêm sinh viên thành công")
        return








       
    


def main():
    while True:
        choice = input('''
        CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN
        ==============================
        1, Hiển thị danh sách sinh viên
        2, Tiếp nhận thêm sinh viên
        3,Cập nhật kết quả học tập 
        4, Xóa sinh viên 
        5, Tìm kiếm sinh viên 
        6, Thống kê điểm trung bình 
        7,Phân loại học lực
        8, Thoát chương trình
        ==============================
        Nhập lựa chọn chức năng:
''')
        match choice:
            case "1":
               display(students)
            case "2":
                add_student(students)
            case '3':
                pass
            case "4":
                pass
            case "5":
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                print("Thoát chương trình ")
                break
            case _:
                print("Lựa chọn không hợp lệ")
main()