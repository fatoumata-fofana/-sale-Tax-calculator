import os

def get_state():
    
    valid_states = {
        "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
        "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
        "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
        "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
        "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

    while True:
        state = input("Enter your state abbreviation: ").upper()
        if state in valid_states:
            return state
        else:
            print("Invalid state. Try again.")
      
def set_tax_rate(state):

    state_tax_rates = {
      
        "AL": 0.04,
        "AK": 0.0,
        "AZ": 0.056,
        "AR": 0.065,
        "CA": 0.0725,
        "CO": 0.029,
        "CT": 0.0635,
        "DE": 0.0,
        "FL": 0.06,
        "GA": 0.04,
        "HI": 0.04,
        "ID": 0.06,
        "IL": 0.0625,
        "IN": 0.07,
        "IA": 0.06,
        "KS": 0.065,
        "KY": 0.06,
        "LA": 0.0445,
        "ME": 0.055,
        "MD": 0.06,
        "MA": 0.0625,
        "MI": 0.06,
        "MN": 0.06875,
        "MS": 0.07,
        "MO": 0.04225,
        "MT": 0.0,
        "NE": 0.055,
        "NV": 0.0685,
        "NH": 0.0,
        "NJ": 0.06625,
        "NM": 0.05125,
        "NY": 0.04,
        "NC": 0.0475,
        "ND": 0.05,
        "OH": 0.0575,
        "OK": 0.045,
        "OR": 0.0,
        "PA": 0.06,
        "RI": 0.07,
        "SC": 0.06,
        "SD": 0.045,
        "TN": 0.07,
        "TX": 0.0625,
        "UT": 0.061,
        "VT": 0.06,
        "VA": 0.053,
        "WA": 0.065,
        "WV": 0.06,
        "WI": 0.05,
        "WY": 0.04,
        "DC": 0.06}
        
    return state_tax_rates[state]

def get_number_items():
    return int(input("How many items do you have? "))

def get_prices(number_items):
    prices = []
    for i in range(number_items):
        price = float(input("Enter the price of the item: "))
        prices.append(price)
    return prices

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
        print("Price: $%s" % prices[i])
        print("Sales Tax: $%s" % taxes[i])
        print("Final Cost: $%s" % final_costs[i])
        print("")
        print("-----------")

    print("=======")
    print("Total Tax: $%s" % total_tax)
    print("Total Cost: $%s" % total_cost)

def main():
  
    state = get_state()
    tax_rate = set_tax_rate(state)

    num_items = get_number_items()
    prices = get_prices(num_items)

    taxes = calculate_taxes(tax_rate, prices)
    final_costs, total_tax, total_cost = calculate_fin_costs(prices, taxes)
  
    print_receipt(prices, taxes, final_costs, total_tax, total_cost)

main()




