class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name}".center(30, "*")

        lines = [title]
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            line = f"{description:<23}{amount:>7}"
            lines.append(line)
        
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)
        
        return "\n".join(lines)

def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        total_withdrawn = 0
        for item in category.ledger:
            if item["amount"] < 0:  
                total_withdrawn += abs(item["amount"])
        withdrawals.append(total_withdrawn)
    
    total_spent = sum(withdrawals)
    
    percentages = []
    for withdrawal in withdrawals:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = (withdrawal / total_spent) * 100
        
        rounded_percentage = int(percentage // 10) * 10
        percentages.append(rounded_percentage)
    
    chart_lines = []
    
    chart_lines.append("Percentage spent by category")
    
    for i in range(100, -10, -10):
        line = f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        chart_lines.append(line.rstrip()) 
    
    horizontal_line = "    " + "-" * (len(categories) * 3 + 1)
    chart_lines.append(horizontal_line)
    
    max_name_length = max(len(category.name) for category in categories) if categories else 0
    
    for i in range(max_name_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        chart_lines.append(line.rstrip())  
    
    return "\n".join(chart_lines)



if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")
    
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more foo")
    food.transfer(50, clothing)
    
    clothing.withdraw(25.55, "shirt")
    clothing.withdraw(100, "pants")
    
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "gas")
    
    print(food)
    print()
    print(clothing)
    print()
    print(auto)
    print()
    
    print(create_spend_chart([food, clothing, auto]))

