class Pizza:
  def __init__(self):
    # Establish the properties of each pizza
    # with a default value
    self.size = 12
    self.style = ""
    self.toppings = []
    
  def add_topping(self, topping):
    self.toppings.append(topping)
    
  def print_order(self):
    toppings = ", ".join(self.toppings)
    print(f'I would like a {self.size}-inch, {self.style} pizza with {toppings}.')

meat_lovers = Pizza()
meat_lovers.size = 6
meat_lovers.style = "Thin crust"
meat_lovers.add_topping("bell peppers")
meat_lovers.add_topping("tomatoes")
meat_lovers.print_order()
