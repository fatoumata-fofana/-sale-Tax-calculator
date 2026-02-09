import os

def get_state():
  state = input ("Enter your state abbreviation (ex: NJ, NY,CA):").upper()
  return state
  
  def set_tax_rate(state):
    state_tax_rates = {"NJ": 0.06625,"NY": 0.04,"CA": 0.0725,"TX":0.0625,"FL":0.06}
def get_number_items():
 return int(input("How many items do you have? "))
 
def get_state():
  state = input ("Enter your state abbreviation (ex: NJ, NY,CA):").upper()
  return state
  
  def set_tax_rate(state):
    state_tax_rates = {"NJ": 0.06625,"NY": 0.04,"CA": 0.0725,"TX":0.0625,"FL":0.06}
def get_number_items():
 return int(input("How many items do you have? "))

def get_prices(number_items):
  prices = []
  for i in range(number_items):
    price = float(input("Enter the price of the item: "))
    prices.append(price)
  return prices
  
def set_tax_rate():
  tax_rate = 0.06625
  return tax_rate

def calculate_taxes(tax_rate, prices):
  taxes = []
  for price in prices:
    tax = round((price * tax_rate), 2)
    taxes.append(tax)
  return taxes
  
def calculate_fin_costs(prices, taxes):
  final_costs = []
  os.system("clear")
  for i in range(len(prices)):
    final_cost = prices[i] + taxes[i]
    final_costs.append(final_cost)
  total_tax = sum(taxes)
  total_cost = sum(final_costs)
  return final_costs, total_tax, total_cost
  
  
def print_receipt(prices, taxes, final_costs, total_tax, total_cost):
    print("RECEIPT")
    print("=======")
    for i in range(len(prices)):
      print("Price: $%s" % (prices[i]))
      print("Sales Tax: $%s" % (taxes[i]))
      print("Final Cost: $%s" % (final_costs[i]))
      print("")
      print("-----------")
    print("=======")
    print("Total Tax: $%s" % (total_tax))
    print("Total Cost: $%s" % (total_cost))

def main():
  num_items = get_number_items()
  prices = get_prices(num_items)
  tax_rate = set_tax_rate()
  taxes = calculate_taxes(tax_rate, prices)
  final_costs, total_tax, total_cost = calculate_fin_costs(prices, taxes)
  print_receipt(prices, taxes, final_costs, total_tax, total_cost)
  
main()  

def get_prices(number_items):
  prices = []
  for i in range(number_items):
    price = float(input("Enter the price of the item: "))
    prices.append(price)
  return prices
  
def set_tax_rate():
  tax_rate = 0.06625
  return tax_rate

def calculate_taxes(tax_rate, prices):
  taxes = []
  os.system("clear")
  for price in prices:
    tax = round((price * tax_rate), 2)
    taxes.append(tax)
  return taxes
  
def calculate_fin_costs(prices, taxes):
  final_costs = []
  os.system("clear")
  for i in range(len(prices)):
    final_cost = prices[i] + taxes[i]
    final_costs.append(final_cost)
  total_tax = sum(taxes)
  total_cost = sum(final_costs)
  return final_costs, total_tax, total_cost
  
  
def print_receipt(prices, taxes, final_costs, total_tax, total_cost):
    print("RECEIPT")
    print("=======")
    for i in range(len(prices)):
      print("Price: $%s" % (prices[i]))
      print("Sales Tax: $%s" % (taxes[i]))
      print("Final Cost: $%s" % (final_costs[i]))
      print("")
      print("-----------")
    print("=======")
    print("Total Tax: $%s" % (total_tax))
    print("Total Cost: $%s" % (total_cost))

def main():
  num_items = get_number_items()
  prices = get_prices(num_items)
  tax_rate = set_tax_rate()
  taxes = calculate_taxes(tax_rate, prices)
  final_costs, total_tax, total_cost = calculate_fin_costs(prices, taxes)
  print_receipt(prices, taxes, final_costs, total_tax, total_cost)
  
main()  
