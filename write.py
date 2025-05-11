import read as rf
import operation as ops
import datetime as dt

def invoice(user_name,phone, cart_list):
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

    #Multiple line string for the VAT Bill 
   
    
    # A new bill is created 
    bill = open(f"{user_name}.txt","w")

  
    title = f"""

                                                                        TAX INVOICE
                                                                        -----------

                                                                            WeCare
                                                                    Matepani-12, Pokhara
                                                                    -------------------



Date: {year}-{month}-{day}                                                                                                          Time:{hour}-{minute}-{sec}
Name: {user_name}                                                                                                              
Phone: {phone}


"""
    bill.write(title)


#["S.N", "Product", "Per cost","Free Item", "Quantity", "Sub Total"]
    bill.write("="*140 + "\n")
    bill.write("|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}|| {:<20}||\n".format(
            "S.N","Products" ,"Per Cost","Free Items","Quantity","Sub Total"))
    bill.write("="*140 + "\n")


    total_cost = 0
    for each in cart_list:

        bill.write("|| {:<20}|| {:<20}|| {:>20}|| {:>20}|| {:>20}|| {:>20}||\n".format(
            each[0], each[1], f"Rs.{each[2]}", each[3], str(each[4]), f"Rs.{each[5]}"))
        bill.write("-"*140 + "\n") 

        total_cost += float(each[5])
            
    bill.write("="*140+"\n")

    
    vat_amount = ops.vat_amount(total_cost)
    grand_total =ops.add(total_cost, vat_amount)
    payment = f"""
                                                                                            || Total               ||          Rs.{total_cost:>7}|| 
                                                                                            ------------------------------------------------
                                                                                            || Vat Amount          ||           Rs.{vat_amount:>7}||
                                                                                            ------------------------------------------------
                                                                                            || Grand Total         ||           Rs.{grand_total:>7}||
                                                                                            ------------------------------------------------ 

"""


    bill.write(payment)
    bill.close()
    rf.read_file_contents(f"{user_name}.txt")

def update_main(quantity,sn):
    """Deduct the stock """

    with open('products.txt', 'r') as file:
        lines = file.readlines()

    
    for i in range(len(lines)):

        if lines[i].startswith(sn):

            parts = lines[i].strip().split(',')
            parts[-2] = str(int(parts[-2])-quantity)  

            new_line = (parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + parts[3] + ',' + parts[4] + ',' + parts[5] + '\n')

            lines[i] = new_line
            break

    
    with open('products.txt', 'w') as file:
        file.writelines(lines)



def append_products(restock):
    with open('products.txt', 'r') as file:
        lines = file.readlines()

    # Get the last serial number from the file
    last_sn = int(lines[-1].split(',')[0]) if lines else 0

    with open('products.txt', 'a') as file:
        for i, product in enumerate(restock):
            new_sn = last_sn + i + 1
            new_line = f"\n{new_sn},{product[1]},{product[2]},{product[3]},{product[4]},{product[5]}"
            file.write(new_line)


def restock_existing_items (products, item_quantity): 
    """Restocking the existing item"""

    updated_lines = []
     
    for line in products: 
                  
        line[4] = str(int(line[4]) + item_quantity)

        new_line = ','.join(line) +'\n'
        updated_lines.append(new_line)
        
    file = open("products.txt","w") 
    file.writelines(updated_lines)
    print("--------------Successfully restocked--------------")
        
        
                    
                    


        























    
    
        


    


