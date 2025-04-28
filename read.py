
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
def product_cart(fileName,counter):  
        
        while True :
                    
        #User Input for the Product 
            item_number = int(input("Enter the Item number : ")) 

            # Gets The 2D list by reading the file 
            products = read_file(fileName)

            # Selected item is stored here (For multiple Options a 2D list is stored)



            #Setting the item as not found 
            found = False 

            # Looping to find the product  
            for product in products:  

                #Checking the S.N in list 
                if item_number == int (product[0]): 

                    # Showing the selected item 
                    print(f" Selected item : {product[1]}")

                    # is in list 
                    found = True     

                    # Quantity 

                    try: 
                        
                        # Try catch : for getting the correct input
                        item_quantity = int (input("Enter the Quantity of Products : "))

                        # For checking in the stock 

                        #First it is not in stock 
                        in_stock = False

                        # Offer check 
                        offer_item_check = item_quantity // 3

                        #Free items 
                        free_items = 0

                        # The product quantity must be in range 
                        if item_quantity > 0 and item_quantity < int(product[4]) :

                            # marking in stock 
                            in_stock = True 
                            
                            # Checking of there are products to give free or not 
                            stock = int(product[4]) - item_quantity

                            # Actual getting free item is greater than the available item in the Stock 
                            if offer_item_check > stock : 

                                #You will get what's left in the stock 
                                getting_offer = offer_item_check - stock 

                                print ( f"You are getting {getting_offer} for free!!!")

                                #passing the free item 
                                free_items = getting_offer

                            #If item is in stock you will get the actual free quantity 
                            elif offer_item_check < stock : 

                                print(f"You will get {offer_item_check} for free!!!")

                                free_items = offer_item_check



                            # Confirming the buying process
                            confirmation = input("Confirm your purchase(y/n)").strip().lower()

                            # For Yes 
                            if confirmation == "y": 

                                #Sub total for the products 
                                sub_total = float(product[3]) * item_quantity
                                
                                # First adding the info of sub total and SN number in the product info 
                                product_list = list(product)

                                #adding sub total in the product info 
                                product_list.append(str(sub_total))

                                #adding the S.N for the buyer 
                                product_list.append(str(counter))

                                #adding number of free item 
                                product_list.append(str(free_items))

                                

                                

                            elif confirmation == "n": 
                                print("Transaction Cancelled")
                                break 
                            else: 
                                print(" Wrong input, Transaction declined")
                                break

                        if not in_stock: 
                            print("Not in stock")
                            break 
                    
                    except Exception: 
                        print(" !!! Only enter numbers ")

            if not found: 
                print("Item Not Found")
                break

            return product_list









# Product selection 
def product_selection():
    """Takes the Product and its quantity """

    # ([SN in original list, Product name, Brand , per cost , Stock , origin , Sub total , s.n for buyer, no of free Item ])
    #Its a 2D list 
    cart_list = []

        #Counter to count the number of inputs in the list 
    counter = 1 
    while True:  

        # Asking for the user input for more items 
        add_more = input(" Add more (y/n) : ").strip().lower()

        #If yes then I will call the function and add the list 
        #also adds the counter (S.N)
        if add_more == "y" :
            cart_list.append(product_cart("products.txt",counter)) 

            
        elif add_more == "n": 
            #This will terminate the loop 
            break 

        else: 
            # Raise will create an expetion for the invalid input 
            raise Exception(" Invalid input ")

    print(cart_list)
    
    # After the Products are selected and added to the cart_list 
    # Billing process starts 

    #Confirmation
    # User name for the Bill 
    # 
    #  
    # user_name = input("Enter Your name : ").strip().title()

    # wf.bill(user_name,cart_list)
        

