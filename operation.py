"""
All the mathmetical function of the main file is here
"""

#For Addition 

def add(a,b,c=0,d=0,e=0): 
    """
    This Function can add upto 5 numbers(float, int)
    Any string input will be concatinated
    """

    try:
        return a+b+c+d+e
     
    except(ValueError):
        return "Enter a valid int or float"

#For Subtraction
    
def sub(a,b,c=0,d=0,e=0): 
    """
    This function will subtract 2 - 5 numbers 
    """

    try:
        return a-b-c-d-e
     
    except(ValueError):
        return "Enter a valid int or float"
    
#For Multiplication 

def mul(a,b,c=1,d=1,e=1):
    """
    This function will multiply 2 - 5 numbers 
    """
    try: 
        return a*b*c*d*e
    
    except(ValueError):
        return "Enter a valid int or float " 

#Setting the selling price of an item
#The selling price is 200% more than the Cost price 
def selling(cost):
    """
    It will calcuate the selling price of an item 
    """
    try: 
        sp = cost + (200/100)*cost
        return sp 
    
    except(ValueError): 
        return "Ënter a int or float"

    
        
    
    

