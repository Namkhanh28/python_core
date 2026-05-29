# Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật (4 điểm) 
# Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình.
password =123456
count = 0
while count<3:
    input_password = int(input("Hãy nhập mật khẩu(Chỉ được phép nhập 3 lần)"))
    if password==input_password:
        print("Đăng nhập thành công")
        break
    else:
        print("Đăng nhập thất bại,vui lòng đăng nhập lại")
        count+=1   
        if input_password =="":
            print("Hãy nhập lại đầy đủ thông tin")
    if count==3:
        print("Đăng nhập thất bại")
        break