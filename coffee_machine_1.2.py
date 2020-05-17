print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

# input
water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
no_of_coffee = int(input("Write how many cups of coffee you will need:"))

# total_ingredients_required = (water * no_of_coffee) + (milk * no_of_coffee) + (coffee * no_of_coffee)
# total_ingredients_of_machine = water + milk + coffee

# total_water_required = water - (water * no_of_coffee)
# total_milk_required = milk - (milk * no_of_coffee)
# total_coffee_required = coffee - (milk * no_of_coffee)

total_water_machine = water // 200
total_milk_machine = milk // 50
total_coffee_machine = coffee // 15
no_of_cups_machine = 0
print(total_water_machine)
print(total_milk_machine)
print(total_coffee_machine)
if (total_water_machine <= total_milk_machine) and (total_water_machine <= total_coffee_machine):
    no_of_cups_machine = total_water_machine
    print("no_of_cups_machine" + str(no_of_cups_machine))
elif (total_milk_machine <= total_water_machine) and (total_milk_machine <= total_coffee_machine):
    no_of_cups_machine = total_milk_machine
    print("no_of_cups_machine" + str(no_of_cups_machine))
else:
    no_of_cups_machine = total_coffee_machine
    print("no_of_cups_machine" + str(no_of_cups_machine))
print(no_of_cups_machine)
extra_cups = no_of_cups_machine - no_of_coffee
# print(extra_cups)
# if (total_water_required and total_milk_required and total_coffee_required) >= 0 and extra_cups == 0:
#     print("Yes, I can make that amount of coffee")
# elif (total_water_required and total_milk_required and total_coffee_required) >= 0 and extra_cups >= 0:
#     print("Yes, I can make that amount of coffee (and even " + str(extra_cups) + " more than that)")
# else:
#     print("No, I can make only " + str(no_of_cups_machine) + " cups of coffee")
if no_of_cups_machine == no_of_coffee:
    print("Yes, I can make that amount of coffee")
elif no_of_cups_machine >= no_of_coffee and extra_cups > 0:
    print("Yes, I can make that amount of coffee (and even " + str(extra_cups) + " more than that)")
else:
    print("No, I can make only " + str(no_of_cups_machine) + " cups of coffee")

