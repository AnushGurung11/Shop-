
import write as wf
import operation as ops



#header of the Shop
def shop_header (): 
    """Shop Details"""

    # multi string 
    print  ("""
                                                            
                                        ✨ WeCare ✨         
                                   ----------------------                                               
                                    Matepani-12, Pokhara  
                                     Contact: 981981981     
        """
    )

def choice(): 
    """This method will display the menu options """

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

def display_products(filename): 
    """ Open the product file and reads the product """

    # Displaying the title in table format 
    print("\n")
    print("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗")
    print("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(
        "S.N","Product Name", "Brand", "Per Price", "Stock", "Origin"))
    print("╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣")
    
    # Reads the main file and stores in 2D list 
    items2D = read_file(filename)    
    
    # Looping through each items 
    for product in items2D: 
         
        # printing the elements of the list in tabular format 
        print("║{:<20}║{:<20}║{:^20}║{:>20}║{:>20}║{:^20}║".format(
            # mo method is called to show the marked price of the products
            product[0], product[1], product[2], ops.mp(product[3]), product[4],product[5]))
        print("╚" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20+"╩" + "═"*20+ "╩" + "═"*20 + "╝")
         
def read_file(filename): 
    """ Open the product file and reads the product and returns the 2D list  """
    
    # Opening the file in read mode 
    file = open(filename,"r")   
    items2D = []    
    
    # Reading through each lines 
    for each in file.readlines(): 
        
        # Striping each elements and spliting, seperated by coma and converting in to string 
        new_list = each.strip().split(",") 
        # Making a 2D list of the contents of the file 
        items2D.append(new_list)

    # Returns the 2D list 
    return items2D

# This function is for the buying option which takes the user input and returns the 2D list of products to buy
def  product_selection(filename):
    """Takes the Product and its quantity """

    
    cart_list = []

    # For couinting the number of items selected 
    counter = 1 
    while True:  
        
        # Collects each items selected form the products cart function 
        cart_list.append(product_cart(filename,counter)) 
        counter += 1

        try: 
                # Asking for the user input for more items 
            add_more = input("\nAdd more (y/n) : \n").strip().lower()

    	    # Will continue the loop 
            if add_more == "y": 
                continue
                    
            elif add_more == "n": 
                print("\n🎁 Thank you for your purchase\n")
                #This will terminate the loop 
                break 

            else: 
                # Raise will create an expetion for the invalid input 
                raise Exception("\n ⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")
            
        except Exception: 
                print("\n⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")


    # Taking user name 
    try: 
        #Preplacing the ":" because the txt will not allow it
        user_name = input("\n🌟 >> Enter your name: ").strip().title().replace(":", "_")
        phone = int(input("\n📱 >> Enter your phone number: "))


        #Validating the cart 
        valid_cart = [item for item in cart_list if len(item) == 6]

        if valid_cart:
            wf.invoice(user_name, phone, valid_cart)
            
        else:
            print("\nX-------No valid products were selected. Empty invoice Generated--------X")


    except ValueError:
        # If the data type is incorrect  
        print ("\n  ::::::: Please Enter a Valid Input ::::::: ")

