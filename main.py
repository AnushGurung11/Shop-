
import read as rf
import write as wf
import operation as ops


#Displays the shop info
rf.shop_header()



while True:
    
   
    rf.choice()

     
    try:
        
        user_choice = int(input("Choose a number form (1 - 4) : ")) # Check 

        
        if user_choice == 1: 
            rf.display_products("products.txt") #Check
        
         
        elif user_choice ==2: 
            
            rf.display_products("products.txt")

            rf.product_selection("products.txt")

        
        elif user_choice == 3: 

            rf.restock_display()

            try: 
                choice = int(input(">> "))
                
                if choice == 1: 
                     
                    rf.display_products("products.txt")
                        
                    

                    while True: 
                        item_number = int(input(">> Product Number: "))

                        products = rf.read_file("products.txt")

                        found = False

                        for each in products: 
                            
                            
                            if item_number == int(each[0]): 
                                print(f"Item: {each[1]}")

                                found = True 

                                item_quantity = int(input(">> Product Quantity: "))

                                if item_quantity < 0: 
                                    print("!! Sorry quantity cannot be reduced")
                                    break 
                                else: 
                                    wf.restock_existing_items(products,item_number,item_quantity)

                                    rf.exist_restock_invoice(item_number,item_quantity)
                                    print(">>Stock Updated successfully<<")
                                                        
                        if not found:  
                            print("!! Product does not exist. ")         
                            break 

                        add_more = input(">> Want to add more (y/n)").strip().lower()

                        if add_more == "y": 
                            continue
                        elif add_more == "n": 
                            print("!! Thank You !!")
                            break                    
                        
                elif choice == 2: 
                    pass
                elif choice == 3: 
                    pass
                else : 
                    print("!! Select an option form the menu. ")
            except ValueError: 
                print("!! Enter a valid input. ")
            
            # #Creating an empty list for the invoice 
            # restock = []
            # counter = 0
            # while True: 
            #     #Temporary list 
            #     temp =[]
            # #user input for the product details 
            #     try: 
            #         name = input("Enter the Product name: ").strip().title()
            #         brand = input("Enter the brand name: ").strip().title()
            #         perCost = float(input("Enter the perCost: "))
            #         quantity = int(input("Enter the quantity: "))
            #         origin = input("Enter the country of origin: ").strip().title()

            #         sub_total = perCost * quantity
            #         counter +=1

            #         print(f"Product: {name}, Brand: {brand}, Per Cost: {perCost}, Quantity: {quantity}, Origin: {origin}")

            #         #Adding the elements in the 
            #         temp.append(counter)
            #         temp.append(name)
            #         temp.append(brand)
            #         temp.append(perCost)
            #         temp.append(quantity)
            #         temp.append(origin)
            #         temp.append(sub_total)

            #         restock.append(temp)

                    

            #         #Confirmation 
            #         confirm = input("Confirm the purchase(y/n) : ").strip().lower()
            #         if confirm == "y": 

            #             more = input("More products(y,n)? ").strip().lower()
            #             if more == "y":
            #                 continue

            #             if more =="n": 
            #                 print("The transaction has been terminated.")
            #                 break

            #             else: 
            #                 print("Choose between (y/n)")
            #                 break 
            #         elif confirm =="n": 
            #             print("Transaction has been terminated")
            #             break

            #     except Exception: 
            #         print("Please enter the correct value")
            # #Now creating a bill for the restock items 
            # wr.restock_invoice("Pokhara Cosmetics", restock)
            # wr.update_main_stock(restock)
        
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
        print("Choose Only Form 1,2,3 and 4")

        


 




 