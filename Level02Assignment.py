#Defining the base variables
user_name = str (input("What is your name? "))
destination = str (input("What is your destination? "))
distance = float (input("What is the one-way distance in miles? "))
mpg = float (input("How many miles per gallon of gas does your vehicle get? "))
gas_price = float (input("How much does a gallon of gas cost? "))
number_of_travelers = int (input("How many people are traveling with you? "))

#Calculating and defining additional variables
round_trip_miles = float (distance*2)
gallons_of_gas_needed = float (round_trip_miles/mpg)
cost_of_gas = float(gallons_of_gas_needed*gas_price)
cost_per_traveler = float(cost_of_gas/number_of_travelers)

#Printing results
print(f"{user_name}'s awesome adventure to {destination}!".upper())
print(f"The total cost of gas for the trip will be ${cost_of_gas}!")
print(f"Each person will pay ${cost_per_traveler} for gas!")
print("Don't forget to bring snacks!")