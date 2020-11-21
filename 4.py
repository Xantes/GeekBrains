from time import sleep


class Car():

    max_speed = 240

    def __init__(self, color, name):
        self.speed = float(0)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        while self.speed < self.max_speed:
            self.speed += 1
            sleep(1)

    def stop(self):
        while self.speed > 0:
            self.speed -= 1

    def change_direction(self, direction):
        self.direction = direction

    def show_speed(self):
        return self.speed


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        if self.speed > self.max_speed:
            return f"Превышение скорости на {self.speed - self.max_speed} км."
        else:
            return self.speed


class WorkCar(TownCar):
    max_speed = 40


class SportCar(Car):
    max_speed = 40


class PoliceCar(Car):
    def __init__(self, name):
        self.speed = float(0)
        self.color = "Black and White"
        self.name = name
        self.is_police = True


car = Car('car', 'red')
work_car = WorkCar('workcar', 'blue')
town_car = TownCar('towncar', 'yellow')
sport_car = SportCar('sportcar', 'black')
police_car = PoliceCar('policecar')

print(work_car.speed, work_car.max_speed)
print(town_car.speed, town_car.max_speed)
