#Function to prompt user to see if they want a printed receipt

def want_receipt (receipt):
    yes_or_no = input ("Would you like to print a receipt? (Y or N) : ")
    if "Y" or "y":
        print receipt

        
