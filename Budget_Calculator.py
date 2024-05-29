#Read Me
#This appliation creates a budget calculator. See body of examples of inputs

import math
#This class defines a new category to go on the budget. It requires one input, name, that is what you want to call this item. EX: Rent
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.withs = 0
        self.budget = 0

    def __str__(self):
        ans = self.name.center(30, '*') + '\n'
        for i in self.ledger:
            ans += str(i["description"][:23])
            this = str(i["amount"])
            this = float(this)
            this = "{:.2f}".format(this)
            ans += this.rjust(30 - len(str(i["description"][:23])))
            ans += '\n'
        ans += 'Total: ' + str(self.budget)
        return ans

    def deposit(self, amount, desc=None):
        if desc == None:
            desc = ""
        self.budget += amount
        i = {"amount": float(amount), "description": desc}
        self.ledger.append(i)

    def withdraw(self, amount, desc=None):
        if self.budget >= amount:
            if desc == None:
                desc = ""
            self.withs += amount
            amount *= -1
            i = {"amount": amount, "description": desc}
            self.ledger.append(i)
            self.budget += float(amount)
            return True
        else:
            return False

    def get_balance(self):
        return self.budget

    def transfer(self, amount, otherbudj):
        if self.get_balance() >= amount:
            cat = 'Transfer to ' + otherbudj.name
            self.withdraw((amount), 'Transfer to ' + otherbudj.name)
            otherbudj.deposit((amount), 'Transfer from ' + self.name)
            return True

        return False

    def check_funds(self, amount):
        if amount > self.budget:
            return False
        return True

#Ths function shows how the budget breaks down for the inputs provided.
def create_spend_chart(categories):
    categories_list = []
    percentages = []

    Budget_Output = 'Percentage spent by category\n'
    for i in categories:
        categories_list .append(i.name)
        percentages.append(i.withs)

    total_spent = sum(percentages)
    count = 0

    for i in percentages:
        percent_of_budget = percentages[count] / total_spent * 10
        percent_of_budget = math.floor(percent_of_budget) * 10
        percentages[count] = percent_of_budget
        count += 1

    tens = 100

    while tens >= 0:
        Budget_Output += str(tens).rjust(3) + '|'
        for i in percentages:
            if i >= tens:
                Budget_Output += ' o '
            else:
                Budget_Output += '   '
        tens -= 10
        Budget_Output += ' \n'

    total_budget = len(percentages) * 3 + 1

    Budget_Output += '    '

    for i in range(0, total_budget):
        Budget_Output += '-'

    Budget_Output += '\n'
    column = (len(max(categories_list , key=len)))
    rows = [names.ljust(column) for names in categories_list ]

    # learned about ZIP function from @python learning on youtube
    # see source here:https://www.youtube.com/watch?v=azSwlBK2hqo
    for name in zip(*rows):
        Budget_Output += '     ' + ('  '.join(name)) + '  \n'

    Budget_Output = Budget_Output.rstrip('\n')
    return Budget_Output


if __name__ == '__main__':
    #sample objects
    Food = Category("Food")
    Clothing = Category("Clothing")
    Rent = Category("Rent")

    #sample transactions
    Food.deposit(100, "deposit")
    Food.withdraw(60, "Spent money at Walmart")
    Food.transfer(40,Clothing)
    Clothing.deposit(100, 'Money from Grandma for clothes')
    Rent.deposit(100)
    Rent.withdraw(10, 'Extra Utility Bill')
    Clothing.withdraw(20, 'Dress for work')

    #see the budget
    print(create_spend_chart([Food, Clothing, Rent]))
