import read as rf
import operation as ops
import datetime as dt


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

        bill.write("|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}||\n".format(
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

        
    



    
    



    #What can I do over here is 
    # Read the file and take the Line which as the exact Indexing entered by the user at first and then change the stock number by the total quantity 
    # I need to pass the SN and then check the Item accordingly 

    
    
        


    


