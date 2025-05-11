
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

                    restocks = []

                    counter = 1
                        
                    while True: 
                        item_number = int(input(">> Product Number: "))

                        products = rf.read_file("products.txt")

                        found = False

                        for each in products: 
                            
                            
                            if item_number == int(each[0]): 
                                print(f"-> Item: {each[1]}")

                                found = True 

                                item_quantity = int(input(">> Product Quantity: "))

                                if item_quantity < 0: 
                                    print("!! Sorry quantity cannot be reduced")
                                    break 
                                else: 
                                    
                                    wf.restock_existing_items(products,item_quantity)

                                    #Creating a list to pass for the billing / invoice 
                                    restock_list = list()
                                    restock_list.append(str(counter)) 
                                    restock_list.append(each[1])
                                    restock_list.append(each[3])
                                    restock_list.append("0")
                                    restock_list.append(item_quantity)
                                    restock_list.append(str(ops.sub_total(float(item_quantity), float(restock_list[2]))))
                                    
                                    restocks.append(restock_list)
                                    print(restocks)
                                    


                                                        
                        if not found:  
                            print("!! Product does not exist. ")         
                            break 

                        add_more = input(">> Want to add more (y/n)").strip().lower()

                        if add_more == "y": 

                            counter += 1 
                            

                            continue

                        elif add_more == "n": 
                           
                            wf.invoice("WeCare","9819819811",restocks)
                           
                            rf.read_file_contents("WeCare.txt")
                           
                            print(">>Stock Updated successfully<<")
                            break                    
                        
                elif choice == 2: 
                    rf.new_arrivals()

                elif choice == 3: 
                    
                    print("------------>Confirm your exit (y/n).")
                    confirm = input("------->").strip().lower()

                    if confirm == "y": 
                        print("Thank You")
                        break
                    
                    elif confirm == "n":
                        continue

                    else: 
                        print("****** Wrong input exiting the restock option ******")
                        break
                else : 
                    print("!! Select an option form the menu. ")
            except ValueError: 
                print("!! Enter a valid input. ")
            
            
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

        


 




 