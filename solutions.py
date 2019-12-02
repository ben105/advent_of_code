from day1.calculate_fuel import *

############
## DAY 1  ##

input_file = 'day1/day1.txt'

day1_part1 = calculate_fuel_from_filepath(input_file)
print('[Day 1, part 1] {}'.format(day1_part1))

# Include fuel as additional mass.
day1_part2 = calculate_fuel_from_filepath(input_file, True)
print('[Day 1, part 2] {}'.format(day1_part2))

############
############
