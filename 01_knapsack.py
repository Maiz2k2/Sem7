def knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    items_in_knapsack = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_in_knapsack.append(i - 1)
            w -= weights[i - 1]

    return max_value, items_in_knapsack

# Input from the user
n = int(input("Enter the number of items: "))
capacity = int(input("Enter the knapsack capacity: "))

values = []
weights = []
for i in range(n):
    value, weight = map(int, input(f"Enter value and weight for item {i + 1}: ").split())
    values.append(value)
    weights.append(weight)

max_value, items_in_knapsack = knapsack_dp(values, weights, capacity)

print("Maximum value:", max_value)
print("Items in the knapsack:")
for item in items_in_knapsack:
    print(f"Item {item + 1}: Value = {values[item]}, Weight = {weights[item]}")

