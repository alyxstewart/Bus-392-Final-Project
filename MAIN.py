# BUS 392 Final Project
# Adam Watson and Alyx Stewart


import csv
import sys
import datetime

def main():
    print("                         UPC Reader                               ")
    print("------------------------------------------------------------------")
   

         
            


    
    
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

#Function to prompt user to see if they want a printed receipt

def want_receipt (receipt):
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
