"""
Main Python file : Main Interface of the program 
"""

#Function for the Shop details 
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



#Working interface 
shop_details()
choice()
while True: 
    
    try: 
        user_choice = int(input("Choose (1-4) : "))
        
        if user_choice == 1: 
            display_products()
            read_file_display("products.txt")
        elif user_choice == 2 : 
            #Now Asking for the Item number and Its Quantity 
            try: 
                item_number = int(input("Enter the Item number : "))
                products = read_file("products.txt")

                found = False 
                for product in products:
                    if item_number == int (product[0]):
                        print(f"Selected item is {product[1]}")
                        found = True 
                        break 
                    if not found: 
                        print("Item Not Found ")
                
                item_quantity = int (input("Enter the Quantity of Products : "))
                for product in products: 

                    in_stock = False
                    if item_quantity <= int(product[4]) and item_quantity > 0 : 
                        print("We have in stock ")
                        found = True 
                        break 
                    if not in_stock: 
                        print("We Dont have in stock ")
                    

                
                    

            except ValueError: 
                print("""
                                                                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                                                  Please Enter the item number   
                                                                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                """)
                


        elif user_choice == 3: 
            print("All stocked")
        elif user_choice == 4 : 
            break
        else : 
            print("""
                                                                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                                                  VALID INPUTS:  1 • 2 • 3 • 4  
                                                                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  """)
    except ValueError: 
        print("""
                                                                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                                                  VALID INPUTS:  1 • 2 • 3 • 4  
                                                                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  """)
        



# In 2 option : When pressed Asking for the item to by and Quantity 
# Then Showing the selected Item and its quantity . Then also showing the Item selected and quantity 
# Enter your name and press Confirm 
# Updating the main Stock and aslo Creating a bill 
 