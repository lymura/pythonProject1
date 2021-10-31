class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_value(self, m, thickness):
        return self._length * self._width * m * thickness / 1000

r = Road(5000, 20)
print(r.get_value(25, 5))
