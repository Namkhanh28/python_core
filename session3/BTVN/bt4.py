print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
value= True
while value == True:
    number = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    if number<= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.")
        print("") 
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho", {number}, "nhân sự mới!")
        value = False
print(f"--- CHƯƠNG TRÌNH KẾT THÚC ---")