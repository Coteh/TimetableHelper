import json
from src import date_converter, time_converter, timetable_converter
from src.timetable_types import Timetable, Course, TimeSlot, SlotType
from src.timetable_exceptions import InvalidTimeException, TimetableParseError

def parse_object_pairs(pairs):
    return pairs

def readTimetableJSON(timetable_buf):
    decoder = json.JSONDecoder(object_pairs_hook=parse_object_pairs)
    try:
        jsonList = decoder.decode(timetable_buf)
    except ValueError as e:
        raise TimetableParseError("Timetable was not decoded from JSON properly.")
    # first node in jsonList has to say timetable_version, otherwise throw error
    if (len(jsonList) <= 0 or jsonList[0][0] != "timetable_version"):
        raise TimetableParseError("These JSON contents don't appear to be a timetable JSON.")
    # construct Timetable object from JSON values
    timetable = Timetable()
    for jsonValue in jsonList:
        if (jsonValue[0] == "start_date"):
            timetable.startDate = jsonValue[1]
        elif (jsonValue[0] == "end_date"):
            timetable.endDate = jsonValue[1]
        elif (jsonValue[0] == "course"):
            # collect info about the course and put it into a new Course instance
            course = Course()
            for courseVal in jsonValue[1]:
                if (courseVal[0] == "slot"):
                    # collect info about a time slot and place it into a new TimeSlot instance
                    timeSlot = TimeSlot()
                    for slotVal in courseVal[1]:
                        if (slotVal[0] == "type"):
                            timeSlot.slotType = timetable_converter.slotTypeStringAsType(slotVal[1])
                        elif (slotVal[0] == "day"):
                            timeSlot.day = date_converter.dayAsNum(slotVal[1])
                        elif (slotVal[0] == "room"):
                            timeSlot.room = slotVal[1]
                        elif (slotVal[0] == "time_start"):
                            try:
                                timeSlot.timeStart = time_converter.timeNumFromString(slotVal[1])
                            except InvalidTimeException as e:
                                timeSlot.timeStart = 0
                        elif (slotVal[0] == "time_end"):
                            try:
                                timeSlot.timeEnd = time_converter.timeNumFromString(slotVal[1])
                            except InvalidTimeException as e:
                                timeSlot.timeEnd = 0
                    course.courseSlots.append(timeSlot) # add the time slot to the course's slot list
                elif (courseVal[0] == "code"):
                    course.courseCode = courseVal[1]
                elif (courseVal[0] == "teacher"):
                    course.teacher = courseVal[1]
                elif (courseVal[0] == "description"):
                    course.description = courseVal[1]
            timetable.coursesList.append(course) # add the course to the timetable's course list
    return timetable
