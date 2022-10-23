import sys  # importing sys module

# adding sys.path to locations which will returns list of paths
locations = sys.path

# printing list of locations of python files
print(locations)
print()

# printing location in much clear way to see
for i in locations:
    print(i)

import calendar  # importing calendar module

# using method leapdays() of calendar module
leapdays = calendar.leapdays(2000, 2030)

# printing leap days
print(leapdays)

# isleap() returns bool, will check is the given year is leapyear or not
print(calendar.isleap(2016))
