import time

class TrafficLight:
    colors = ('красный', 'желтый', 'зеленый')
    time_delay = (7, 2, 7)

    def __init__(self):
        self.__color = "зеленый"

    def running(self):

       while True:
        for i in self.colors:
            self.__color = i
            print(self.__color)
            time.sleep(self.time_delay[self.colors.index(self.__color)])

tl = TrafficLight()
tl.running()