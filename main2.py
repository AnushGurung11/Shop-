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
    
    header = ["Product Name", "Brand", "Per Price", "Stock", "Origin"] #Storing the column name in list 

    print("╔" + "═"*30 + "╦" + "═"*30 + "╦" + "═"*30 + "╦" + "═"*30 + "╦" + "═"*30 + "╗")
    print("║{:^30}║{:^30}║{:^30}║{:^30}║{:^30}║".format(
        header[0], header[1], header[2], header[3], header[4]))
    print("╠" + "═"*30 + "╬" + "═"*30 + "╬" + "═"*30 + "╬" + "═"*30 + "╬" + "═"*30 + "╣")



#Function for reading the file 
def read_file(filename): 
    """ Open the product file and reads the product """
    
    file = open(filename,"r")  #opening the file  
    items2D = [] #creating a list to store 2D list   
    
    for each in file.readlines(): #Looping and reading the file lines 
    
        new_list = each.strip().split(",")# Striping and making a list of each line 
     
        items2D.append(new_list)# Adding the list 
        
    #For Printing each product in the table format 
    for product in items2D: 
         
        print("║{:<30}║{:<30}║{:^30}║{:^30}║{:<30}║".format(
            product[0], product[1], product[2], product[3], product[4]))
        print("╠" + "═"*30 + "╬" + "═"*30 + "╬" + "═"*30 + "╬" + "═"*30+ "╬" + "═"*30 + "╣")
         
    file.close()


#Working interface 
shop_details()
choice()
while True: 
    
    try: 
        user_choice = int(input("Choose (1-4) : "))
        
        if user_choice == 1: 
            display_products()
            read_file("products.txt")
        elif user_choice == 2 : 
            print("Currently un available")
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