cart = []
while True:
    print("\nCASHREG MAIN MENU")
    print("1 - Add an item")
    print("2 - Checkout")
    print("3 - Remove an item")
    print("4 - Exit")
    userinput = input("Choose an option: ").strip()
    if userinput == "1":
        itemname = input("Enter the name of the item: ").strip()
        itemprice = input("Enter the price of the item: ").strip()
        try:
            float(itemprice)
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue
        cart.append((itemname, itemprice))
        print("Item added to cart.")
    elif userinput == "2":
        if not cart:
            print("Cart is empty. Add items before checkout.")
            continue
        total = sum(float(price) for name, price in cart)
        print("\nReceipt:")
        for name, price in cart:
            print(f"- {name}: ${float(price):.2f}")
        print(f"Total: ${total:.2f}")
        cart.clear()
        print("Checkout complete. Cart has been cleared.")
    elif userinput == "3":
        if not cart:
            print("Cart is empty. Nothing to remove.")
            continue
        itemname_to_remove = input("Enter the name of the item to remove: ").strip()
        new_cart = [(name, price) for name, price in cart if name != itemname_to_remove]
        if len(new_cart) == len(cart):
            print("Item not found in cart.")
        else:
            cart = new_cart
            print("Item removed from cart.")

    elif userinput == "4":
        print("exit.")
        break
    else:
        print("Error.")