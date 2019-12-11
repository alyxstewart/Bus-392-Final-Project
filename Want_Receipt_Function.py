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
    
        
        

        
