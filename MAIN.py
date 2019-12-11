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

# Prompt user to see if they want a printed receipt
def want_receipt (receipt):
    yes_or_no = input ("Would you like to print a receipt? (Y or N) : ")
    if "Y" or "y":
        print receipt
