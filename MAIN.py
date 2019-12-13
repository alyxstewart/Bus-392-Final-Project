# BUS 392 Final Project
# Adam Watson and Alyx Stewart

import csv
import sys
import datetime
import random
import sqlite3

def main():
    print("                         UPC Reader Menu                          ")
    print("------------------------------------------------------------------")
    print( "1. Record Sale")
    print( "2. Retrieve Online Orders")
    print( "3. Update Catalog")
    print( "4. Terminate Program")
    
    # Set order_number equal to 1.
    order_number = 1
    
    # Prompt user to make a menu selection
    another = input ("Would you like to make a selection? (Y or N) :" )
    while another == "Y" or "y":
        selection = input("Please make a selection (1,2,3,or 4): " )
        if selection == "1":
            # Run the Record Sale functions
            #Recordsale()
            create_order_number(upc)
            calculate_total (price)
            want_receipt ()
        elif selection == "2":
         # Run the Retrieve Online Order functions
        elif selection == "3":
        # Run the Update Catalog functions
        elif selection == "4":
          #Run the Terminate Program functions
            terminate_program()
        elif selection != "1" or selection != "2" or selection != "3" or selection != "4":
            print ("ERROR: Please enter valid selection number")
            selection = input("Please make a selection (1,2,3,or 4): " )

            
#ENTIRE PROGRAM FUNCTIONS:   
# Function to convert CSV file to a list
def CSV_to_list():
    # Reads in the csv file to a list
    infile = open('UPC.csv', 'r',encoding='utf-8-sig')
    items = []
    for line in infile:
        items.append(line.rstrip('\n').split(','))

    for item in items:
        item.append(ran_price=get_price())
    
    return items
        

# Function to create our sqlite database and add tables
# for our catalog and sales records.
def create_database():
    # Establish a connection to the new database.
    conn = sqlite3.connect("conveniencestore.db")
    
    # Create a cursor object.
    c = conn.cursor()
    
    # Create a table for our catalog.
    c.execute('''CREATE TABLE catalog
                (upc text, description text, price real)''')
    
    # Create a table to record each sale into the database.
    c.execute('''CREATE TABLE sales
                (order_num text, upc text, description text, price real, \
                subtotal real, sales_tax real, total real)''')
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

        
# Function to generate and return random prices for items
def get_price():
    ran_price = random.uniform(.99,4.99)
    return ran_price


# Function to create the initial catalog.
def create_catalog(items):
    # Establish a connection to the database.
    conn=sqlite3.connect("conveniencestore.db")
    
    # Create a cursor object.
    c = conn.cursor()
    
    # Create a loop which will go through each index
    # of the items list and add a new row of data to 
    # the database catalog.
    for index in items:
        # Run get_price to produce a random price for this good.
        random_price = get_price()
        
        # Add this row to the catalog.
        c.execute("INSERT INTO catalog VALUES(items[index][0],items[index][1],random_price)")
        
        # Commit the change after each iteration.
        conn.commit()
    
    # Close the connection when finished iterating.
    conn.close()


#RECORD SALE FUNCTIONS: 
def record_sale():


# Function that creates a unique order number.
def create_order_number(order_number):
    
    # Create time stamp    
    today = datetime.date.today()

    # Formate date
    date = today.strftime("%m%d%Y")
    
    # Varible to hold order number (combine count and date)
    unique_order_number = date + "-" + order_number
    
    # Add to order_number
    order_number += 1
    
    # Return unique order number.
    return unique_order_number


# Add items function will prompt clerk to enter items until they
# are finished adding entire cart.
def add_items():
    # Accumulator variable for while loop.
    keep_going = 'y'
    
    # Cart list
    cart = []
    
    # Loop that adds items until the user is done.
    while keep_going == "y":
        # Prompt user to enter in a UPC
        item = input("Enter UPC here: ")
        
        # Add item to cart.
        cart.append(item)
        
        # Prompt user to keep going.
        keep_going = input("Would you like to keep going? (Enter y if yes)")
        
        # Return cart
        return cart
    

# Run product price lookup.
def run_product_lookup(item):
    # Establish a connection to the database.
    conn = sqlite3.connect("conveniencestore.db")
    
    # Create a cursor object.
    c = conn.cursor()
    
    # Lookup the item UPC in sqlite and return the price.
    t = (item,)
    c.execute("SELECT * FROM catalog WHERE description=?",t)
    product_info = [c.fetchone()]
    
    # Name the price and the description and return them.
    description = product_info[1]
    price = product_info[2]
    
    # Return those values
    return description, price
    
    
