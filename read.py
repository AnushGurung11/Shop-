
import write as wf


#header of the Shop
def shop_details (): 
    """Shop Details"""
    print  ("""
                                                            ┌──────────────────────────────────────┐
                                                            │           POKHARA COSMETICS          │
                                                            │                                      │
                                                            │        Pokhara, Matepani-12, Nepal   │
                                                            │           Contact: 9810000000        │
                                                            └──────────────────────────────────────┘        
            
"""
    )


#Option to choose 
def choice(): 
    print(

        """
                                                                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                                                ┃        ✨ SHOP MENU ✨     ┃
                                                                ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                                                ┃ 1. 👀  View Products       ┃
                                                                ┃                            ┃
                                                                ┃ 2. 💰  Buy Products        ┃
                                                                ┃                            ┃
                                                                ┃ 3. 🔄  Restock Products    ┃
                                                                ┃                            ┃
                                                                ┃ 4. ❌  Exit                ┃
                                                                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """

    )


# Displays the header of the table 
def display_header():
    """Displays the items for the txt file in a tabular format"""
    
    header = ["S.N","Product Name", "Brand", "Per Price", "Stock", "Origin"] #Storing the column name in list 

    print("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗")
    print("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(
        header[0], header[1], header[2], header[3], header[4], header[5]))
    print("╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣")




# Displays the products in the table 
def display_products(filename): 
    """ Open the product file and reads the product """
    
    file = open(filename,"r")  #opening the file  
    items2D = [] #creating a list to store 2D list   
    
    for each in file.readlines(): #Looping and reading the file lines 
    
        new_list = each.strip().split(",")# Striping and making a list of each line 
     
        items2D.append(new_list)# Adding the list 
        
    #For Printing each product in the table format 
    for product in items2D: 
         
        print("║{:<20}║{:<20}║{:^20}║{:^20}║{:<20}║{:^20}║".format(
            product[0], product[1], product[2], product[3], product[4],product[5]))
        print("╚" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20+"╩" + "═"*20+ "╩" + "═"*20 + "╝")
         
    file.close()

# Return a 2D list by reading the contents of the file  
def read_file(filename): 
    """ Open the product file and reads the product and returns the 2D list  """
    
    file = open(filename,"r")  #opening the file  
    items2D = [] #creating a list to store 2D list   
    
    for each in file.readlines(): #Looping and reading the file lines 
    
        new_list = each.strip().split(",")# Striping and making a list of each line 
     
        items2D.append(new_list)
    return items2D


# Returns the 2D list of items added to the cart
def product_cart(fileName):

    try: 
     
         
        while True :
                    
        #User Input for the Product 
            item_number = int(input("Enter the Item number : ")) 
            products = read_file(fileName) 

            

            found = False 

            #Verifying the Product 
            for product in products:  
                if item_number == int (product[0]): 
                    found = True     

                    # Quantity 
                    item_quantity = int (input("Enter the Quantity of Products : "))
                    in_stock = False
                    if item_quantity <= int(product[4]) and item_quantity > 0 : 

                        # Selected Product info 
                        print(f"Item : {product[1]}")
                        print(f"Quantity : {item_quantity}")

                        

                        #Confimation for buying
                        confirmation = input("Confirm (y/n)").strip().lower()

                        if confirmation == "y": 
                            
                            in_stock = True

                            return product, item_quantity
                            

                        elif confirmation == "n": 
                            print("Transaction Cancelled")
                            break 
                        else: 
                            print(" Wrong input, Transaction declined")
                            break

                    if not in_stock: 
                        print("No in stock")
                        break 

            if not found: 
                print("Item Not Found")
                break

    except ValueError: 
        print("""
                                                        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                                          Please Enter the item number   
                                                        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """)







# Product selection 
def product_selection():
    """Takes the Product and its quantity """

    #A 2D list for items in cart 
    cart_list = []
    
    try: 
        numOfProducts = int(input("Enter the number of Products : "))

        for i in range (1, numOfProducts+1):
            product_list, quantity = product_cart("products.txt")
            cart_list.append(product_list)
            cart_list.append(quantity)
        
        #Confirmation 
        user_name = input("Enter Your name : ").strip().title()

        print(cart_list)

    except ValueError: 
        print("Please enter numbers only")