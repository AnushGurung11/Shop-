def invoice(user_name, product, quantity): 
    """Generates an invoice for the items bought"""
    total_cost = int(product[0]) * quantity

    file = open("Invoice.txt","w")
    header = ["SN", "Product", "Quantity", "Per Cost", "Country", "Total Cost"]
    file.write("╔" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╦" + "═"*20 + "╗\n")
    file.write("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(header[0], header[1], header[2], header[3], header[4], header[5]))
    file.write("\n╠" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╬" + "═"*20 + "╣\n")
    file.write("║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║{:^20}║".format(product[0], product[1], str(quantity), product[4], product[5], str(total_cost))) 
    file.write("\n╚" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╩" + "═"*20 + "╝\n")
    print("Invoice generated successfully.")