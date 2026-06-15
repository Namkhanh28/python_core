# phân tích lỗi 
    #old_prescription và new_prescription trỏ đến cùng 1 vùng nhớ khi bạn sửa new_prescription → old_prescription cũng bị ảnh hưởng
    # vi dung append sẽ đẩy vào  mảng chính nên old cung co du lieu da day
    #  new_prescription = old_prescription là không tạo list mới mà gán lại vao list cũ
    # replace() trả về chuỗi mới, không sửa trực tiếp
    #  new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
# sua loi
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]
def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    new_prescription.append("Oresol")
    return new_prescription
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)