so_luong_phong = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if so_luong_phong <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for phong in range(1, so_luong_phong + 1):
        print(f"\n--- Đang thiết lập Phòng {phong} ---")
        
        so_hang = int(input("Nhập số hàng ghế: "))
        so_ghe = int(input("Nhập số ghế trên mỗi hàng: "))
        
        if so_hang > 10 or so_ghe > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break  
            
        if so_hang <= 0 or so_ghe <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue 
            
        print("Sơ đồ chỗ ngồi:")
        
        for hang in range(so_hang):
            for ghe in range(so_ghe):
                print("*", end="")
                
            print()