def product_cart(fileName, counter):
    """This function will ask for the items to buy and the quentity and retiurns the 1D list """

    # Loop the block of code 
    while True:

        try:
            print("\n🛍️  Item Number:")

            item_number = int(input("->  "))

            # Reading the main text file and listing the elements in a 2D list
            products = read_file(fileName)

            found = False

            # Looping through each elements
            for product in products:

                if item_number == int(product[0]):
                    found = True

                    print(f"\n Selected Item: {product[1]}\n")

                    print("\n🧮 Enter the quantity of products:")

                    item_quantity = int(input("->  "))

                    # Checking the items for the free items 
                    if item_quantity <= 0 or item_quantity > int(product[4]):
                        print("\n    !!Not in stock or invalid quantity.    ")
                        break

                    stock = int(product[4]) - item_quantity
                    offer_item_check = item_quantity // 3
                    free_items = 0

                    if stock == 0:
                        print("\n -> Sorry, there are no items left. <- ")

                    elif offer_item_check > stock:
                        print(f"\n >> You will get {stock} items as per the scheme!!! <<\n")
                        free_items = stock

                    else:
                        free_items = offer_item_check
                        print(f"\n >>  You get {free_items} items as per the scheme. <<\n ")

                    
                    confirmation= input("->  Confirm purchase? (y/n): ").strip().lower()
                    


                    # If the user confirm append in the list 
                    if confirmation == "y":

                        product_list = list()
                        product_list.append(str(counter))             
                        product_list.append(product[1])              
                        product_list.append(ops.mp(product[3]))           
                        product_list.append((free_items))
                        product_list.append(str(item_quantity))
                        product_list.append(str(ops.sub_total(float(ops.mp(product[3])),item_quantity)))

                        # Update stock in the file
                        wf.update_main(ops.add(free_items, item_quantity), str(item_number))
                                   
                        return product_list
                    
                    elif confirmation == "n":
                        print("\n******** Transaction Cancelled ******** \n")
                        return []

                    else:
                        print("\n XXX- Wrong input, Transaction declined -XXX")
                        return []

            if not found:
                print("\n Item Not Found 🔍?")
                return []

        except ValueError: 
            print("\n  ::::::: Please Enter a Valid Input ::::::: ")

def restock_display():
    """Displays the header of the restocking options"""
    print("""
=====================================
|     1. Restock Existing Item      |
|     2. Restock New Item           |
|     3. Exit                       |
=====================================
""")
    

def read_file_contents(filename): 
    """ This finction will read the file and store all its'content and print it in the terminal"""
    try:
        # Opening the file in read mode 
        with open(filename, 'r') as file:
            # Reading all the contents of the file and storing 
            content = file.read()
            #P Printing all the contents 
            print(content)

    except FileNotFoundError:
        # If file not found this exception is shown 
        print(f"\n Error: File not found at path: {filename} ")

    except Exception as e:
        # For any other exceptions 
        print(f"\n⚠️ An error occurred: {e} ")

def new_arrivals(): 
    """This function will add new items in the inventory."""

    counter = 1
    # Creating two 2D list, one for appending to the main stock and another one for billing 
    arrivals = []
    arrivals_bill =[]

    while True:

        try: 

            print("\n🛍️  Item Name: ")
            name = input("---->").strip().title()

            print("\n Item Brand: ")
            brand = input("---->").strip().title()

            print("\nItem Rate:")
            rate = float(input("----->"))

            print("\nItem Quantity")
            quantity = int(input("---->"))

            print("\nOrigin: ")
            country = input("---->").strip().title()

            # New list to store the update details 
            arrival_list = []
            arrival_list.append(counter)
            arrival_list.append(name)
            arrival_list.append(brand)
            arrival_list.append(rate)
            arrival_list.append(quantity)
            arrival_list.append(country)

            arrivals.append(arrival_list)

            # New List for biling details
            bill_list = []
            bill_list.append(counter)
            bill_list.append(name)
            bill_list.append(rate)
            bill_list.append("0")
            bill_list.append(quantity)
            bill_list.append(str(ops.sub_total(float(rate),quantity)))

            arrivals_bill.append(bill_list)

            print("\nAdd more(y/n)")
            more = input("---->").strip().lower()

            if more == "y": 

                counter += 1
                continue

            elif more == "n":
                print()
                break 

            name = "WeCare"
            number = 9819819811

            # Updating the inventory 
            wf.append_products(arrivals)

            # Invoice creating 
            wf.invoice(name,number,arrivals_bill)

            # Reading the contents of the file 
            read_file_contents(f"{name}.txt")
                

        except ValueError: 
            print("\n  ::::::: Please Enter a Valid Input ::::::: ")
    

        

