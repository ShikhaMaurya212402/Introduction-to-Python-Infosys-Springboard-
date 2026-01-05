transactions = [
    {"id": 1, "amount": 500, "location": "Chennai"},
    {"id": 2, "amount": 45000, "location": "Delhi"},
    {"id": 3, "amount": 52000, "location": "Chennai"},
    {"id": 4, "amount": 200, "location": "Coimbatore"}
]

suspicious_transactions = []

# Rule 1: Amount greater than 50,000
for tx in transactions:
    if tx["amount"] > 50000:
        suspicious_transactions.append(tx)

# Rule 2: Same user, multiple locations (simulated short time)
locations = set(tx["location"] for tx in transactions)

if len(locations) > 1:
    for tx in transactions:
        if tx not in suspicious_transactions:
            suspicious_transactions.append(tx)

# Output
print("Suspicious Transactions:")
for tx in suspicious_transactions:
    print(tx)
