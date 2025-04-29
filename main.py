
import read as rf
import write as wr
import operation as ops


#Working interface 
rf.shop_details()

#Looping for the choices
while True:
    
    # Displayig the ouput of the choice method 
    rf.choice()

    # For run time error 
    try:
        # Input method for User input 
        user_choice = int(input("Choose a number form (1 - 4) : "))

        # 1 will display the products
        if user_choice == 1: 
            rf.display_header()
            rf.display_products("products.txt")
        
        #2 will ask for item number, quantity, user name and will create a bill for the user 
        elif user_choice ==2: 
            
            #Calls the method for selecting products 
            rf.product_selection()

        elif user_choice == 3: 
            print("In Progess")
        
        # To exit the menu
        elif user_choice == 4 : 

            #For the user input 
            try: 

                #Taking a confimation 
                terminate = input("Do you want to exit (y/n): ").strip().lower()

                #if y : termiantes the program 
                if terminate == "y": 
                    print("Thank You !")
                    break

                #if n : will not terminate the program 
                elif terminate == "n": 
                    print("Termination Denied ")
                
                #if the input is any other alphabet the message will show up 
                else: 
                    print ("Enter (y/n) : ")
            
            except ValueError: 
                print("Invalid input ")

        # in case user enters number except 1-4
        else: 
            print("Please select a valid input form (1-4)")


    # In case of Type cast error (Alphabets and special characters cannot be int)    
    except ValueError: 
        print(" Choose Only Form 1,2,3 and 4")

        


# 2 button now when run successfully will returns the list of the product selected 
# Now The selected item is going to be used to prepare the bill 
# Bill Contant (For each person a new Bill ) same person will get different bill in new time 
# 
 




 