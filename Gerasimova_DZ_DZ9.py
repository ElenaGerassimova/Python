print('Задание 1')
import time


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 10))

    def running(self):
        for color, time_traffic_light in self.__color:
            print(f'{color} {time_traffic_light} sec')
            time.sleep(int(time_traffic_light))


traffic_light = TrafficLight()
while True:
    traffic_light.running()