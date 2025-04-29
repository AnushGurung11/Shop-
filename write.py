import read as rf
import operation as ops
import datetime as dt






def invoice(user_name, cart_list):
    """Generates a bill for each customer"""

    # ([SN in original list, Product name, Brand , per cost , Stock , origin , Sub total , s.n for buyer, no of free Item, Total bought  ])
    # Cart_list Contains the following 
    
    #header list 
    header = ["S.N", "Product", "Brand", "Country", "Per cost","Free Item", "Quantity", "Sub Total"]

    print(cart_list)

    # testing inside a loop 
    for each in cart_list: 
        for one in each: 
            print(one)

    #Testing 
    # for each in cart_list: 
    #     print(each)

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


    #Heading of the Bill 
    # bill.writelines("""
    #                                                         ┌──────────────────────────────────────┐
    #                                                         │           POKHARA COSMETICS          │
    #                                                         │                                      │
    #                                                         │        Pokhara, Matepani-12, Nepal   │
    #                                                         │           Contact: 9810000000        │
    #                                                         └──────────────────────────────────────┘ 
    #         """)
    


        #Writing the date and time 
    bill.write("Date : ")
    bill.write(f"{year}-{month}-{day}\n")

    bill.write("Time : ")
    bill.write(f"{hour}-{minute}-{sec}\n")

        # writes the user name and goes to the next line 
    bill.write("Cutomer Name : ")
    bill.write(f"{user_name}\n")


#["S.N", "Product", "Brand", "Country", "Per cost","Free Item", "Quantity", "Sub Total"]
    bill.write("="*140 + "\n")
    bill.write("|| {:<20}||{:<20}|| {:<20}||{:<20}|| {:<20}||{:<20}|| {:<20}||\n".format(
                header[0],header[1],header[2],header[3],header[4],header[5],header[6],header[7]))
    bill.write("="*140 + "\n")


    # ([SN in original list, Product name, Brand , per cost , Stock , origin , Sub total , s.n for buyer, no of free Item, Total bought  ])

    for each in cart_list:  
        bill.write("|| {:<20}||{:<20}|| {:<20}||{:<20}|| {:<20}||{:<20}|| {:<20}||\n".format(
                each[7],each[1],each[2],each[5],each[3],each[8],each[9],each[6]))
            

    
                

        
        
    bill.close()
            

        

            
    




# A function to update the main products.txt file 
def update_main(quantity): 
    pass    


    


