import read as rf
import operation as ops
import datetime as dt






def bill(user_name,cart_list):
    """Generates a bill for each customer"""

    grand_total = 0
    
   

    

       

    #Creating a file for each user 
    file = open(f"{user_name}.txt","w")
    file.write(
    """
                                                            ┌──────────────────────────────────────┐
                                                            │           POKHARA COSMETICS          │
                                                            │                                      │
                                                            │        Pokhara, Matepani-12, Nepal   │
                                                            │           Contact: 9810000000        │
                                                            └──────────────────────────────────────┘   
                                                            
    """)

    # An object for date and time
    date = dt.datetime.now()
    #Current time in Hour Minute and second 
    time = str(date.strftime("%H,%M,%S")).replace(":","-")

    year = str(date.year)
    month = str(date.month)
    day = str (date.day)

    file.write(f"Date : {year}-{month}-{day}")
    file.write(f"Time (H/M/S): {time}")
    file.write(f"Name : {user_name}")
    
    header = ["SN", "Product", "Quantity", "Per Cost", "Country", "Total Cost"]
    file.write("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗\n")
    file.write("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(header[0], header[1], header[2], header[3], header[4], header[5]))

    for each in cart_list:

        grand_total += ops.total_cost(each[4],each[-1])

        file.write("\n╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣\n")
        file.write("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(each[0], each[1], str(each[-1]), each[4], each[5], str(ops.total_cost(each[4],each[-1])))) 
        file.write("\n╠" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╣\n")

    file.write("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format("", "", "", "", "Grand Total", str(grand_total)))
    file.write("\n╚" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╝\n")
    print("Invoice generated successfully ")

    


