
import write as wf
import operation as ops
import datetime as dt


#header of the Shop
def shop_header (): 
    """Shop Details"""
    print  ("""
                                                            
                                                                              WeCare         
                                                                        ---------------------                                                 
                                                                        Matepani-12, Pokhara  
                                                                         Contact: 9810000000      
        """
    )

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
         
def read_file(filename): 
    """ Open the product file and reads the product and returns the 2D list  """
    
    file = open(filename,"r")   
    items2D = []    
    
    for each in file.readlines(): 
        new_list = each.strip().split(",") 
     
        items2D.append(new_list)
    return items2D

def  product_selection(filename):
    """Takes the Product and its quantity """

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
        user_name = input(">>Enter your name : ").strip().title().replace(":","_")
        phone = int(input(">>Enter your phone number : "))

        #Calling a bill method 
        wf.invoice(user_name,phone, cart_list)
        

    except ValueError: 
        print ("!! Enter a valid Phone number. ")

def product_cart(fileName, counter):

    while True:

        try:

            item_number = int(input(">>Enter the Item number: "))

            products = read_file(fileName)

            found = False

            for product in products:

                if item_number == int(product[0]):
                    found = True
                    print(f"->Selected item: {product[1]}")

                    item_quantity = int(input(">>Enter the Quantity of Products: "))

                    if item_quantity <= 0 or item_quantity > int(product[4]):
                        print("!!Not in stock or invalid quantity.")
                        break

                    stock = int(product[4]) - item_quantity
                    offer_item_check = item_quantity // 3
                    free_items = 0

                    if stock == 0:
                        print("->Sorry, there are no free items left.")

                    elif offer_item_check > stock:
                        print(f">>You will get {stock} for free!!!")
                        free_items = stock

                    else:
                        free_items = offer_item_check
                        print(f">>Congratulations! You get {free_items} items for free.")

                    confirmation = input("Confirm your purchase (y/n): ").lower().strip()

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
                        print("Transaction Cancelled")
                        return []

                    else:
                        print("Wrong input, Transaction declined")
                        return []

            if not found:
                print("Item Not Found")
                break

        except ValueError: 
            print("!! Enter  a valid input ")

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

                               WeCare
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

    print("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗")
    print("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(
        "S.N","Product Name", "Brand", "Per Price", "Stock", "Origin"))
    print("╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣")

def read_file_contents(filename): 
    """ This finction will read the file and store all its'content and print it in the terminal"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File not found at path: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def new_arrivals(): 
    """This function will add new items in the inventory."""

    counter = 1

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

            arrival_list = []
            arrival_list.append(counter)
            arrival_list.append(name)
            arrival_list.append(brand)
            arrival_list.append(rate)
            arrival_list.append(quantity)
            arrival_list.append(country)

            arrivals.append(arrival_list)

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

                wf.append_products(arrivals)
                wf.invoice("WeCare",9819819811,arrivals_bill)
                read_file_contents("WeCare")
                break

        except ValueError: 
            print("::::::: Please Enter a Valid Input ::::::::")
    

        

