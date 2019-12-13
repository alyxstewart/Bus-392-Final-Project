# BUS 392 Final Project
# Adam Watson and Alyx Stewart

import csv
import sys
import datetime
import random


def main():
    print("                         UPC Reader Menu                          ")
    print("------------------------------------------------------------------")
    print( "1. Record Sale")
    print( "2. Retrieve Online Orders")
    print( "3. Update Catalog")
    print( "4. Terminate Program")
    
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

    for item in items:
        print(item)

# Function to generate and return random prices for items
def get_price():
    ran_price = random.uniform(.99,4.99)
    return ran_price


#RECORD SALE FUNCTIONS: 
def record_sale():


# Function that runs
def create_order_number():
    
    # Create time stamp    
    today = datetime.date.today()

    # Formate date
    date = today.strftime("%m%d%Y")
    
    # Varible to hold order number (combion count and date)
    unique_order_number = date + "-" + order_number
    
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
    

# Run product description lookup.



# Run product price lookup.



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


# Date line function to create lines of data for receipt/sqlite.
def data_line(item,subtotal, sales_tax, grand_total):
    
    
    
#Function to prompt user to see if they want a printed receipt
def want_receipt ():
    # Prompt user if they want a receipt
    decision = input ("Would you like to print a receipt? (Y or N) : ")
    decision.upper()
    
    # Return decision
    return decision

# Function to write sale to file.
def write_sale(decision,unique_order_number,
    if decision == "Y":
        receipt unique_order_number
        receipt = open (receipt_file_name.txt, "w")
        receipt.write(data)
        # Change data to whatever we name the UPC file return info
        receipt.close()
        
    else:
        print ("No Receipt")
        
# ONLINE ORDER FUNCTIONS:

# UPDATE CATALOG FUNCTIONS:
        
# TERMINATE PROGRAM FUNCTION:
def terminate_program():
    exit()
    
