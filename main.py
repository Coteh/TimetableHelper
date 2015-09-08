# Timetable Helper
# By James Cote
# Load in a timetable file and find out the classes and times within it

''' Imports '''
from os import listdir, getcwd
from os.path import isfile, join
from argparse import ArgumentParser, RawTextHelpFormatter

from src import timetable_config, timetable_json, date_converter, timetable_exceptions
from src.timetable_printer import printClasses, printTimes, printInfo

''' Global Variables '''
# Filepath to the schedules
SCHEDULE_PATH = getcwd() + "/schedules/"
TIMETABLE_EXTENSION = ".json"
# Timetable data
currTimetableData = None

def loadTimetable(_fileName):
	""" Loads in a new timetable.
	:param _fileName: Filename of the timetable to load.
	"""
	# Open text file that was passed in and populate data
	data = ""
	with open(SCHEDULE_PATH + _fileName + TIMETABLE_EXTENSION) as fp:
		for line in fp.readlines():
			data += ''.join(line.split('\n'))
	# Parse the JSON buffer and save it as the current timetable list
	global currTimetableData
	currTimetableData = timetable_json.readTimetableJSON(data)

def changeCurrTimetable(_timetableName):
	""" Changes the current timetable.
	:param _timetableName: Name of the timetable file to change to.
	"""
	timetable_config.currentTimetable = _timetableName
	timetable_config.saveConfig()
	print("Timetable has been changed!\n")

def processCommand(_fmtCmd):
	if (_fmtCmd.subCommand == "info"):
		try:
			loadTimetable(timetable_config.currentTimetable)
		except timetable_exceptions.TimetableParseError as e:
			print("ERROR: Timetable was not parsed properly. Check the timetable file, then try again.")
			return
		try:
			printInfo(currTimetableData)
		except timetable_exceptions.InvalidTimetableException as e:
			print("ERROR: Timetable data is invalid. Exiting...")
			return
	elif (_fmtCmd.subCommand == "times"):
		try:
			loadTimetable(timetable_config.currentTimetable)
		except timetable_exceptions.TimetableParseError as e:
			print("ERROR: Timetable was not parsed properly. Check the timetable file, then try again.")
			return
		classStr = _fmtCmd.course_code
		try:
			printTimes(currTimetableData, classStr)
		except timetable_exceptions.InvalidTimetableException as e:
			print("ERROR: Timetable data is invalid. Exiting...")
			return
	elif (_fmtCmd.subCommand == "classes"):
		try:
			loadTimetable(timetable_config.currentTimetable)
		except timetable_exceptions.TimetableParseError as e:
			print("ERROR: Timetable was not parsed properly. Check the timetable file, then try again.")
			return
		day = date_converter.dayAsNum(_fmtCmd.day)
		try:
			printClasses(currTimetableData, day)
		except timetable_exceptions.InvalidTimetableException as e:
			print("ERROR: Timetable data is invalid. Exiting...")
			return
	elif (_fmtCmd.subCommand == "config"):
		if (_fmtCmd.configCommand == "change_timetable"):
			changeCurrTimetable(_fmtCmd.timetable_name)

def main():
	# Setup command parsing
	parser = ArgumentParser(prog="timetable", description="Displays timetable information.", formatter_class=RawTextHelpFormatter)
	subparsers = parser.add_subparsers(dest='subCommand', help="Timetable commands.")
	parserInfo = subparsers.add_parser('info', help="Display info about timetable.")
	parserTime = subparsers.add_parser('times', help="Display the times for a specified class.")
	parserTime.add_argument('course_code', help='Displays times for a particular class.' + "Any course code in timetable as argument.")
	parserClasses = subparsers.add_parser('classes', help="Display the time slots for a particular day.")
	parserClasses.add_argument('day', help='Displays classes for a particular day.' + " (" + ", ".join(timeStr for timeStr in date_converter.timesDic) + ")")
	parserConfig = subparsers.add_parser('config', help="Edit config options.")
	configSubParsers = parserConfig.add_subparsers(dest='configCommand', help="Config commands.")
	parserChangeTimetable = configSubParsers.add_parser('change_timetable', help="Change the timetable currently read by the program.")
	parserChangeTimetable.add_argument('timetable_name', help='Name of timetable file to change to.')
	# Check to see if user entered any command line arguments
	args = parser.parse_args()
	# process commands that have been entered as arguments
	processCommand(args)

if __name__ == '__main__':
	main()
