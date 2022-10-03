class Beverage:
    prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
              "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
              "Pineapple": 3.5}

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        cost_prices = 0
        for i in self.ingredients:
            for j in Beverage.prices:
                if i == j:
                    cost_prices += Beverage.prices[i]
        str(cost_prices)
        return "$"+"{0:4.2f}".format(cost_prices)

    def get_price(self):
        full_price = 0
        for i in self.ingredients:
            for j in Beverage.prices:
                if i == j:
                    full_price += Beverage.prices[i]
        full_price *= 2.5
        str(full_price)
        return "$"+"{0:4.2f}".format(full_price)

    def get_name(self):
        self.ingredients.sort()
        new_ingredients = []
        for i in self.ingredients:
            a = i.replace('ies', 'y')
            new_ingredients.append(a)
        if len(self.ingredients) == 1:
            a = self.ingredients[0].replace('ies', 'y')
            new_ingredients.append(a)
            return new_ingredients[0] + ' Smoothie'
        elif len(self.ingredients) > 1:
            for i in self.ingredients:
                str_a = ' '.join(new_ingredients)
        return str_a + " Fusion"


s1 = Beverage(["Banana"])
s1.ingredients
s1.get_cost()
s1.get_price()
s1.get_name()
s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
s2.ingredients
s2.get_cost()
s2.get_price()
s2.get_name()

