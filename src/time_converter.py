import math
from src.timetable_exceptions import InvalidTimeException

## Right now I'm not using datetime because the time of day for the class
# should be timestamp-independent
## 1440 is the amount of minutes in a single day, starting from 0

def getHoursAndMins(timeNum):
    amtOfHours = math.floor(timeNum / 60)
    amtOfMins = timeNum - (amtOfHours * 60)
    return amtOfHours, amtOfMins

def getPrintedTime(amtOfHours, amtOfMins):
    amtOfHoursStr = "0" + str(amtOfHours) if (amtOfHours < 10) else str(amtOfHours)
    amtOfMinsStr = "0" + str(amtOfMins) if (amtOfMins < 10) else str(amtOfMins)
    return (amtOfHoursStr + ":" + amtOfMinsStr)

def convertTo24Hr(timeNum):
    timeNum = timeNum % 1440
    amtOfHours, amtOfMins = getHoursAndMins(timeNum)
    return getPrintedTime(amtOfHours, amtOfMins)

def convertTo12Hr(timeNum):
    timeNum = timeNum % 1440
    amtOfHours, amtOfMins = getHoursAndMins(timeNum)
    endStr = " AM" if (amtOfHours < 12) else " PM"
    amtOfHours = amtOfHours % 12
    amtOfHours = 12 if amtOfHours == 0 else amtOfHours
    return getPrintedTime(amtOfHours, amtOfMins) + endStr

def timeNumFromString(timeStr):
    timeStrLen = len(timeStr)
    isPM = False
    if not(timeStrLen == 4 or timeStrLen == 6):
        raise InvalidTimeException("Time string format is invalid.")
    elif (timeStrLen == 6):
        meridiem = timeStr[4:]
        if not(meridiem == "AM" or meridiem == "PM"):
            raise InvalidTimeException("Time string format is invalid.")
        isPM = (meridiem == "PM")
    hours = int(timeStr[:2]) % 24
    mins = int(timeStr[2:4])
    if (isPM):
        hours = hours + 12 if hours != 12 else hours
    elif (hours == 12 and timeStrLen == 6):
        hours = 0
    return (hours * 60) + mins
