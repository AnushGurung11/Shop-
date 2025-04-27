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
                # An array List for Bought Products
                selected_item = [] 

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
                            for product in products:
                                in_stock = False
                                if item_quantity <= int(product[4]) and item_quantity > 0 : 
                                    print("In Stock")
                                    in_stock = True
                                    break 
                                if not in_stock: 
                                    print("No in stock")

                            


                            break 
                        if not found: 
                            print("Item Not Found, Please try again! ")
                            break

                    # Now Taking the Customer name as input 
                    # Name will be used in the billing 

                    user_name = input("Enter Your name : ") 

                    # Conformation of the purchase 
                    confirmation = input(" Confirm your purchase y/n : ").lower().strip()

                    if confirmation == "y": 
                        #Opening the file and updating the txt file 
                        print("Purchased Successfully")
                        #Making a new txt file where you will print the bill 
                        file = open("Invoice.txt", "w", encoding="utf-8")  # Added encoding for special characters
                        header = ["SN","Product","Quantity","Per Cost","Country","Total Cost"]
                        file.write("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗\n")
                        file.write("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(
                        header[0], header[1], header[2], header[3], header[4], header[5]))
                        file.write("╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣\n")
                        file.close()
                    
                    elif confirmation == "n": 
                        print("Confiration declined")
                    
                    else :
                        print(" Please Enter a valid input ")




                    

                
                    

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
        



 


# Updating the main Stock and aslo Creating a bill 
# Adding The list that is selcted store it in a new 2D list and later print the same list in the file 
# Quantity multiple of 3 get 1 free and total becomes 3*Selling price , total goods = 4 , sub to the stock 

 