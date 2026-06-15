grade_book = [
{"stt" : 1, "id": "SV01", "name": "Nguyễn Van A", "info": (8.5, 7.0)},
{"stt" : 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
{"stt" : 1, "id": "SV03", "name": "Nguyễn Danh A", "info": (8.5, 9.0)},
{"stt" : 2, "id": "SV04", "name": "Trần Thị Bình", "info": (7.0, 9.0)},
]
# Tạo danh sách chỉ chứa tên sinh viên 
names =[]
for student in grade_book :
    names.append(student['name'])
print(names)
names=list(map(lambda student : student['name'],grade_book))
print(names)
#DÙng vòng lặp for
