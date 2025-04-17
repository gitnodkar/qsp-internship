items = {"apple": 30, "banana": 10, "milk": 50}
cart = []

def add_to_cart(item):
    if item in items:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item not available.")

def checkout():
    total = sum(items[i] for i in cart)
    print("Items:", cart)
    print("Total:", total)

while True:
    print("Items Available:", list(items.keys()))
    ch = input("1. Add item 2. Checkout 3. Exit: ")
    if ch == "1":
        item = input("Enter item: ")
        add_to_cart(item)
    elif ch == "2":
        checkout()
        break
    else:
        break
