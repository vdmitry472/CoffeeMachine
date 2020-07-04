class CoffeeMachine:
    water = 0
    milk = 0
    beans = 0
    cups = 0
    money = 0
    status = None

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.status = "menu"

    def read_input(self, input_string):
        if (self.status == "menu") & (input_string == "buy"):
            self.buy_drink()
        elif (self.status == "menu") & (input_string == "remaining"):
            self.machine_state()
        elif (self.status == "menu") & (input_string == "take"):
            self.take_money()
        elif (self.status == "menu") & (input_string == "fill"):
            add_water = int(input("Write how many ml of water do you want to add:"))
            add_milk = int(input("Write how many ml of milk do you want to add:"))
            add_beans = int(input("Write how many grams of coffee beans do you want to add:"))
            add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
            self.water += add_water
            self.milk += add_milk
            self.beans += add_beans
            self.cups += add_cups
        elif (self.status == "buy") & (input_string == "back"):
            self.status = "menu"
        elif (self.status == "buy") & (input_string in ["1", "2", "3"]):
            self.choosing_a_drink(input_string)

    def buy_drink(self):
        self.status = "buy"
        command = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.read_input(command)

    def choosing_a_drink(self, number_of_drink):
        if number_of_drink == "1":
            if (self.water >= 250) & (self.beans >= 16) & (self.cups > 0):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                print("I don't have enough resources. Please refill the storage!")
        elif number_of_drink == "2":
            if (self.water >= 350) & (self.milk >= 75) & (self.beans >= 12) & (self.cups > 0):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                print("I don't have enough resources. Please refill the storage!")
        elif number_of_drink == "3":
            if (self.water >= 200) & (self.milk >= 100) & (self.beans >= 12) & (self.cups > 0):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                print("I don't have enough resources. Please refill the storage")
        self.status = "menu"

    def machine_state(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")

    def take_money(self):
        print("I gave you $" + str(self.money))
        self.money = 0

machine = CoffeeMachine(400, 540, 120, 9, 550)
x = 2
while x > 0:
    command = input("Write action (buy, fill, take, remaining, exit):")
    if command == "exit":
        break
    else:
        machine.read_input(command)