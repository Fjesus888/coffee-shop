# Coffee and Muffin Shop Simulator

def main():
    # Prices
    coffee_price = 5.00
    muffin_price = 4.00
    tax_rate = 0.06

   # Coffee and Muffin Shop Simulator

def main():
    # Prices
    coffee_price = 5.00
    muffin_price = 4.00
    tea_price = 3.00
    cookie_price = 2.00
    tax_rate = 0.06

    # User input
    print("***************************************")
    print("Welcome to My Coffee and Muffin Shop!")
    coffees = int(input("Number of coffees bought?\n"))
    muffins = int(input("Number of muffins bought?\n"))
    teas = int(input("Number of teas bought?\n"))
    cookies = int(input("Number of cookies bought?\n"))
    print("***************************************")

    # Calculations
    subtotal_coffee = coffees * coffee_price
    subtotal_muffin = muffins * muffin_price
    subtotal_tea = teas * tea_price
    subtotal_cookie = cookies * cookie_price
    subtotal = subtotal_coffee + subtotal_muffin + subtotal_tea + subtotal_cookie
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{coffees} Coffee{'s' if coffees != 1 else ''} at ${coffee_price} each: $ {subtotal_coffee:.2f}")
    print(f"{muffins} Muffin{'s' if muffins != 1 else ''} at ${muffin_price} each: $ {subtotal_muffin:.2f}")
    print(f"{teas} Tea{'s' if teas != 1 else ''} at ${tea_price} each: $ {subtotal_tea:.2f}")
    print(f"{cookies} Cookie{'s' if cookies != 1 else ''} at ${cookie_price} each: $ {subtotal_cookie:.2f}")
    print(f"6% tax: $ {tax:.2f}")
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************")
    
    # Thank you message
    print("Thank you for visiting My Coffee and Muffin Shop! We hope to see you again!")

# Run the program
if __name__ == "__main__":
    main()
