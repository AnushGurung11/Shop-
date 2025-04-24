"""
Module for reading the product file .txt and Displaying as the table. 
"""

def read_file(filename): 
    """ To open the file in read mode and display the products details"""
    
    #By default the file always opens in read mode 
    file = open(filename,"r")
    #Creating an empty list 
    items2D = []
    
    #From the file now reading line and looping 
    for each in file.readlines():
        #Here a temporary list is created 
        #Strip removes the extra spaceing and split sperates each string accoring to the ","
        new_list = each.strip().split(",")
        # adding the obtained list form the temporary list to the empty list 
        items2D.append(new_list)
        
        #Now loop places each of the items in a tabluar form by left aligining and reserving 20 space 
    for product in items2D: 
         print(f"{product[0]:<20} {product[1]:<20} {product[2]:<20} {product[3]:<20} {product[4]:<20}")
    file.close()