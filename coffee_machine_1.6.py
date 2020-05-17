class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    # def user_input(self, u_input):
    #     self.u_input = u_input

    def menu_options(self, option):
        # machine_details()

        if option == "buy":
            self.buy_option()
        if option == "fill":
            self.fill_option()
        if option == "take":
            self.take_option()
        if option == "remaining":
            self.remaining_option()

    def buy_option(self):
        # global answer
        buy_list = [1, 2, 3, "back"]
        buy_answer = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        # print(type(buy_answer))
        if buy_answer == buy_list[3]:
            pass
        elif int(buy_answer) == buy_list[0]:
            self.calculate_machine_contents(1)
        elif int(buy_answer) == buy_list[1]:
            self.calculate_machine_contents(2)
        elif int(buy_answer) == buy_list[2]:
            self.calculate_machine_contents(3)

    def fill_option(self):
        # global water, milk, coffee, cups, money
        fill_water = int(input("Write how many ml of water do you want to add:"))
        self.water = self.water + fill_water
        fill_milk = int(input("Write how many ml of milk do you want to add:"))
        self.milk = self.milk + fill_milk
        fill_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
        self.coffee = self.coffee + fill_coffee
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups = self.cups + fill_cups
        # return machine_details(water, milk, coffee, cups, money)

    def take_option(self):
        # global water, milk, coffee, cups, money
        print("I gave you " + str(self.money))
        self.money = self.money * 0
        # return machine_details(water, milk, coffee, cups, money)

    def calculate_machine_contents(self, cal_answer):
        # print(cal_answer)
        # global water, milk, coffee, cups, money
        if cal_answer == 1:
            if self.water < 250 or self.coffee < 16 or self.cups < 1:
                self.check_contents(cal_answer)
            elif self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 250
                self.coffee = self.coffee - 16
                self.cups = self.cups - 1
                self.money = self.money + 4

        if cal_answer == 2:
            if self.water < 350 or self.milk < 75 or self.coffee < 20 or self.cups < 1:
                self.check_contents(cal_answer)
            elif self.water >= 350 and self.milk >= 75 and self.cups >= 1 and self.coffee >= 20:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee = self.coffee - 20
                self.cups = self.cups - 1
                self.money = self.money + 7

        if cal_answer == 3:
            if self.water < 200 or self.milk < 100 or self.coffee < 12 or self.cups < 1:
                self.check_contents(cal_answer)
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.coffee = self.coffee - 12
                self.cups = self.cups - 1
                self.money = self.money + 6

    def check_contents(self, option):
        # global water, milk, coffee, cups, money
        if option == 1:
            min_water = 250
            min_coffee = 16
            min_cup = 1
            if self.water < min_water:
                print("Sorry, not enough water!")

            if self.coffee <= min_coffee:
                print("Sorry, not enough coffee beans!")
                # coffee = 0
            if self.cups <= min_cup:
                print("Sorry, not enough cups!")

        if option == 2:
            min_water = 350
            min_milk = 75
            min_coffee = 20
            min_cup = 1
            if self.water < min_water:
                print("Sorry, not enough water!")

            if self.milk < min_milk:
                print("Sorry, not enough milk!")

            if self.coffee <= min_coffee:
                print("Sorry, not enough coffee beans!")

            if self.cups <= min_cup:
                print("Sorry, not enough cups!")

        if option == 3:
            min_water = 200
            min_milk = 100
            min_coffee = 12
            min_cup = 1
            if self.water < min_water:
                print("Sorry, not enough water!")

            if self.milk < min_milk:
                print("Sorry, not enough milk!")

            if self.coffee <= min_coffee:
                print("Sorry, not enough coffee beans!")

            if self.cups <= min_cup:
                print("Sorry, not enough cups!")

    def remaining_option(self):
        # self.machine_details(self.water, self.milk, self.coffee, self.cups, self.money)
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    # def machine_details(self, water, milk, coffee, cups, money):


on = True
ccd = CoffeeMachine()
while on:
    # machine_details(water, milk, coffee, cups, money)
    answer = input("Write action (buy, fill, take, remaining, exit):")
    if answer == "exit":
        break
    ccd.menu_options(answer)
