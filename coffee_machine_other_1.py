
class CoffeeMachine:

    def __init__(self, money, water, milk, coffee_beans, disposable_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups

    def display_status(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'${self.money} of money')
        print()

    def get_action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        return input()

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu')

        coffee_type = str(input())
        if coffee_type.lower() == 'back':
            return
        else:
            coffee_type = int(coffee_type)

        if coffee_type == 1:
            self.make_espresso()
        elif coffee_type == 2:
            self.make_latte()
        elif coffee_type == 3:
            self.make_cappuccino()
        else:
            print('Command not recognized')
            buy()

    def make_espresso(self):

        if self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.disposable_cups -= 1
            self.money += 4
            print('I have enough resources, making you a coffee!\n')
        else:
            if self.water - 250 < 0:
                print('Sorry, not enough water!\n')
            elif self.coffee_beans - 16 < 0:
                print('Sorry, not enough coffee beans\n')
            elif self.disposable_cups - 1 < 0:
                print('Sorry, not enough disposable cups\n')

    def make_latte(self):
        if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.disposable_cups -= 1
            self.money += 7
            print('I have enough resources, making you a coffee!\n')
        else:
            if self.water - 350 < 0:
                print('Sorry, not enough water!\n')
            elif self.coffee_beans - 20 < 0:
                print('Sorry, not enough coffee beans\n')
            elif self.milk - 75 < 0:
                print('Sorry, not enough milk')
            elif self.disposable_cups - 1 < 0:
                print('Sorry, not enough disposable cups\n')


    def make_cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.disposable_cups -= 1
            self.money += 6
            print('I have enough resources, making you a coffee!\n')
        else:
            if self.water - 200 < 0:
                print('Sorry, not enough water!\n')
            elif self.coffee_beans - 12 < 0:
                print('Sorry, not enough coffee beans\n')
            elif self.milk - 100 < 0:
                print('Sorry, not enough milk\n')
            elif self.disposable_cups - 1 < 0:
                print('Sorry, not enough disposable cups\n')

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water_add = int(input())
        print('Write how many ml of milk do you want to add:')
        milk_add = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        coffee_beans_add = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        disposable_cups_add = int(input())

        self.water += water_add
        self.milk += milk_add
        self.coffee_beans += coffee_beans_add
        self.disposable_cups += disposable_cups_add

    def take(self):
        print(f'I gave you ${self.money}')
        print()
        self.money = 0

    def run(self):
        while True:
            action = self.get_action()
            if action.lower() == 'buy':
                self.buy()
            elif action.lower() == 'fill':
                self.fill()
            elif action.lower() == 'take':
                self.take()
            elif action.lower() == 'remaining':
                print()
                self.display_status()
            elif action.lower() == 'exit':
                break
            else:
                print('command not recognized')
                run()


coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)

coffee_machine.run()

