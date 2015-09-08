from os import getcwd
from configparser import ConfigParser

# Config filepath
CONFIG_FILE = getcwd() + "/config.ini"
# Read config from config file
config = ConfigParser()
config.read(CONFIG_FILE)
# Preferences set from config file
use12HrFormat = config["Main"].getboolean("12HrTimeFormat")
currentTimetable = config["Main"]["CurrentTimetable"]

def saveConfig():
    config["Main"]["12HrTimeFormat"] = "True" if use12HrFormat else "False"
    config["Main"]["CurrentTimetable"] = currentTimetable
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
