# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
delivery_orders[2] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL")

transferred_order = delivery_orders.pop()

# In kết quả
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)