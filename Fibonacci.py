import timeit

def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        prev_sequence = fibonacci_recursive(n - 1)
        prev_sequence.append(prev_sequence[-1] + prev_sequence[-2])
        return prev_sequence

def main():
    n = int(input("Enter the value of n: "))

    # Calculate and display Fibonacci numbers for non-recursive method
    time_iterative = timeit.timeit(lambda: fibonacci_iterative(n), number=1000)
    result_iterative = fibonacci_iterative(n)

    print(f"Fibonacci numbers up to Fibonacci({n}) using iterative method: {result_iterative}")
    print(f"Time taken to calculate Fibonacci numbers using iterative method (average of 1000 runs): {time_iterative:.6f} seconds")

    # Calculate and display Fibonacci numbers for recursive method
    time_recursive = timeit.timeit(lambda: fibonacci_recursive(n), number=1000)
    result_recursive = fibonacci_recursive(n)

    print(f"Fibonacci numbers up to Fibonacci({n}) using recursive method: {result_recursive}")
    print(f"Time taken to calculate Fibonacci numbers using recursive method (average of 1000 runs): {time_recursive:.6f} seconds")

if __name__ == "__main__":
    main()
