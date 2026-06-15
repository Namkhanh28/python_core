ds_diem = []
student_number = int(input("Nhập số lượng học sinh: "))

for student in range(student_number):
    diem = float(input(f"Nhập điểm học sinh thứ {student+1} (0-10, nhập -1 để kết thúc): "))
    if diem <0:
        break
    if 0 <= diem <= 10:
        ds_diem.append(diem)
    else:
        print("Điểm không hợp lệ, vui lòng nhập lại!")

print("\nDanh sách điểm học sinh:")
for i, d in enumerate(ds_diem, start=1):
    print(f"Học sinh {i}: {d}")

if len(ds_diem) > 0:
    diem_tb = sum(ds_diem) / len(ds_diem)
    print(f"\nĐiểm trung bình của lớp: {diem_tb:.2f}")
else:
    print("\nKhông có dữ liệu điểm để tính trung bình.")


for ito,point in enumerate(ds_diem,start=0):
    if point >=5:
        ito+=1
print(f"Số học sinh đạt (>=5): {ito}")
