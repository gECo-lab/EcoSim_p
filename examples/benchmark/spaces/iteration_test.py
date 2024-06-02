demand = {"item1": 5, "item2": 3, "item3": 2}
offers = {"item1": 10, "item2": 4, "item3": 6, "item4": 8}

for item, quantity in demand.items():
    if item in offers:
        if quantity <= offers[item]:
            print(f"Offering {quantity} of {item}")
            offers[item] -= quantity
        else:
            print(f"Offering {offers[item]} of {item}")
            offers[item] = 0
    else:
        print(f"No offer available for {item}")

print("Remaining offers:")
for item, quantity in offers.items():
    print(f"{item}: {quantity}")