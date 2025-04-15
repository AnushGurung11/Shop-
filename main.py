

def read_file(filename): 
    """ To open the file in read mode and display the products details"""
    
    #By default the file always opens in read mode 
    file = open(filename,"r")
    
    print(file.readlines())


def display_products():
    """Displays the items for the txt file in a tabular format"""
    #Storing the column name in list 
    header = ["Product Name", "Brand", "Per Price", "Stock", "Origin"]
    #printing the column headers with left align and dedicated space of 20 
    print(f"{header[0]:<20}{header[1]:<20}{header[2]:<20}{header[3]:<20}{header[4]:<20}")
    # A line to divide the header form the content 
    print("-"*70)
    
    

def main_menu(): 
    """"Displays the main menu """
    home = """------------------------------------------
-------------- 1. View products ------------
-------------- 2. Buy Products -------------
-------------- 3. Exit ---------------------
--------------------------------------------"""
    print(home)  

#main function

#This loop will automatically run during execution of the program
while True: 
    #displaying the main menu 
    main_menu()
    #Using try except to check the user input and handel errors 
    try: 
        # taking user input to execute the program 
        user= int(input("Choose : "))
        #if the user input is 1 then read_file method is called and products.txt file is passed 
        if user == 1: 
            display_products()
            read_file("products.txt")

        # if the user input is 2 then the following will print 
        elif user == 2: 
            print("Unavailable")
        # if the user inputis 3 then the following will print and loop will break 
        elif user == 3:
            print("Thank you")
            break 
        # If user input any other number then this will print 
        else:
            print("Choose 1,2 or 3 only")
    # If the user input is String then a value error will occur due to error in casting and will be handeled by ValueError 
    except (ValueError):
        print("Enter 1,2 or 3") 






