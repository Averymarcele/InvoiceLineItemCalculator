#Invoice Line Item Calculator

def get_price():
    while True:
        try:
            price = float(input("Enter a price: "))
            return price
        except ValueError:
            print("Invalid price. Please try again.")
            
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter a quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity. Please try again.")
            
if __name__ =="__main__":
    print("Welcome to the Invoice Line Item Calculator")
    
    answer = "y"
    while answer.lower() == "y":
        price = get_price()
        quantity = get_quantity()
        
        total = price * quantity
        
        print()
        print("Price:    ", f"{price: .2f}")
        print("Quantity: ", quantity)
        print("Total:    ", f"{total: .2f}")
        answer = input("Enter another long item? (y/n): ")
        print()

    print("Bye!")