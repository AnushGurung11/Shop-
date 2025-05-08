import read as rf
import operation as ops
import datetime as dt


#Invoice for the restock
def restock_invoice(user_name,restock):
    
    # Date in the bill 
    date = dt.datetime.now()

    #Getting the date 
    year = date.year
    month = date.month
    day = date.day

    #getting the time 
    hour = date.hour
    minute = date.minute
    sec = date.second
    
    # A new bill is created 
    bill = open(f"{user_name}.txt","w")

        #Writing the date and time 
    bill.write("Date : ")
    bill.write(f"{year}-{month}-{day}\n")

    bill.write("Time : ")
    bill.write(f"{hour}-{minute}-{sec}\n")

        # writes the user name and goes to the next line 
    bill.write("Cutomer Name : ")
    bill.write(f"{user_name}\n")


#counter, name, Brand, Per Cost, Quantity, Origin, Sub total

    bill.write("="*140 + "\n")
    bill.write("|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| \n".format(
            "S.N","Products" ,"Brand","Per Cost","Quantity", "Origin","Sub Total"))
    bill.write("="*140 + "\n")

    total_cost = 0
    for each in restock:

        bill.write("|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}||\n".format(
            each[0], each[1], each[2], f"Rs.{each[3]}", str(each[4]), each[5], str(each[6])))
        bill.write("-"*140 + "\n")  # Added separator line between rows

        total_cost += float(each[6])
            
    bill.write("="*140+"\n")

    #For VAT 
    vat_percent = 13
    vat_amount = float(total_cost*(vat_percent/100))
    bill.write(f"VAT percent = {vat_percent}% \n")
    bill.write(f"VAT amount = {vat_amount}\n")
    bill.write(f"Total Cost = Rs.{total_cost+vat_amount}")
    bill.close()



#Invoice for the customers
def invoice(user_name, cart_list):
    """Generates a bill for each customer""" 

    # Date in the bill 
    date = dt.datetime.now()

    #Getting the date 
    year = date.year
    month = date.month
    day = date.day

    #getting the time 
    hour = date.hour
    minute = date.minute
    sec = date.second
    
    # A new bill is created 
    bill = open(f"{user_name}.txt","w")

        #Writing the date and time 
    bill.write("Date : ")
    bill.write(f"{year}-{month}-{day}\n")

    bill.write("Time : ")
    bill.write(f"{hour}-{minute}-{sec}\n")

        # writes the user name and goes to the next line 
    bill.write("Cutomer Name : ")
    bill.write(f"{user_name}\n")


#["S.N", "Product", "Per cost","Free Item", "Quantity", "Sub Total"]
    bill.write("="*140 + "\n")
    bill.write("|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}||\n".format(
            "S.N","Products" ,"Per Cost","Free Items","Quantity","Sub Total"))
    bill.write("="*140 + "\n")

#Format inside the cart_List 
# ([SN in original list, Product name, Brand, per cost, Stock, origin, Sub total, s.n for buyer, no of free Item, Total bought])

#For total cost 
    total_cost = 0
    for each in cart_list:

        bill.write("|| {:<20}|| {:<20}|| {:>20}|| {:>20}|| {:>20}|| {:>20}||\n".format(
            each[7], each[1], f"Rs.{each[3]}", each[8], each[9], f"Rs.{each[6]}"))
        bill.write("-"*140 + "\n")  # Added separator line between rows

        total_cost += float(each[6])
            
    bill.write("="*140+"\n")

    #For VAT 
    vat_percent = 13
    vat_amount = float(total_cost*(vat_percent/100))
    bill.write(f"VAT percent = {vat_percent}% \n")
    bill.write(f"VAT amount = {vat_amount}\n")
    bill.write(f"Total Cost = Rs.{total_cost+vat_amount}")
    bill.close()
            


# A function to update the main products.txt file 
#Here the total quantity and product list in of the stock file and the item number is being passed
def update_main(quantity,sn):

    #Opening the file in both read and write mode 
    # file = open("products.txt","r+")

    #Now checking through each line and checking for the sn (Serial number)
    # Step 1: Read the file
    with open('products.txt', 'r') as file:
        lines = file.readlines()

    # Step 2: Update the specific line
    for i in range(len(lines)):
        if lines[i].startswith(sn):
            parts = lines[i].strip().split(',')
            parts[-2] = str(int(parts[-2])-quantity)  
            # Manually rebuild the line
            new_line = (parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + parts[3] + ',' + parts[4] + ',' + parts[5] + '\n')
            lines[i] = new_line
            break

    # Step 3: Write updated lines back to the file
    with open('products.txt', 'w') as file:
        file.writelines(lines)


def update_main_stock(restock):
    with open('products.txt', 'r') as file:
        lines = file.readlines()

    for each in restock:
        product_name = each[1].strip()
        add_quantity = int(each[4])
        found = False

        for i in range(len(lines)):
            parts = lines[i].strip().split(',')

            if parts[1].strip() == product_name:
                # Update quantity
                parts[4] = str(int(parts[4]) + add_quantity)

                # Rebuild the line manually
                new_line = (parts[0] + ',' + parts[1] + ',' + parts[2] + ',' +
                            parts[3] + ',' + parts[4] + ',' + parts[5] + '\n')
                lines[i] = new_line
                found = True
                break

        if not found:
            # Manually construct new line for new product
            new_line = (str(each[0]) + ',' + str(each[1]) + ',' + str(each[2]) + ',' +
                        str(each[3]) + ',' + str(each[4]) + ',' + str(each[5]) + '\n')
            lines.append(new_line)

    # Write updated lines back to the file
    with open('products.txt', 'w') as file:
        file.writelines(lines)






def restock_existing_items (products,item_number, item_quantity): 
    """Restocking the existing item"""

    updated_lines = []
     
    for line in products: 
                  
        line[4] = str(int(line[4]) + item_quantity)

                    # Rebuild the line manually
        new_line = ','.join(line) +'\n'
        updated_lines.append(new_line)
        
    file = open("products.txt","w") 
    file.writelines(updated_lines)
        
        
                    
                    


        






















#Now passing the restock item which is 2D list 
# def update_main_stock(restock):
    
#     with open('products.txt', 'r+') as file:
#         lines = file.readlines()

#     for each in restock:
#         for i in range(len(lines)):
            
#             if lines[i].startswith(each[1]):
#                 parts = lines[i].strip().split(',')
#                 parts[4] = str(int(parts[4])+int(each[4]))  
#                 # Manually rebuilding the line
#                 new_line = (parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + parts[3] + ',' + parts[4] + ',' + parts[5] + '\n')
#                 lines[i] = new_line
#                 file.writelines(lines)
#                 break

#             elif lines[2] != each[2]: 
#                 new_line = (str(each[0]) + ',' + str(each[1]) + ',' + str(each[2]) + ',' +str( each[3]) + ',' +str( each[4]) + ',' +str( each[5]) + '\n')
#                 file.writelines(new_line)


   
    
        



        
    



    
    



    #What can I do over here is 
    # Read the file and take the Line which as the exact Indexing entered by the user at first and then change the stock number by the total quantity 
    # I need to pass the SN and then check the Item accordingly 

    
    
        


    


