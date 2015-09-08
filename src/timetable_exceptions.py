class InvalidTimetableException(Exception):
    """Error that occurs when a Timetable object is expected,
    but not provided or doesn't have the correct members."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class TimetableParseError(Exception):
    """Error that occurs when there is a problem parsing the timetable."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidCalendarDateException(Exception):
    """Error that occurs when the calendar value sent for parsing
    doesn't have the correct format."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidTimeException(Exception):
    """Error that occurs when a slot time's time string
    is formatted incorrectly."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
