# BUS 392 Final Project
# Adam Watson and Alyx Stewart

import csv
import sys
import datetime

def main():
    print("                         UPC Reader Menu                          ")
    print("------------------------------------------------------------------")
    print( "1. Record Sale")
    print( "2. Retrieve Online Orders")
    print( "3. Update Catalog")
    print( "4. Terminate Program")
    
    # Prompt user to make a menu selection
    another = input ("Would you like to make a selection? (Y or y for yes) :" )
    while another == "Y" or "y":
        selection = input("Please make a selection (1,2,3,or 4): " )
        if selection == "1":
            # Run the Record Sale functions
            #Recordsale()
            create_order_number(UPC)
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
        
        
#RECORD SALE FUNCTIONS: 

# Function that takes scanned UPC as an argument
def create_order_number (order_number):
    
    # Create time stamp    
    today = datetime.date.today()

    # Formate date
    date = today.strftime("%m%d%Y")
    
    # Varible to hold order number (combion count and date)
    unique_order_number = date + "-" + order_number
    return unique_order_number

# Function to calculate subtotal, tax, and grand total
def calculate_total (price):
    # Add up all the item prices
    total = price += price

    # Calculate sales tax
    sales_tax = total * .08

    # Calculate grand total
    grand_total = total + sales_tax

    # Return total
    return grand_total

#Function Prompt user to see if they want a printed receipt
def want_receipt ():
    yes_or_no = input ("Would you like to print a receipt? (Y or N) : ")
    if "Y" or "y":
        order_number = receipt_file_name
        #Order_number is whatever the UPC is (might have to change) 
        receipt = open (receipt_file_name.txt, "w")
        receipt.write(data)
        # Change data to whatever we name the UPC file return info
        receipt.close()
        
    else:
        print ("No Receipt")
        
# ONLINE ORDER FUNCTIONS

# UPDATE CATALOG FUNCTIONS
        
# TERMINATE PROGRAM FUNCTION
def terminate_program():
    exit()
    
