# creating a class
class Person:
    # constructor 
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f'My name is {self.name}, i am {self.gender} of age {self.age}')
        
        
        
info = Person('James',25,'Males')

info.introduce()