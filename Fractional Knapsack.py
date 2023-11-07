import time

def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    value_index = sorted(index, key=lambda i: value[i] / weight[i], reverse=True)
    max_value = 0
    fractions = [0] * len(value)

    for i in value_index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions

def main():
    start_time = time.time()
    n = int(input("Enter number of items: "))
    value = list(map(int, input("Enter value of each item: ").strip().split()))
    weight = list(map(int, input("Enter weight of each item: ").strip().split()))
    capacity = int(input("Enter knapsack capacity: "))

    max_value, fractions = fractional_knapsack(value, weight, capacity)
    end_time = time.time()

    print("Total profit obtained: ", max_value)
    selected_items = []
    for i in range(n):
        if fractions[i] != 0:
            selected_items.append((i + 1, weight[i], value[i], fractions[i]))
        else:
            print("Rejected item", i + 1, "with weight", weight[i], ", profit", value[i], ", and fraction", fractions[i])

    for item in selected_items:
        print("Selected item", item[0], "with weight", item[1], ", profit", item[2], ", and fraction", item[3])

    print("Total execution time of the fractional knapsack: ", end_time - start_time)

if __name__ == "__main__":
    main()