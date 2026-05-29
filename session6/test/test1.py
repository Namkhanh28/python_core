# Câu 1: Khởi động - Tính tiền thanh toán (3 điểm) 
# Viết chương trình tính tiền mua hàng cho khách.
# Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
# Tính Tổng tiền = Đơn giá * Số lượng.
# Áp dụng logic khuyến mãi:
# Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
# Nếu Tổng tiền < 1.000.000, không giảm giá.
# In ra màn hình số tiền cuối cùng khách phải thanh toán.

price_input = input("Nhập giá của đơn hàng")
if price_input <=0 or price_input=="":
    print("yêu cầu nhập đúng thông tin")
else:
    price=int(price_input)
product_number_input = input("Nhập vào số lượng mua hàng")
if product_number_input <=0 or product_number_input=="":
    print("yêu cầu nhập đúng thông tin")
else:
    product_number=int(product_number_input)

total_price = price*product_number
if total_price < 1000000:
    print(f"Đơn hàng giá :{total_price} VND")
else:
    total_price = price*0.9
    print(f"Đơn hàng phải trả giá {total_price}VND")