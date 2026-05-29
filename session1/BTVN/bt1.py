
name_patient = input ('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input ('Mời bạn nhập triệu chứng bênh: ')

print(' -- PHIẾU KHÁM BỆNH --- ')
print(f'Tên bệnh nhân: {name_patient}')
print(f'Tuổi: {age}')
print(f'Triệu chứng: {symptom}')

# Lỗi mắc phải ở đây là đặt các biến không đúng chỗ dẫn đến tham chiếu sai thông tin 
# Thừa dấu chấm phẩy vì Python không cần dùng đến chấm phẩy để kết thúc câu lệnh 