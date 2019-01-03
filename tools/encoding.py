#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
lettera = font['u0D05']
lettera.name = 'avowel'

# Save UFO
font.changed()
font.save()
font.close()
