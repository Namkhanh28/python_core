# 1. Nhập dữ liệu
ten = input("Nhập tên bệnh nhân: ")
nam_sinh = int(input("Nhập năm sinh: "))
so_ngay = int(input("Nhập số ngày bị bệnh: "))
nhiet_do = float(input("Nhập nhiệt độ cơ thể (°C): "))
chi_phi = float(input("Nhập chi phí khám: "))

NAM_HIEN_TAI = 2026

if ten == "":
    print("Lỗi: Tên không được để trống")
elif nam_sinh < 1900 or nam_sinh > NAM_HIEN_TAI:
    print("Lỗi: Năm sinh không hợp lệ")
elif so_ngay < 0:
    print("Lỗi: Số ngày bị bệnh phải >= 0")
elif nhiet_do < 30 or nhiet_do > 45:
    print("Lỗi: Nhiệt độ không hợp lệ")
elif chi_phi <= 0:
    print("Lỗi: Chi phí phải > 0")

else:
    tuoi = NAM_HIEN_TAI - nam_sinh
    phu_phi = chi_phi * 0.1
    tong_chi_phi = chi_phi + phu_phi

    if nhiet_do > 38 and so_ngay > 3:
        tinh_trang = "Nguy hiểm"
    elif nhiet_do > 38:
        tinh_trang = "Sốt cao"
    elif nhiet_do > 37.5:
        tinh_trang = "Sốt nhẹ"
    else:
        tinh_trang = "Bình thường"

    if tinh_trang == "Nguy hiểm":
        if tuoi > 60:
            uu_tien = "Cấp cứu"
        else:
            uu_tien = "Ưu tiên cao"
    else:
        uu_tien = "Bình thường"

   
    muc_chi_phi = "Cao" if tong_chi_phi > 500000 else "Thấp"

    # 7. In kết quả
    print("\n===== KẾT QUẢ =====")
    print("Tên:", ten)
    print("Tuổi:", tuoi)
    print("Tình trạng:", tinh_trang)
    print("Ưu tiên:", uu_tien)
    print("Tổng chi phí:", tong_chi_phi)
    print("Mức chi phí:", muc_chi_phi)