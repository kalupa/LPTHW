cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
# a car must have a driver to be driven
cars_driven = drivers
# capacity is total cars that have drivers and space and the amount of space per car
carpool_capacity = cars_driven * space_in_a_car

# total passengers by total cars with space and driver
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can tranport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Extra credit
# the error was the additional "_" in "carpool" - he typed "car_pool" instead.
# 1. use 4.0 to cause floating point math for better division accuracy.
