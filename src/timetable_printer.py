from src import timetable_config, date_converter, time_converter, timetable_types, timetable_converter
from src.timetable_exceptions import InvalidTimetableException

smallDashes = "---------------------"
bigDashes = "------------------------------"

def printInfo(timetable):
	""" Prints general info about the timetable.
	:param timetable: The timetable object to print out.
	"""
	# check to see if this is a timetable instance before continuing, otherwise throw error
	startDate = 0
	try:
		startDate = timetable.startDate
	except AttributeError as e:
		raise InvalidTimetableException("Timetable is invalid.")
	print(bigDashes + "\n"
		+ "Start Date: " + date_converter.calendarDateAsString(startDate) + "\n"
		+ "End Date: " + date_converter.calendarDateAsString(timetable.endDate) + "\n"
		+ "Courses in this semester: ")
	for course in timetable.coursesList:
		print(course.courseCode + ": " + course.teacher + "\n\tDescription: " + course.description.split('\n')[0] + "\n\tAmount of time slots: " + str(len(course.courseSlots)))
	print(bigDashes)

def printClasses(timetable, dayInt):
	""" Prints all classes that occur on a particular day.
	:param timetable: The timetable object to print out.
	:param dayInt: The day of the week in integer form. See date_converter's dayOfWeekList for ordering.
	"""
	coursesList = []
	try:
		coursesList = timetable.coursesList
	except AttributeError as e:
		raise InvalidTimetableException("Timetable is invalid.")
	isAnyClasses = False
	for course in coursesList:
		isCourseInfoPrinted = False
		for slot in course.courseSlots:
			if (slot.day == dayInt):
				if (not isAnyClasses):
					print(bigDashes + "\n"
						+ "Classes scheduled for " + date_converter.dayAsString(dayInt) + ":\n"
						+ bigDashes)
					isAnyClasses = True
				if (not isCourseInfoPrinted):
					print(course.courseCode + "\n"
						+ course.teacher + "\n"
						+ course.description + "\n"
						+ smallDashes)
					isCourseInfoPrinted = True
				timeStart, timeEnd = "", ""
				if (timetable_config.use12HrFormat):
					timeStart, timeEnd = time_converter.convertTo12Hr(slot.timeStart), time_converter.convertTo12Hr(slot.timeEnd)
				else:
					timeStart, timeEnd = time_converter.convertTo24Hr(slot.timeStart), time_converter.convertTo24Hr(slot.timeEnd)
				print(timetable_converter.slotTypeAsString(slot.slotType)  + "\n"
					+ "Time Start: " + timeStart + "\n"
					+ "Time End: " + timeEnd + "\n"
					+ "Room: " + slot.room + "\n"
					+ smallDashes)
	if (not isAnyClasses):
		print("There are no classes scheduled for " + date_converter.dayAsString(dayInt) + ".")

def printTimes(timetable, courseCodeStr):
	""" Prints all times this course is scheduled for.
	:param timetable: The timetable object to print out.
	:param courseCodeStr: The course code of the course to print times for.
	"""
	coursesList = []
	try:
		coursesList = timetable.coursesList
	except AttributeError as e:
		raise InvalidTimetableException("Timetable is invalid.")
	isCourseExist = False
	selectedCourse = None
	for course in coursesList:
		if (course.courseCode == courseCodeStr):
			isCourseExist = True
			selectedCourse = course
	if (not isCourseExist):
		print("Course " + courseCodeStr + " was not found.")
		return
	isAnyTimes = False
	for slot in selectedCourse.courseSlots:
		if (not isAnyTimes):
			print(course.courseCode + "\n"
				+ course.teacher + "\n"
				+ course.description + "\n"
				+ smallDashes)
			isAnyTimes = True
		timeStart, timeEnd = "", ""
		if (timetable_config.use12HrFormat):
			timeStart, timeEnd = time_converter.convertTo12Hr(slot.timeStart), time_converter.convertTo12Hr(slot.timeEnd)
		else:
			timeStart, timeEnd = time_converter.convertTo24Hr(slot.timeStart), time_converter.convertTo24Hr(slot.timeEnd)
		print(timetable_converter.slotTypeAsString(slot.slotType)  + "\n"
			+ "Day: " + date_converter.dayAsString(slot.day) + "\n"
			+ "Time Start: " + timeStart + "\n"
			+ "Time End: " + timeEnd + "\n"
			+ "Room: " + slot.room + "\n"
			+ smallDashes)
	if (not isAnyTimes):
		print("No times for " + courseCodeStr + ".")
