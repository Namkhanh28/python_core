# # Biến toàn cục lưu tổng điểm hiện tại của khách hàng
# total_points = 100
# # Hàm cộng điểm thưởng
# def add_reward_points(points_earned):
#     # Cố gắng lấy tổng điểm cũ cộng thêm điểm mới
#     total_points = total_points + points_earned
#     print("Đã cộng thêm", points_earned, "điểm.")

# # Khách mua hàng được thưởng 50 điểm
# add_reward_points(50)

# # In ra kết quả
# print("Tổng điểm hiện tại của khách hàng:", total_points)



# Hàm không có return
#total_points = total_points + points_earned
# Python thấy có dấu "=" nên hiểu total_points là biến LOCAL
# Nhưng biến này chưa được gán giá trị trước đó => gây lỗi

def add_reward_points(current_points, points_earned):
    total = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return total
total_points = 100
total_points = add_reward_points(total_points, 50)
print("Tổng điểm hiện tại của khách hàng:", total_points)