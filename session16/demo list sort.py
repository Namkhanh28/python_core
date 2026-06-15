grade_book = [
{"stt" : 1, "id": "SV01", "name": "Nguyễn Van A", "info": (8.5, 7.0)},
{"stt" : 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
{"stt" : 1, "id": "SV03", "name": "Nguyễn Danh A", "info": (8.5, 9.0)},
{"stt" : 2, "id": "SV04", "name": "Trần Thị Bình", "info": (7.0, 9.0)},
]
# Sắp xếp danh sách theo tên
# names = [student['name'] for student in grade_book]
# names.sort()
# print(names)

grade_book.sort(key = lambda student :(student['info'][0] + student['info'][1])/2 , reverse=True) 
grade_book = sorted(grade_book ,key = lambda student :(student['info'][0] + student['info'][1])/2 , reverse=True)
print(grade_book)
 