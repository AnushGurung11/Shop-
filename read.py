
import write as wf
import operation as ops
import datetime as dt


#header of the Shop
def shop_header (): 
    """Shop Details"""
    print  ("""
                                                            
                                                                          POKHARA COSMETICS          
                                                                        ---------------------                                                 
                                                                        Matepani-12, Pokhara  
                                                                         Contact: 9810000000      
        """
    )


#Option to choose 
def choice(): 
    print(

        """
                                                                    ______________________________
                                                                    |        * SHOP MENU *       |
                                                                    |____________________________|
                                                                    | 1. 👀  View Products       |
                                                                    |                            |
                                                                    | 2. 💰  Buy Products        |
                                                                    |                            |
                                                                    | 3. 🔄  Restock Products    |
                                                                    |                            |
                                                                    | 4. ❌  Exit                |
                                                                    |____________________________|
        """

    )




    def restock_display():
        print("""
        =====================================
        |     1. Restock Existing Item      |
        |     2. Restock New Item           |
        |     3. Exit                       |
        =====================================
    """)
    





     
def exist_restock_invoice(item_number, item_quantity):

    date = dt.datetime.now()
    
    today = date.date()


    bill = f"""
    ================================================================
                            TAX INVOICE
                            -----------

                        POKHARA COSMETICS
                        Matepani-12, Pokhara
                        -------------------

    Date: {today}                           
    Name: Anush Gurung                            Phone: 98111111
    ===================================================================
    """

    header = """
    ====================================================================
    |  SN  |        Name                     | Qty  | Rate | Sub Total |
    ====================================================================
    """

    print(bill)
    print(header)

    products = read_file("products.txt")
    counter = 1

    for product in products: 
        if product[0] == int(item_number): 
            rate = int(product[3]) 
            subTotal = rate *  item_quantity
            counter += 1
            print(f"""
    |  {counter:<4}|  {product[1]:<31}| {item_quantity:>5}| {rate:>5}| {subTotal:>10}|        
""")    
    







#Display products in the stock in tabular form 
def display_products(filename): 
    """ Open the product file and reads the product """

    print("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗")
    print("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(
        "S.N","Product Name", "Brand", "Per Price", "Stock", "Origin"))
    print("╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣")
    

    items2D = read_file(filename)    
    
    for product in items2D: 
         
        print("║{:<20}║{:<20}║{:^20}║{:>20}║{:>20}║{:^20}║".format(
            product[0], product[1], product[2], ops.mp(product[3]), product[4],product[5]))
        print("╚" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20+"╩" + "═"*20+ "╩" + "═"*20 + "╝")
         
    

# Reads the file and returns a 2D list
def read_file(filename): 
    """ Open the product file and reads the product and returns the 2D list  """
    
    file = open(filename,"r")   
    items2D = []    
    
    for each in file.readlines(): 
        new_list = each.strip().split(",") 
     
        items2D.append(new_list)
    return items2D


# Returns the 2D list of items added to the cart
def product_cart(fileName, counter):
    while True:
        try:
            item_number = int(input("Enter the Item number: "))


            products = read_file(fileName)
            found = False

            for product in products:
                if item_number == int(product[0]):
                    found = True
                    print(f"Selected item: {product[1]}")

                    
                    item_quantity = int(input("Enter the Quantity of Products: "))

                        

                    if item_quantity <= 0 or item_quantity > int(product[4]):
                        print("Not in stock or invalid quantity.")
                        break

                    stock = int(product[4]) - item_quantity
                    offer_item_check = item_quantity // 3
                    free_items = 0

                    if stock == 0:
                        print("Sorry, there are no free items left.")
                    elif offer_item_check > stock:
                        print(f"You will get {stock} for free!!!")
                        free_items = stock
                    else:
                        free_items = offer_item_check
                        print(f"Congratulations! You get {free_items} items for free.")

                    confirmation = input("Confirm your purchase (y/n): ").strip().lower()

                    if confirmation == "y":

                        #Making it in di
                        sub_total = float(product[3]) * item_quantity
                        product_list = list(product)
                        product_list.append(str(sub_total))              # Subtotal
                        product_list.append(str(counter))               # Buyer's SN
                        product_list.append(str(free_items))            # Free items
                        product_list.append(str(free_items + item_quantity))  # Total qty

                        # Update stock in the file
                        wf.update_main(int(free_items + item_quantity), str(item_number))
                        
                        
                        return product_list


                    elif confirmation == "n":
                        print("Transaction Cancelled")
                        return []

                    else:
                        print("Wrong input, Transaction declined")
                        return []

            if not found:
                print("Item Not Found")
                break

        except ValueError: 
            print(" !! Enter  a valid input ")


    













# Product selection 
def product_selection(filename):
    """Takes the Product and its quantity """

    # ([SN in original list, Product name, Brand , per cost , Stock , origin , Sub total , s.n for buyer, no of free Item ])
    #Its a 2D list 
    cart_list = []


    counter = 1 
    while True:  

        
        cart_list.append(product_cart(filename,counter)) 
        counter += 1


        try: 
                # Asking for the user input for more items 
            add_more = input("Add more (y/n) : \n").strip().lower()

            if add_more == "y": 
                continue
                    
            elif add_more == "n": 
                print("Thank You !\n")
                #This will terminate the loop 
                break 

            else: 
                # Raise will create an expetion for the invalid input 
                raise Exception(" Invalid input ")
            
        except Exception: 
                print("Enter a valid Input")


    # Taking user name 
    try: 
        #Preplacing the ":" because the txt will not allow it
        user_name = input("Enter your name : ").strip().title().replace(":","_")

        #Calling a bill method 
        wf.invoice(user_name, cart_list)
        

    except Exception: 
        print ("Enter a valid input")





    

        

