from hrm_package.ui_display import display_records
attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, # Đang làm việc, chưa chấm công ra
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]

while True:
    choice=input('''=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===
1. Xem bảng chấm công ngày
2. Chấm công Vào (Clock-in)
3. Chấm công Ra (Clock-out)
4. Đánh giá vi phạm
5. Thoát chương trình 
================================================= 
Chọn chức năng (1-5): ''')
    match choice:
        case "1":
            display_records(attendance_book)
            break
        case "5":
            print("Thoat")
            break
        case _:
            print("Nhap lai")