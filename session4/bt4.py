so_bi_mat = 50
so_luot_toi_da = 5
da_doan_dung = False

print("=== TRÒ CHƠI ĐOÁN SỐ MAY MẮN ===")
print("Bạn có 5 lượt để đoán số bí mật")
for luot in range(1,6,1):
    while True:
        du_doan_str = input(f"Lượt {luot} - Nhập số bạn đoán: ")
        if not du_doan_str.isdigit():
            print(" Vui lòng nhập số hợp lệ!")
        else:
            du_doan = int(du_doan_str)
            break
    if du_doan == so_bi_mat:
        print(" Chính xác!")
        print(f"Số may mắn là: {so_bi_mat}")
        da_doan_dung = True
        break
    elif du_doan > so_bi_mat:
        print("📉 Số bạn đoán LỚN HƠN số bí mật")
    else:
        print("📈 Số bạn đoán NHỎ HƠN số bí mật")
print("\n===== KẾT QUẢ =====")
if da_doan_dung:
    print(" Chúc mừng bạn đã trúng thưởng!")
else:
    print(" Bạn đã hết lượt!")
    print("Chúc bạn may mắn lần sau!")