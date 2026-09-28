class Animal :
    def _init_(self,sound,name):
        self.sound=sound
        self.name =name
    def speak(self):
        print(self.sound) 
class Dog(Animal):
    def __init__(self , sound , name,owner):
        super()._init_(sound,name)
        self.owner=owner
    def speak(self):
        print('Chó sủa')
        super().speak()

dog1 = Dog("Gâu Gâu ", 'Choky','An ')
dog1.speak()