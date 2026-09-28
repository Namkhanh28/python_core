# class Vector:
#     def __init__(self,x,y):
#         self.x =x
#         self.y= y
#     def  __add__ (self,other):
#         return Vector(
#         self.x+ other.x,
#         self.y + other.y)
#     def __str__(self):
#         return f"({self.x},{self.y})"
# v1 = Vector(1,3)
# v2 =Vector(3,4)
# v3 =v1+v2
# print(v3)

from abc import ABC, abstractmethod
# 1. Khởi tạo lớp trừu tượng
class HinhHoc(ABC):
    
    @abstractmethod
    def tinh_dien_tich(self):
        pass
    
    @abstractmethod
    def tinh_chu_vi(self):
        pass
    
# 2. Lớp con kế thừa và bắt buộc phải triển khai phương thức trừu tượng
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
        
    def tinh_dien_tich(self):
        return 3.14 * self.ban_kinh * self.ban_kinh
        
    def tinh_chu_vi(self):
        return 2 * 3.14 * self.ban_kinh

# 3. Sử dụng
# hinh = HinhHoc()  # SẼ BÁO LỖI: Không thể khởi tạo abstract class
hinh_tron = HinhTron(5)
print("Diện tích hình tròn:", hinh_tron.tinh_dien_tich())