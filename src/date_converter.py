from datetime import date
from src.timetable_exceptions import InvalidCalendarDateException

# List of days of the week
dayOfWeekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daysInAWeek = len(dayOfWeekList)
# Grabs the current day of the week from datetime
todayNum = date.today().weekday()
# Extrapolate the previous day and the next day from today's value
tomorrowNum = (todayNum + 1) % daysInAWeek
yesterdayNum = (todayNum - 1) % daysInAWeek
# Times dictionary that will hold the string forms of all the day commands as key
# and the day int as value
timesDic = {
	"today" : todayNum,
	"tomorrow" : tomorrowNum,
	"yesterday" : yesterdayNum,
}
# Appending days of the week to the times dictionary
for i in range(len(dayOfWeekList)):
	timesDic[dayOfWeekList[i].lower()] = i

def dayAsString(_dayInt):
	_dayInt = _dayInt % daysInAWeek
	dayStr = dayOfWeekList[_dayInt]
	if (_dayInt == todayNum):
		dayStr += " (today)"
	elif (_dayInt == yesterdayNum):
		dayStr += " (yesterday)"
	elif (_dayInt == tomorrowNum):
		dayStr += " (tomorrow)"
	return dayStr

def dayAsNum(_dayString):
	return timesDic[_dayString.lower()] % len(dayOfWeekList)

def calendarDateAsString(calVal):
	# throw an error if the string isn't big enough to represent a calendar date
	if (len(calVal) != 8): raise InvalidCalendarDateException("Not a valid calendar date value.")
	# format string for the datetime conversion
	calVal = calVal[:-4] + "/" + calVal[-4:-2]+ "/" + calVal[-2:]
	# convert to a date using datetime
	calDate = datetime.strptime(calVal, "%Y/%m/%d")
	# return formatted calendar date string
	return calDate.strftime("%b %d, %Y")
