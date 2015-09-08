from enum import Enum

class Timetable(object):
    """Represents a timetable."""
    def __init__(self):
        super(Timetable, self).__init__()
        self.coursesList = []
        self.startDate = 0
        self.endDate = 0

class Course(object):
    """Represents a course within the timetable."""
    def __init__(self):
        super(Course, self).__init__()
        self.courseSlots = []
        self.courseCode = ""
        self.teacher = ""
        self.description = ""

class TimeSlot(object):
    """Represents a time slot for a course."""
    def __init__(self):
        super(TimeSlot, self).__init__()
        self.slotType = ""
        self.day = 0
        self.room = ""
        self.timeStart = 0
        self.timeEnd = 0

class SlotType(Enum):
    """Type of time slot the course's time slot may have."""
    none = 0
    lecture = 1,
    lab = 2,
    exam = 3
