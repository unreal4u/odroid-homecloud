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
                  awesome_font = ImageFont.truetype('../fonts/fontawesome-webfont.ttf', 25)
                  text_font = ImageFont.truetype('../fonts/roboto-2014/Roboto-Light.ttf', 20)
                  if screen_number == 1:
                        draw.text((0, 0), today_time, font=text_font, fill=1)
                        draw.text((0, 25), "\uf185", font=awesome_font, fill=1)
                        draw.text((25, 25), '18°', font=text_font, fill=1)
                        draw.text((60, 25), "\uf015", font=awesome_font, fill=1)
                        draw.text((85, 25), '19°', font=text_font, fill=1)
                  if screen_number == 2:
                        draw.text((0, 0), "\uf019", font=awesome_font, fill=1)
                        draw.text((25, 0), '287.73 Mbps', font=text_font, fill=1)
                        draw.text((0, 25), "\uf066", font=awesome_font, fill=1)
                        draw.text((25, 25), '26 clients', font=text_font, fill=1)
                  if screen_number == 3:
                        draw.text((0, 0), "\uf0e7", font=awesome_font, fill=1)
                        draw.text((20, 0), 'Tar.: Normal', font=text_font, fill=1)
                        draw.text((0, 25), "\uf0e7", font=awesome_font, fill=1)
                        draw.text((20, 25), '2.52 kW', font=text_font, fill=1)
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
