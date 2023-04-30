class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('동물이 울음소리를 냅니다.')


class Dog(Animal):
    def speak(self):
        print('개가 짖습니다.')


class Cat(Animal):
    def speak(self):
        print('고양이가 웁니다.')
