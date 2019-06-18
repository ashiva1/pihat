#!/usr/bin/env python 
# this script will display colors for individual pixels on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.set_pixel(7, 3, (255,0,0))
sense.set_pixel(6, 3, (255,0,0))
sense.set_pixel(6, 2, (255,0,0))
sense.set_pixel(6, 4, (255,0,0))
sense.set_pixel(5, 3, (255,0,0))
sense.set_pixel(5, 2, (255,0,0))
sense.set_pixel(5, 4, (255,0,0))

sense.set_pixel(5, 1, (255,0,0))
sense.set_pixel(5, 5, (255,0,0))

sense.set_pixel(4, 3, (255,0,0))
sense.set_pixel(4, 2, (255,0,0))
sense.set_pixel(4, 1, (255,0,0))
sense.set_pixel(4, 4, (255,0,0))

sense.set_pixel(4, 5, (255,0,0))
sense.set_pixel(4, 6, (255,0,0))
sense.set_pixel(4, 7, (255,0,0))
sense.set_pixel(4, 0, (255,0,0))
time.sleep(1)
sense.clear()
