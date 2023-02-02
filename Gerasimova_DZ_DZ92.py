print('Задание 2')
class Road:
    def __init__(self, length_road, width_road):
        self._length = length_road
        self._width = width_road

    def result(self):
        weight = self._length * self._width * 25 * 5 / 1000
        return weight


road = Road(31, 5000)
print(road.result())