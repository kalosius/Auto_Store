def get_customer_info():
    customer_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    town_code = input("Enter town code (KLA, EBB, MBR, or others): ")
    customer_type = input("Enter customer type (ret or who): ")
    return customer_id, name, town_code, customer_type

def get_part_ordered_details():
    partner_number = input("Enter partner number: ")
    description = input("Enter description: ")
    price_per_part = input("Enter price per part: ")
    quantity = input("Enter quantity: ")
    oversize_order = input("Oversize order? (yes or no): ")
    return partner_number, description, price_per_part, quantity, oversize_order

def calculate_cost(price_per_part, quantity):
    cost = round(float(price_per_part) * int(quantity), 2)
    return cost

def calculate_sales_tax(town_code, customer_type):
    if customer_type == "ret":
        if town_code == "KLA":
            sales_tax = 0.1
        elif town_code == "EBB" or town_code == "MBR":
            sales_tax = 0.05
        else:
            sales_tax = 0
    elif customer_type == "who":
        sales_tax = 0
    return sales_tax

def calculate_shipping_cost(quantity, shipping_method):
    if shipping_method == "UPS":
        shipping_charge = 7
    elif shipping_method == "PostalAir":
        shipping_charge = 8.5
    elif shipping_method == "FedExGround":
        shipping_charge = 9.25
    elif shipping_method == "FedExOvernight":
        shipping_charge = 12
    shipping_cost = round(float(shipping_charge) * int(quantity), 2)
    return shipping_cost

def calculate_total_cost(cost, sales_tax, shipping_cost):
    total_cost = round(cost * (1 + sales_tax) + shipping_cost, 2)
    return total_cost

customer_id, name, town_code, customer_type = get_customer_info()
partner_number, description, price_per_part, quantity, oversize_order = get_part_ordered_details()
cost = calculate_cost(price_per_part, quantity)
sales_tax = calculate_sales_tax(town_code, customer_type)
shipping_cost = calculate_shipping_cost(quantity, "UPS")
total_cost = calculate_total_cost(cost, sales_tax, shipping_cost)

with open("order.txt", "w") as file:
    file.write("Customer ID: " + customer_id + "\n")
    file.write("Name: " + name + "\n")
    file.write("Town code: " + town_code + "\n")
    file.write("Customer type: " + customer_type + "\n")
    file.write("Partner number: " + partner_number + "\n")
    file.write("Description: " + description + "\n")
    file.write("Price per part: " + price_per_part + "\n")
    file.write("Quantity: " + quantity + "\n")
    file.write("Oversize order: " + oversize_order + "\n")
    file.write("Cost: $" + str(cost) + "\n")
    file.write("Sales tax: " + str(sales_tax) + "\n")
    file.write("Shipping cost: $" + str(shipping_cost) + "\n")
    file.write("Total cost: $" + str(total_cost) + "\n")

