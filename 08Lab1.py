# inventory_Surname.py
# Demonstrating parameter-passing methods in Python

def add_to_stock(stock_list):
    """
    Function 1: Modifies the original list (pass-by-reference behavior)
    Adds a fixed quantity (75) to the inventory stock list
    """
    print("\n=== Running add_to_stock() ===")
    stock_list.append(75)  # Modifies the original list
    print(f"Inside function (stock): {stock_list}")

def update_price(price):
    """
    Function 2: Doesn't modify original variable (pass-by-value behavior)
    Calculates a 10% price markup but doesn't change the original price
    """
    print("\n=== Running update_price() ===")
    new_price = price + (price * 0.10)
    print(f"Inside function (price): {new_price}")

def main():
    # Function 1 demonstration - list modification
    inventory = [100, 200, 150]
    print(f"Original inventory: {inventory}")
    add_to_stock(inventory)
    print(f"Outside function (stock): {inventory}")
    
    # Function 2 demonstration - price calculation
    base_price = 250.0
    print(f"\nOriginal price: {base_price}")
    update_price(base_price)
    print(f"Outside function (price): {base_price}")

if __name__ == "__main__":
    main()