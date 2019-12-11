
#Import date&time to add timestamp to order number
import datetime

#Create order function that takes scanned UPC as an argument
def create_order_number (order_number):
    
    # Create time stamp    
    today = datetime.date.today()

    # Formate date
    date = today.strftime("%m%d%Y")
    
    # Varible to hold order number (combion count and date)
    unique_order_number = date + "-" + order_number
    return unique_order_number




    
