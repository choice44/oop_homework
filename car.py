class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount

    def get_speed(self):
        return self.speed


car = Car('트레일블레이저', '새비지블루')
car.accelerate(80)
car.brake(40)
print(car.get_speed())
