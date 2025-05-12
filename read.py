
import write as wf
import operation as ops



#header of the Shop
def shop_header (): 
    """Shop Details"""

    # multi string 
    print  ("""
                                                            
                                                                        ✨  WeCare  ✨         
                                                                    -------------------------                                                 
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
            add_more = input("Add more (y/n) : \n").strip().lower()

    	    # Will continue the loop 
            if add_more == "y": 
                continue
                    
            elif add_more == "n": 
                print("Thank You !\n")
                #This will terminate the loop 
                break 

            else: 
                # Raise will create an expetion for the invalid input 
                raise Exception(" ⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")
            
        except Exception: 
                print("⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")


    # Taking user name 
    try: 
        #Preplacing the ":" because the txt will not allow it
        user_name = input("🌟 >> Enter your name: ").strip().title().replace(":", "_")
        phone = int(input("📱 >> Enter your phone number: "))


        #Validating the cart 
        valid_cart = [item for item in cart_list if len(item) == 6]

        if valid_cart:
            wf.invoice(user_name, phone, valid_cart)
            
        else:
            print("No valid products were selected. Empty invoice Generated")


    except ValueError:
        # If the data type is incorrect  
        print ("⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")

def product_cart(fileName, counter):
    """This function will ask for the items to buy and the quentity and retiurns the 1D list """

    # Loop the block of code 
    while True:

        try:
            print("Item number")
            item_number = int(input("--->"))

            products = read_file(fileName)

            found = False

            for product in products:

                if item_number == int(product[0]):
                    found = True
                    print(f"->Selected item: {product[1]}")

                    print("Enter the Quantity of Products")
                    item_quantity = int(input("--->"))

                    # Checking the items for the free items 
                    if item_quantity <= 0 or item_quantity > int(product[4]):
                        print("⚠️    !!Not in stock or invalid quantity.    ⚠️")
                        break

                    stock = int(product[4]) - item_quantity
                    offer_item_check = item_quantity // 3
                    free_items = 0

                    if stock == 0:
                        print("❌ -> Sorry, there are no free items left. <- ❌")

                    elif offer_item_check > stock:
                        print(f"🎁 >> You will get {stock} for free!!! 🎉")
                        free_items = stock

                    else:
                        free_items = offer_item_check
                        print(f"🎉 >> Congratulations! You get {free_items} items for free. << 🎉")

                    confirmation = input("Confirm your purchase (y/n): ").lower().strip()

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
                        print("❌ Transaction Cancelled ❌")
                        return []

                    else:
                        print("🚫 Wrong input, Transaction declined 🚫")
                        return []

            if not found:
                print("🔍 Item Not Found 🔍")
                return []

        except ValueError: 
            print("⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")

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
        print(f"❌ Error: File not found at path: {filename} ❌")

    except Exception as e:
        # For any other exceptions 
        print(f"⚠️ An error occurred: {e} ⚠️")

def new_arrivals(): 
    """This function will add new items in the inventory."""

    counter = 1
    # Creating two 2D list, one for appending to the main stock and another one for billing 
    arrivals = []
    arrivals_bill =[]

    while True:

        try: 

            print("Product name")
            name = input("---->").strip().title()

            print("Brand")
            brand = input("---->").strip().title()

            print("Rate")
            rate = float(input("----->"))

            print("Quantity")
            quantity = int(input("---->"))

            print("Made in ")
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

            print("Add more(y/n)")
            more = input("---->").strip().lower()

            if more == "y": 

                counter += 1
                continue

            elif more == "n": 

                name = "WeCare"
                number = 9819819811

                # Updating the inventory 
                wf.append_products(arrivals)

                # Invoice creating 
                wf.invoice(name,number,arrivals_bill)

                # Reading the contents of the file 
                read_file_contents(f"{name}.txt")
                break

        except ValueError: 
            print("⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")
    

        

