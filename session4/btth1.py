name = input("->> Nhập tên bệnh nhân:").strip()
input_year = int(input("->> Nhập vào năm sinh"))
input_sick_day =int(input("->Nhập số ngày bị bệnh"))
input_body_temp =float(input("-> Nhập nhiệt độ cơ thể (độ C)"))
input_price =float(input("Nhập chi phí khám :"))

if name=='':
    print("Tên không được để trống")

if input_year =="":
    print("Không để trống năm sinh")
else :
    birth_year = int(input_year)
    if(birth_year < 1900 or birth_year >2026):
        print("Năm sinh không hợp lệ")
if(input_sick_day==""):
    print("Không được để trống trường ngày bị bệnh")
    
if(input_body_temp ==""):
    print("KHông được để trống dữ liệu ")
else :
    body_temp = float(input_body_temp)
    if(body_temp<36.5 or body_temp>40):
        print("Nhiệt độ cơ thể không hợp!!")

if(input_price==''):
    print("không được để trống giá")
else:
    price =float(input_price)
    if(price <0):
        print("Chi phí không hợp lệ !!")
