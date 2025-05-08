display = """
1. Restock 
2. Add new stock
3. Back
"""

stock = int(input("Choose: "))

if stock == 1:
    item_num = int(input("Enter the product number :"))
    item_quantity = int(input("Enter the quantity to restock: "))

    #Read the txt file and update the Stock
    
elif stock == 2: 
    # Read the txt file 
    # check the indexing fom[-1] and take the [0] 
    # Enter the product details and update the file 
    pass
elif stock == 3: 
    # Break
    print("Thank You !")
    
else: 
    print("Please enter a valid input")


