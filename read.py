#Function for the Shop details 
import write
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


#A function for the header of the Table 
def display_products():
    """Displays the items for the txt file in a tabular format"""
    
    header = ["S.N","Product Name", "Brand", "Per Price", "Stock", "Origin"] #Storing the column name in list 

    print("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗")
    print("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(
        header[0], header[1], header[2], header[3], header[4], header[5]))
    print("╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣")




#Function for reading the file 
def read_file_display(filename): 
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

#function For Just reading and returning the 2D list 
def read_file(filename): 
    """ Open the product file and reads the product and returns the 2D list  """
    
    file = open(filename,"r")  #opening the file  
    items2D = [] #creating a list to store 2D list   
    
    for each in file.readlines(): #Looping and reading the file lines 
    
        new_list = each.strip().split(",")# Striping and making a list of each line 
     
        items2D.append(new_list)
    return items2D

def product_selection():
    """Takes the Product and its quantity """ 
    try: 
    # An array List for Bought Products 

        #Now A loop, if the user wants to enter multiple items 
        while True :
                    
        #User Input for the Product 
            item_number = int(input("Enter the Item number : ")) 
            products = read_file("products.txt") 

            found = False 

            #Verifying the Product 
            for product in products:  
                if item_number == int (product[0]): 
                    found = True     
                    print(f"Selected item : {product[1]}")

                    # Quantity 
                    item_quantity = int (input("Enter the Quantity of Products : "))
                    in_stock = False
                    if item_quantity <= int(product[4]) and item_quantity > 0 : 
                        print("In Stock")
                        in_stock = True
                        break 
                    if not in_stock: 
                        print("No in stock")
                        break 
                            
                    #For the Conformation of the Item 
                    user_name = input("Enter Your name : ")
                    confirmation = input("Check out (y/n) : ").lower()

                            #Check Out Process
                    if confirmation == "y": 
                        write.check_out(user_name,product,item_quantity)
                            
                    if confirmation == "n": 
                        print("Purchase Cancelled")
                        break 

                    else: 
                        print("Enter a valid input")
                            

                        #For Item Not Found 
                if not found: 
                    print("Item Not Found, Please try again! ")
                    break

    except ValueError: 
        print("""
                                                        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                                          Please Enter the item number   
                                                        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """)