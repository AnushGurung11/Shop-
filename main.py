"""
Task: 
1. read the txt file 
2. make a 2D list form the content of txt file 
3. Display the 2D list in a suitable manner 

>> modular approach 
"""

#initaial display 
home =""" -----------------------------------------
-----------------------1. View --------------------
-----------------------2. Buy ---------------------
-----------------------3. Exit --------------------
"""

print(home)

i = 0
while  i <= 1: 
    try: 
        user = int (input("Choose : "))
        if user == 1: 
            file = open("products.txt","r")
            lines = file.read().split("\n")
           # products = lines.split()
            print(lines)
            #print(products)
            file.close()
        elif user == 2: 
            print("Sold Out ")

        elif user ==3 : 
            print("Thank Your for time")
            break 
        else : 
            print("Please enter 1,2 or 3")
    except (ValueError): 
        print("Please enter form the above options 1,2,3")
    
    





