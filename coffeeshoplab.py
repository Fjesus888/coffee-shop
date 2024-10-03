# Coffee and Muffin Shop Simulator

def main():
    # Prices
    coffee_price = 5.00
    muffin_price = 4.00
    tax_rate = 0.06

    # User input
    print("***************************************")
    print("My Coffee and Muffin Shop")
    coffees = int(input("Number of coffees bought?\n"))
    muffins = int(input("Number of muffins bought?\n"))
    print("***************************************")

    # Calculations
    subtotal_coffee = coffees * coffee_price
    subtotal_muffin = muffins * muffin_price
    subtotal = subtotal_coffee + subtotal_muffin
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{coffees} Coffee{'s' if coffees != 1 else ''} at ${coffee_price} each: $ {subtotal_coffee:.2f}")
    print(f"{muffins} Muffin{'s' if muffins != 1 else ''} at ${muffin_price} each: $ {subtotal_muffin:.2f}")
    print(f"6% tax: $ {tax:.2f}")
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************")

# Run the program
if __name__ == "__main__":
    main()
