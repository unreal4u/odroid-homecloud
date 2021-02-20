#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
An analog clockface with date & time.
"""

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
from PIL import ImageFont, ImageDraw, Image
import time
import datetime
import os

serial = i2c(port=0, address=0x3C)
# device = sh1106(serial, rotate=0)
device = ssd1306(serial, rotate=2)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    today_last_time = "Unknown"
    screen_number = 1
    timer = 0
    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                  #draw.rectangle(device.bounding_box, outline="white")
                  font = ImageFont.truetype('./fonts/roboto-2014/Roboto-Light.ttf', 20)
                  if screen_number == 1:
                        #font = ImageFont.truetype('/home/unreal4u/fonts/ArchivoNarrow-Regular.ttf', 25)
                        draw.text((0, 0), today_time, font=font, fill=1)
                        draw.text((0, 20), 'abcdefghijklm', font=font, fill=1)
                        draw.text((0, 40), 'nopqrstuvwxyz', font=font, fill=1)
                  if screen_number == 2:
                        draw.text((0, 0), 'Hallo', font=font, fill=1)
                  if screen_number == 3:
                        draw.text((0, 0), 'Dag!', font=font, fill=1)
                  timer = timer + 1
                  if timer % 3 == 0:
                        screen_number = screen_number + 1;
                        if screen_number == 4:
                              screen_number = 1;
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
