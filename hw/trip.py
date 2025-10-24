gas_cost = 3.16
mpg = 25
trip_length = 750
tank_volume = 19.5
gallons_needed = trip_length / mpg
total_cost = gallons_needed * gas_cost
tank_range = mpg * tank_volume
stops_needed = trip_length / tank_range
print("You need", gallons_needed, "gallons of gas.")
print("You will have to spend", total_cost, "dollars.")
print("On one tank of gas, you can go", tank_range, "miles")
print("You'll need to make (roughly)", stops_needed, "stops")