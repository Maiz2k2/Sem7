def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['value-to-weight'] = item['value'] / item['weight']

    # Sort items in descending order of value-to-weight ratio
    items.sort(key=lambda x: x['value-to-weight'], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if item['weight'] <= capacity:
            total_value += item['value']
            knapsack.append(item)
            capacity -= item['weight']
        else:
            fraction = capacity / item['weight']
            total_value += item['value'] * fraction
            knapsack.append({'item': item['item'], 'weight': capacity, 'value': item['value'] * fraction})
            break

    return total_value, knapsack

# Input from the user
n = int(input("Enter the number of items: "))
capacity = int(input("Enter the knapsack capacity: "))

items = []
for i in range(n):
    item = input(f"Enter item {i+1} (value weight): ").split()
    items.append({'item': i + 1, 'value': float(item[0]), 'weight': float(item[1])})

max_value, knapsack = fractional_knapsack(items, capacity)

print("Maximum value:", max_value)
print("Items in the knapsack:")
for item in knapsack:
    print(f"Item {item['item']}: Weight = {item['weight']}, Value = {item['value']}")

