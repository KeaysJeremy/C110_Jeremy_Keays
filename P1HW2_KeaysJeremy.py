print("This program calculates and displays travel expenses")
budget = int(input("Budget:"))
fuel_cost = int(input("Fuel:"))
travel_destination = (input("Destination:"))
hotel_cost = int(input("Hotel:"))
food_cost = int(input("Food:"))
remaining_balance = print(budget - fuel_cost - hotel_cost - food_cost)
print("\n")

print("Travel expenses", "\n")

print("Destination:", travel_destination)
print("Initial Budget:", budget, "\n")

print("Your approximate fuel cost:", fuel_cost)
print("Your approximate hotel cost:", hotel_cost) 
print("Your approximate food cost:", food_cost)
print("\n")

print(remaining_balance)







