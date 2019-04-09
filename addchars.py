#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.2
    upm = 1000.0/2048.0
    scale = str(upm/workshop)

    for sn in stylesName:
        modifyFile(scale, 'gentium', f, sn)
