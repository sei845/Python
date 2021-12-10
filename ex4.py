class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
        print(f"{self.name}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed}")


class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - Превышение скорости!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}"


class TownCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - Превышение скорости!" \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля - {self.speed}"


class SportCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - Превышение скорости!" \
            if self.speed > 100 else f"{self.name}: Скорость автомобиля - {self.speed}"


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


work_car = WorkCar('Газ', 'Серый', 45)
town_car = TownCar('KIA', 'Черный', 55)
sport_car = SportCar('Ferrari', 'Красный', 95)
police_car = PoliceCar('ДПС', 'Белый', 80)
print(work_car.show_speed())
town_car.turn(1)
sport_car.stop()
police_car.go()
