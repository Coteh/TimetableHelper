timetable
=========

A console app written in Python 3 that displays school timetable information.

School timetables are stored as JSON and parsed using [the Python Standard Library's JSON decoder](https://docs.python.org/3/library/json.html).

Features
---------
- View general information about timetable (start date, end date, list of all courses with time slot count)
- View all time slots for specified class
- View all classes scheduled for a particular day
- Option to view times in either 12hr format (AM/PM) or 24hr format

Issues
---------
- Nothing yet, but report an issue in Issues if you come across anything

Future Additions
---------
- Exam mode: View exams only. (and hide exams from normal timetable view)
- View amount of exams in timetable info
- Write documentation
- Add unit tests
- Render timetable to HTML
- Add/remove courses and slots to/from a timetable from within the console app
  - Export modified timetable to JSON, overwriting the previous version
- Import/Export from/to iCalendar format

Name History
---------
TimetableHelper: September 2014 - September 2015

timetable: September 2015 - present
