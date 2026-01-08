def sell_product(inventory, product, quantity):
    # Check if product exists
    if product not in inventory:
        return "Product not found"

    # Check stock availability
    if inventory[product]["stock"] < quantity:
        return "Insufficient stock"

    # Reduce stock
    inventory[product]["stock"] -= quantity
    return "Sale successful"


def total_inventory_value(inventory):
    total_value = 0
    for item in inventory.values():
        total_value += item["price"] * item["stock"]
    return total_value


def low_stock_items(inventory, threshold=10):
    low_stock = []
    for product, details in inventory.items():
        if details["stock"] < threshold:
            low_stock.append(product)
    return low_stock
inventory = {
    "Laptop": {"price": 60000, "stock": 5},
    "Mouse": {"price": 500, "stock": 50},
    "Keyboard": {"price": 1500, "stock": 20}
}

print(sell_product(inventory, "Laptop", 2))
print(sell_product(inventory, "Laptop", 10))

print("Total Inventory Value:", total_inventory_value(inventory))
print("Low Stock Items:", low_stock_items(inventory))
