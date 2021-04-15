import random
from math import sqrt

class Rocket:
    def __init__(self, speed=1, altitude = 0, x=0):
        self.altitude = altitude

        self.speed = speed

        self.x = 0

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rocketList = [Rocket(random.randint(1,6)) for _ in range(amountOfRockets)]

        for rockets in range(10):
            rocketIndexToMove = random.randint(0, len(self.rocketList) - 1)
            self.rocketList[rocketIndexToMove].moveUp()

        for rocket in self.rocketList:
            print(rocket)

    def __getitem__(self, key):
        return self.rocketList[key]
    def __setitem__(self, key, value):
        self.rocketList[key].altitude = value


    @staticmethod
    def get_distance(rocket: Rocket, rocket2: Rocket):
        xs = (rocket.altitude - rocket2.altitude) ** 2
        ys = (rocket.x - rocket2.x) ** 2
        return sqrt(xs + ys)

    def __len__(self):
        return len(self.rocketList)