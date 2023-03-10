cars = 100
space_in_cars = 4.0
drivers = 30
passengers = 90
cars_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_cars
average_passengers_per_car = passengers / cars_driven

print("There are" , cars , "cars available.")
print("There are" , drivers , "drivers available.")
print("There is", cars_not_driven, "empty cars today")
print(passengers, "passengers")
print(average_passengers_per_car,"passengers in car")