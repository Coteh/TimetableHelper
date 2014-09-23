TimetableHelper
=========

A small python script that reads in specially formatted textfiles containing school timetable information (courses, times, and rooms),
which are then organized by the script and then displayed to the user.

The user types in the following commands to get information displayed to them:

times [today, tomorrow, yesterday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday] - displays the courses that are in session for that day with the corresponding room number for each time slot

classes [CRSE 100, ...] - displays all the timeslots of specified course

change_timetable [timetablename, ...] - swaps out one timetable for another that has been loaded in

exit - exits the console app