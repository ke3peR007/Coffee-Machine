water = 400
milk = 540
coffee = 120
cups = 9
money = 550
answer = ""


def menu_options(option):
    # machine_details()

    if option == "buy":
        buy_option()
    if option == "fill":
        fill_option()
    if option == "take":
        take_option()
    if option == "remaining":
        remaining_option()


def machine_details(machine_water, machine_milk, machine_coffee, machine_cups, machine_money):
    print("The coffee machine has:")
    print(str(machine_water) + " of water")
    print(str(machine_milk) + " of milk")
    print(str(machine_coffee) + " of coffee beans")
    print(str(machine_cups) + " of disposable cups")
    print("$" + str(machine_money) + " of money")


def buy_option():
    # global answer
    buy_answer = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
    print(buy_answer)
    if buy_answer == 1:
        calculate_machine_contents(buy_answer)
    if buy_answer == 2:
        calculate_machine_contents(buy_answer)
    if buy_answer == 3:
        calculate_machine_contents(buy_answer)
    # if buy_answer != 1 and buy_answer != 2 or buy_answer != 3:
    #     # answer = input("Write action (buy, fill, take, remaining, exit):")
    if str(buy_answer) == "back":
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
    # return machine_details(water, milk, coffee, cups, money)


def take_option():
    global water, milk, coffee, cups, money
    print("I gave you " + str(money))
    money = money * 0
    # return machine_details(water, milk, coffee, cups, money)


def remaining_option():
    machine_details(water, milk, coffee, cups, money)


def calculate_machine_contents(cal_answer):
    global water, milk, coffee, cups, money
    if cal_answer == 1:
        if water < 250 or coffee < 16 or cups < 1:
            check_contents(cal_answer)
        elif water >= 250 and coffee >= 16 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            water = water - 250
            coffee = coffee - 16
            cups = cups - 1
            money = money + 4
        # if (water or milk or coffee or cups) <= 0:
        #     check_contents(cal_answer)
        # else:
        #     print("I have enough resources, making you a coffee!")

    if cal_answer == 2:
        if water < 350 or milk < 75 or coffee < 20 or cups < 1:
            check_contents(cal_answer)
        elif water >= 350 and milk >= 75 and cups >= 1 and coffee >= 20:
            print("I have enough resources, making you a coffee!")
            water = water - 350
            milk = milk - 75
            coffee = coffee - 20
            cups = cups - 1
            money = money + 7
        # if (water or milk or coffee or cups) <= 0:
        #     check_contents(cal_answer)
        # else:
        #     print("I have enough resources, making you a coffee!")

    if cal_answer == 3:
        if water < 200 or milk < 100 or coffee < 12 or cups < 1:
            check_contents(cal_answer)
        else:
            print("I have enough resources, making you a coffee!")
            water = water - 200
            milk = milk - 100
            coffee = coffee - 12
            cups = cups - 1
            money = money + 6
        # if (water or milk or coffee or cups) <= 0:
        #     check_contents(cal_answer)
        # else:
        #     print("I have enough resources, making you a coffee!")


def check_contents(option):
    global water, milk, coffee, cups, money
    if option == 1:
        min_water = 250
        min_coffee = 16
        min_cup = 1
        if water < min_water:
            print("Sorry, not enough water!")

        if coffee <= min_coffee:
            print("Sorry, not enough coffee beans!")
            # coffee = 0
        if cups <= min_cup:
            print("Sorry, not enough cups!")
            # cups = 0
    if option == 2:
        min_water = 350
        min_milk = 75
        min_coffee = 20
        min_cup = 1
        if water < min_water:
            print("Sorry, not enough water!")

        if milk < min_milk:
            print("Sorry, not enough milk!")

        if coffee <= min_coffee:
            print("Sorry, not enough coffee beans!")

        if cups <= min_cup:
            print("Sorry, not enough cups!")
            # cups = 0
        if option == 3:
            min_water = 200
            min_milk = 100
            min_coffee = 12
            min_cup = 1
            if water < min_water:
                print("Sorry, not enough water!")

            if milk < min_milk:
                print("Sorry, not enough milk!")

            if coffee <= min_coffee:
                print("Sorry, not enough coffee beans!")

            if cups <= min_cup:
                print("Sorry, not enough cups!")
                # cups = 0
    # if water < min_water:
    #     print("Sorry, not enough water!")
    #
    # if milk <  min_milk:
    #     print("Sorry, not enough milk!")
    #
    # if coffee <= min_coffee:
    #     print("Sorry, not enough coffee beans!")
    #     coffee = 0
    # if cups <= min_cup:
    #     print("Sorry, not enough cups!")
    #     cups = 0


on = True
while on:
    # machine_details(water, milk, coffee, cups, money)
    answer = input("Write action (buy, fill, take, remaining, exit):")
    if answer == "exit":
        break
    menu_options(answer)
