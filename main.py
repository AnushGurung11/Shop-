# Importing other operational files
import read as rf
import write as wf
import operation as ops

# Displaying the main header of the shop 
rf.shop_header()

# The program will run till the user wants to stop 
while True:
    
    #Menu option 
    rf.choice()

    # Using try except exception handeling in the block of code
    try:
        
        # taking user input for the main operation 
        print("=============================")
        print("    Choose an Option (1-4) ")
        print("=============================")

        user_choice = int(input("->  ")) 

        
        if user_choice == 1: 
            
            # Displaying the products present in the main inventory 
            rf.display_products("products.txt") 
        
        elif user_choice ==2: 
            
            # Displaying the products in inventory 
            rf.display_products("products.txt")

            # Method called for selecting the products 
            rf.product_selection("products.txt")

        
        elif user_choice == 3: 

            # Displays the restock options 
            rf.restock_display()

            try: 
                print("=============================")
                print(" Select restock option (1-3) ")
                print("=============================")
                choice = int(input(">> "))
                
                # Conditional branching for the user input 
                if choice == 1: 
                    
                    # Displays the products in main inventory 
                    rf.display_products("products.txt")

                    # 2D list for the multiple selections 
                    restocks = []

                    # For serializing the items 
                    counter = 1
                        
                    # Runs till user finishes adding items   
                    while True:

                        item_number = int(input("\n🛍️  Item Number: "))

                        # Method returns 2D list reading main inventory 
                        products = rf.read_file("products.txt")

                        found = False

                        # checks each list form the 2D list 
                        for each in products: 
                            
                            if item_number == int(each[0]): 
                                print(f"\n Selected Item: {each[1]}")

                                found = True 
                                
                                item_quantity = int(input("\n🧮 Item Quantity: "))

                                if item_quantity < 0: 
                                    print("\n❌  Sorry, quantity cannot be reduced. Please adjust your order. ❌\n")
                                    break 
                                else: 
                                    
                                    wf.restock_existing_items(item_number,products,item_quantity)

                                    #Creating a list to pass for the billing / invoice 
                                    restock_list = list()
                                    restock_list.append(str(counter)) 
                                    restock_list.append(each[1])
                                    restock_list.append(each[3])
                                    restock_list.append("0")
                                    restock_list.append(item_quantity)
                                    restock_list.append(str(ops.sub_total(float(item_quantity), float(restock_list[2]))))
                                    
                                    # Adding to the 2D list 
                                    restocks.append(restock_list)

                        # If the products is not found                                    
                        if not found:  
                            print("\n⚠️  Product does not exist. Please check your selection. ⚠️\n")         
                            break 
                        
                        print("\nWant to add more (y/n)")
                        add_more = input("\n-> ").strip().lower()

                        if add_more == "y": 

                            # increasing the counter by 1
                            counter += 1 
                            continue

                        elif add_more == "n": 
                            break   
                       
                    wf.invoice("WeCare","9819819811",restocks) 
                    
            
                    
                    
                    
                                    
                        
                elif choice == 2: 
                    
                    # Adding new products in the main inventory 
                    rf.new_arrivals()

                elif choice == 3: 
                    
                    # For the confirmation 
                    print("\n--->Confirm your exit (y/n).")
                    confirm = input("->").strip().lower()

                    if confirm == "y": 
                        print("\nThank You\n")
                        break
                    
                    elif confirm == "n":
                        continue

                    else: 
                        print("\n❌ Invalid input. Exiting Restock Option... ❌\mn")
                        break
                else : 
                    print("\n❌  Please select a valid option from the menu. (1-4) ❌\n")
            
            # Handeling Value error 
            except ValueError: 
                # Handled when an wrong data type is being cased to another
                print("⚠️  ::::::: Please Enter a Valid Input ::::::: ⚠️")
            
            
        elif user_choice == 4 : 

            #Taking a confimation 
            terminate = input("\n⚠️  Do you want to exit the program? (y/n): ").strip().lower()

            #if y : termiantes the program 
            if terminate == "y": 
                print("\n🎉  Thank You for your purchase! Have a great day! 🎉\n")
                break

            #if n : will not terminate the program 
            elif terminate == "n": 
                print("\n❌  Termination Denied! Please try again. ❌\n")
                
            #if the input is any other alphabet the message will show up 
            else: 
                print ("\n❌ Invalid Input ❌\n")
            
           
        # in case user enters number except 1-4
        else: 
            print("⚠️  Please select a valid option from the menu (1 - 4) ⚠️")


    # In case of Type cast error (Alphabets and special characters cannot be int)    
    except ValueError: 
        print("⚠️  Please select a valid option from the menu (1 - 4) ⚠️")

        


 




 