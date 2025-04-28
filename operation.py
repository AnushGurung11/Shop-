def market_price(perCost):
    """ calculates the marked price of perCost Item  """
    perCost = float(perCost)+ 3*float(perCost)

    return perCost
    

def total_cost(quantity, per_cost):
    """Calculates the total cost of the products"""

    cost = float(per_cost)*int(quantity)
    return cost 

