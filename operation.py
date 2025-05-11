
def mp(rate):
    """Returns the 200% of the actual rate""" 
    r = float(rate)
    final_rate = r + 3*r

    return final_rate

def sub_total(quantity, rate): 
    """This fuction will multiply any two numbers"""

    total = float(quantity * rate)
    return total

def add(a,b): 
    """This function will add any two numbers"""

    sum = int(a + b)
    return sum 

def vat_amount(total): 
    """This function calculate the grand total including vat"""
    vat_percent = 13
    vat_amount = float(total*(vat_percent/100))
    return vat_amount


    