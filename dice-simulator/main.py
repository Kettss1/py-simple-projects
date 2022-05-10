import random


class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = "Would you like to throw the dice? [y/n]"

    def initialize(self):
        response = input(self.message)
        if response == "y":
            self.GetDiceValue()
        elif response == 'n':
            print("Sorry T-T")
        else:
            print("Your response did not match what we expected. Please, try again")

    def getDiceValue(self):
        print("------------------------------------")
        print("Value:")
        print(random.randint(self.min_value, self.max_value))


DiceSimulator.Initialize()
