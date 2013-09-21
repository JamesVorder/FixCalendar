#! /usr/bin/env python
print "Enter the path to the .ics file"
file = input()
file = open(file, "rt")
print "Enter the Course ID and Course Number (i.e. THEO 111) (The caps matter)"
course = input()
print "Enter the desired start time in 24 hour format like this: '152300', meaning 3:23 PM"
time = input()
print "Enter the desired end time in the same format"
endTime = input()
calendarString = file.read()
file.close()
#make the strings into a list so that it can be worked with
calendarList = []
for x in range(0, len(calendarString) - 1):
	calendarList.append(calendarString[x])
timeList = []
for x in range(0, len(time)):
	timeList.append(time[x])
endTimeList = []
for x in range(0, len(endTime)):
	endTimeList.append(endTime[x])
#go through the whole file, and find each instance of the class in question
#after the class and time are found, the current time is replaced with the desired time
endLocation = 0
while calendarString.find(course, endLocation) != -1:
	classLocation = calendarString.find(course, endLocation)
	startDateLocation = calendarString.find("DTSTART:", classLocation)
	startTimeLocation = calendarString.find("T", startDateLocation + 7) + 1
	for i in range(startTimeLocation, startTimeLocation + 5):
		calendarList[i] = timeList[i - startTimeLocation]
		endLocation = i
	endDateLocation = calendarString.find("DTEND:", endLocation)
	endTimeLocation = calendarString.find("T", endDateLocation) + 1
	for i in range(endTimeLocation, endTimeLocation + 5):
		calendarList[i] = endTimeList[i - endTimeLocation]
		endLocation = i

#write the changes you've made to the list to a string, then to a file
outFile = "fixed-schedule.ics"
outFile = open(outFile, "wt")
newCalendarString = " "
for y in range(0, len(calendarString) - 1):
	newCalendarString = newCalendarString + calendarList[y]
outFile.write(newCalendarString)
outFile.close()

print "complete"
