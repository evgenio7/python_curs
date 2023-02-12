def calculate_profit(invoice_items):
    profit = 0
    for item in invoice_items:
        profit += item[2] * item[3]
    return profit

invoice_items = [
    (1, 1, 5, 10),
    (2, 2, 3, 20),
    (3, 3, 2, 30),
    (4, 4, 1, 40)
]

print("Total profit: ", calculate_profit(invoice_items))

def repeated_first_names(customers):
    first_names = {}
    for customer in customers:
        if customer[1] in first_names:
            first_names[customer[1]] += 1
        else:
            first_names[customer[1]] = 1
    repeated_names = {k: v for k, v in first_names.items() if v > 1}
    return repeated_names

customers = [
    (1, "John", "Doe", 20),
    (2, "Jessica", "Smith", 30),
    (3, "John", "Doe", 40),
    (4, "Jessica", "Smith", 50),
    (5, "Jessica", "Brown", 60)
]

print("Repeated first names: ", repeated_first_names(customers))
