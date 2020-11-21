from time import sleep


class TrafficLight():
    __color = str()

    def running(self):
        modes = ['Red', 'Yellow', 'Green', 'Yellow', 7, 2, 7, 2]
        while True:
            for i in range(len(modes[0:4:])):
                self.__color = modes[i]
                print(self.__color)
                sleep(modes[i+4])


first_light = TrafficLight()
first_light.running()
