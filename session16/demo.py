grade_book = [
{"stt" : 1, "id": "SV01", "name": "Nguyễn Van A", "info": (8.5, 7.0)},
{"stt" : 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
{"stt" : 1, "id": "SV03", "name": "Nguyễn Danh A", "info": (8.5, 9.0)},
{"stt" : 2, "id": "SV04", "name": "Trần Thị Bình", "info": (7.0, 9.0)},
]
name_list = grade_book[0]['name'].split()
print(f'Họ : {name_list[0]} Tên đệm {name_list[1]} Tên riêng{name_list[2]} ')
full_name = ''.join(name_list)
print(full_name)
def printstudent():
    print("Danh sách sinh viên")
    for student in grade_book:
        print('{id:<7}|{name:<20}|'.format_map(student))
printstudent()