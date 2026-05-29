student_name =" nguYEn vAn a "
student_code = " rk-001-python "
email = " Student01@GMAIL.COM "

student_name = student_name.strip()
student_name = student_name.title()

student_code = student_code.strip()
student_code = student_code.upper()

email = email.strip()
email = email.lower()

print("Ho tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)

# '''1. Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
# Vì strip() không sửa trực tiếp chuỗi gốc mà chỉ tạo ra một chuỗi mới sau khi xóa khoảng trắng. Biến student_name vẫn giữ nguyên giá trị cũ.

# 2. Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A"?
# Vì title() chỉ trả về chuỗi mới với chữ cái đầu được viết hoa. Kết quả không được lưu lại nên biến không thay đổi.

# 3. Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
# Vì upper() tạo ra một chuỗi mới viết hoa toàn bộ ký tự. Nếu không gán lại thì giá trị cũ vẫn được giữ nguyên.

# 4. Vì sao email.lower() không làm email chuyển thành chữ thường?
# Vì lower() chỉ trả về chuỗi mới ở dạng chữ thường. Biến email không tự cập nhật giá trị mới.