#! /usr/bin/env/python
from configmaker import *
from simulation import *

r=ReadConfig()
s=Simulation(r[6],r[0],r[1],r[2],r[3],r[4],r[5])
s.Run()
print('END')
