tong_tien_input = input("Nhập tổng số tiền hóa đơn (VND): ")
if tong_tien_input == "" or not tong_tien_input.isdigit():
    print("Yêu cầu nhập đúng số tiền")
else:
    tong_tien = int(tong_tien_input)
    if tong_tien < 0:
        print("Yêu cầu nhập số tiền >= 0")
    else:
        if tong_tien >= 500000:
            giam_gia = tong_tien * 0.1
        else:
            giam_gia = 0
        so_tien_phai_tra = tong_tien - giam_gia
        print("Số tiền giảm giá:", int(giam_gia), "VND")
        print("Số tiền khách phải trả:", int(so_tien_phai_tra), "VND")
