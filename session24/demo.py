class Student:
    def __init__(self,id ,name,age =19):
        self.id = id
        self.name =name
        self.age =age

    def sayHello(self):
        print('Hello ')
    @staticmethod
    def check_age(self):
        return self.age >= True 
    
s1 =Student(1, 'Nguyễn Văn A')
s2 =Student(2, 'Nguyễn thi B',-50)
s1.sayHello = sayHello()
print(s1.name)
print(s2.name)
 