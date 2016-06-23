cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
empty_cars_no = cars - drivers
people_can_transport_today = drivers * space_in_car
average_passengers_per_car = passengers / drivers

print "there are", cars, "available."
print "There are only", drivers, "drivers avaialable."
print "There will be", empty_cars_no, "empty cars today."
print "We can transport", people_can_transport_today, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "people in each car."
