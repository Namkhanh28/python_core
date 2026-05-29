tong_doanh_thu = 0
so_ngay_dat_muc_tieu = 0
for i in range(1, 8):
    doanh_thu = int(input(f"Nhập doanh thu Ngày {i} (VND): "))
    tong_doanh_thu += doanh_thu
    if doanh_thu >= 5000000:
        so_ngay_dat_muc_tieu += 1
trung_binh = tong_doanh_thu / 7
print("\n===== BÁO CÁO DOANH THU TUẦN =====")
print("Tổng doanh thu:", tong_doanh_thu, "VND")
print("Doanh thu trung bình:", int(trung_binh), "VND/ngày")
print("Số ngày đạt mục tiêu:", so_ngay_dat_muc_tieu)