print(" --- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN---")
name_patient = input ("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân : "))

print(" --- KIỂM TRA DỮ LIỆU LƯU TRỮ --- ")
print (f"Bệnh nhân :{ name_patient} ")
print (f"Cân nặng dã nhập :{weight} ")

# Trưởng nhóm IT viết thêm dòng này dể kiểm tra dữ liệu của cân nặng và kết quả CẢNH BAO - Kiểu dữ Liệu dang lưu là :<class 'str'> 
print (f"CẢNH BAO - Kiểu dữ Liệu dang lưu là :{type(weight)} ")

# Lỗi là chưa ép kiểu dữ liệu cho biến weight nên nhập vào Python sẽ lưu string 
