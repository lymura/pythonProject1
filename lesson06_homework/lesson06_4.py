class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
       print("Go")


    def stop(self):
        print("Stop")
    def turn(left, direction):
        print(f'Turn to {direction}')


    def show_speed(self):
        print(f'Current speed = {self.speed}')

class SportCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        super().show_speed
        if self.speed > 40:
            print(f" Increased speed!")

class WorkCar(Car):
   def show_speed(self):
       super().show_speed
       if self.speed > 60:
           print(f" Increased speed!")


class PoliceCar(Car):
    def __init(self, speed, color, name):
        super().__init__(speed, color, name, True)

tc = TownCar(45, "white", "Town")
sc = SportCar(140, "pink", "Sport")
wc = WorkCar(65, "orange", "Work")
pc = PoliceCar(120, "red", "Police")

tc.show_speed()
wc.show_speed()
pc.show_speed()
sc.show_speed()

#wc.speed = 50
#wc.show_speed()
#tc.speed = 30
#tc.show_speed()

pc.turn('right')
