import mouse
import keyboard
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read("Config/binds.ini")

while True:
    if keyboard.is_pressed(config['starts-with']['key']):
        while True:
            sleep(0.01)
            mouse.double_click(button='left')
            if keyboard.is_pressed(config['stops-with']['key']):
                break

