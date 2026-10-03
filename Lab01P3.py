#
# Naomi Muchiri
# 08/23/2026
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Get the number of miles.

miles = int(input('Enter the number of miles: '))

# Get the speed in MPH.
speed = int(input('Enter the speed in MPH: '))
# Calculate the travel time.
travel_time = miles/speed

# Display the travel time (formatted to 2 decimal places).
print(f"You should cover that distance in: {travel_time:.2f} hours")
