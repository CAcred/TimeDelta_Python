'''
Made by C. A. Acred 2016, 04 21
For his father

This code takes a 2D list where each sublist has two datetimes, subtracts the 0th from the 1st, replacing the list of datetimes with
One timedelta object with their difference. Then, it adds all the timedeltas and puts it into yet another timedelta.
'''

import random
import datetime


list = [""] * 10

# Simulating dates:
# Fill list with 10 lists of two dates:
i = 0
while i < 10:
	list[i] = [datetime.date(random.randrange(2000, 2016, 1), random.randrange(1, 12, 1), random.randrange(1, 30, 1)),     datetime.date(random.randrange(2000, 2016, 1), random.randrange(1, 12, 1), random.randrange(1, 30, 1))]
	i += 1;
	
# Test:
print "\n\nStarting Dates List: ", list, "\n\n"


# Subtract each list's items from each other, 1st - 0th:
i = 0
while i < len(list):
	list[i] = list[i][1] - list[i][0]
	list[i] = list[i].total_seconds()
	i += 1

# Test
print "Current List after Subtraction: ", list, "\n\n"

# Add the entire list to one integers
result_seconds = 0
for num in list:
	result_seconds += num

# Convert seconds to hours, minutes, seconds:

print "Total Seconds: ", result_seconds, "\n"

hours_ = result_seconds // (60*60)
result_seconds = result_seconds % (60*60) # Remove the seconds that fit into hours

minutes_ = result_seconds // 60
result_seconds = result_seconds % 60# Remove the seconds that fit into minutes

# Put the results into a timedelta:

result = datetime.timedelta(hours=hours_, minutes = minutes_, seconds = result_seconds)


# Result
print hours_, "\n", minutes_, "\n", result_seconds

print result