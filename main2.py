"""
Main Python file : Main Interface of the program 
"""

import read 
import write


def check_out(user_name,product,quantity):
    """Confirms the Product and calls the invoice function"""
    user_name = input("Enter Your name : ")
    confirmation = input("Check out (y/n) : ").lower()

    #Check Out Process
    if confirmation == "y": 
        write.invoice(user_name, product, quantity)
                            
    if confirmation == "n": 
        print("Purchase Cancelled")
         
    else: 
        print("Enter a valid input")

    


#Working interface 
read.shop_details()

while True: 
    
    try: 
        read.choice()
        user_choice = int(input("Choose (1-4) : "))
        
        if user_choice == 1: 
            read.display_products()
            read.read_file_display("products.txt")

        elif user_choice == 2 : 
            #Now Asking for the Item number and Its Quantity  
            read.product_selection()   #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Looping problem 
            break
                
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

 