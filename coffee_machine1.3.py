water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def menu_options(option):
    # machine_details()

    if option == "buy":
        buy_option()
    if option == "fill":
        fill_option()
    if option == "take":
        take_option()


def machine_details(machine_water, machine_milk, machine_coffee, machine_cups, machine_money):
    print("The coffee machine has:")
    print(str(machine_water) + " of water")
    print(str(machine_milk) + " of milk")
    print(str(machine_coffee) + " of coffee beans")
    print(str(machine_cups) + " of disposable cups")
    print(str(machine_money) + " of money")


def buy_option():
    buy_answer = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))

    if buy_answer == 1:
        calculate_machine_contents(buy_answer)
    if buy_answer == 2:
        calculate_machine_contents(buy_answer)
    if buy_answer == 3:
        calculate_machine_contents(buy_answer)
    pass


def fill_option():
    global water, milk, coffee, cups, money
    fill_water = int(input("Write how many ml of water do you want to add:"))
    water = water + fill_water
    fill_milk = int(input("Write how many ml of milk do you want to add:"))
    milk = milk + fill_milk
    fill_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
    coffee = coffee + fill_coffee
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    cups = cups + fill_cups
    return machine_details(water, milk, coffee, cups, money)


def take_option():
    global water, milk, coffee, cups, money
    print("I gave you " + str(money))
    money = money * 0
    return machine_details(water, milk, coffee, cups, money)


def calculate_machine_contents(cal_answer):
    global water, milk, coffee, cups, money
    if cal_answer == 1:
        water = water - 250
        coffee = coffee - 16
        cups = cups - 1
        money = money + 4
        return machine_details(water, milk, coffee, cups, money)

    if cal_answer == 2:
        water = water - 350
        milk = milk - 75
        coffee = coffee - 20
        cups = cups - 1
        money = money + 7
        return machine_details(water, milk, coffee, cups, money)

    if cal_answer == 3:
        water = water - 200
        milk = milk - 100
        coffee = coffee - 12
        cups = cups - 1
        money = money + 6
        return machine_details(water, milk, coffee, cups, money)


machine_details(water, milk, coffee, cups, money)


answer = input("Write action (buy, fill, take):")


menu_options(answer)