# Function to calculate subtotal.
def calculate_subtotal(cart):
    # Create subtotal variable
    subtotal = 0
    
    # For loop to lookup all item prices in cart
    for items in cart:
        price = run_price_lookup()
        
        # Add up all the item prices
        subtotal += price
    
    # Return subtotal
    return subtotal


# Function to calculate tax.
def calculate_tax(subtotal):
    # Calculate sales tax
    sales_tax = subtotal * .08

    # Return sales tax
    return sales_tax


# Function to calculate grand total.
    # Calculate grand total
    grand_total = subtotal + sales_tax

    # Return total
    return grand_total


# Data line function to create lines of data for receipt/sqlite.
def data_line(item):
    # Lookup the price
    price = run_price_lookup(item)
    
    # Lookup the description
    description = run_description_lookup(item)
    
    # Add item, price, and description to one line as a string.
    data_string = item + "\t" + description + "...................." + price
    
    # Return data string.
    return data_string
    
    
#Function to prompt user to see if they want a printed receipt
def want_receipt ():
    # Prompt user if they want a receipt
    decision = input ("Would you like to print a receipt? (Y or N) : ")
    decision.upper()
    
    # Return decision
    return decision


# Function to write sale to file.
def write_sale(decision,unique_order_number,data_string,cart):
    if decision == "Y":
        # Open a new text file 
        receipt = open(unique_order_number.txt, "w")
        
        # For each item in the cart, add each item's data line to the file.
        for items in cart:
            # Run data line for the item to create a string.
            data_string = data_line(item)
            
            # Write the data string to the receipt text file.
            receipt.writeline(data_string+"\n")
        
        # Change data to whatever we name the UPC file return info
        receipt.close()
        
    else:
        print ("No Receipt")
        

# Function to push sale information to sqlite database.
def save_sale(unique_order_number,cart,subtotal,sales_tax,grand_total):
    # Establish a connection to the sqlite database.
    conn=sqlite3.connect("conveniencestore.db")
    
    # Create a cursor object.
    c = conn.cursor()
    
    # Add the order number to the appropriate collumn
    c.execute("INSERT INTO sales VALUES(unique_order_number,"","","","","","")")
    
    # Commit the change before moving on.
    conn.commit()
              
    # For each item in the cart add a row to the sqlite database
    for item in cart:
        # Run product description lookup and price lookup.
        description = run_product_lookup(item)
        price = run_product_lookup(item)
        
        # Add a new row to the database in sqlite.
        c.execute("INSERT INTO sales VALUES("",item,description,price,"","","")")
        
        # Commit those changes.
        conn.commit()
        
    # Add a new row with subtotal, tax, and grand total.
    c.execute("INSERT INTO sales VALUES("","","","",subtotal,sales_tax,grand_total)")
    
    # Commit these changes.
    conn.commit()
    
    # Close the database when finished.
    conn.close()
   

# ONLINE ORDER FUNCTIONS:

def retrieve_online_orders (online_order):
    unpickled_order = unpickle_online_orders(online_order)
    create_online_order(online_order)
        
def unpickle_online_orders(filename):
    online_order_file = open (filename, 'rb')
    new_online_order = pickle.load(online_order_file)
    online_order_file.close
    
    return new_online_order

def create_online_order(new_online_order):
    record_sale(new_online_order)
    
# UPDATE CATALOG FUNCTIONS:
# Function to gather information for new item entry.
def new_item():
    # Prompt user to enter in UPC, description, and price.
    upc = input("Enter UPC here: ")
    description = input("Enter description here: ")
    price = float(input("Enter price here: "))
    
    # Return those values
    return upc,description,price
    
    
def update_catalog(upc,description,price):
    # Establish a connection to the database
    conn = sqlite3.connect("conveniencestore.db")
    
    # Create a cursor object.
    c = conn.cursor()
    
    # Insert a new row of data.
    c.execute("INSERT INTO catalog VALUES(upc,description,price)")
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection when done.
    conn.close()
    

# TERMINATE PROGRAM FUNCTION:
def terminate_program():
    exit()
    
