import time

# Decorator function to measure the execution time of a function
def measure_time(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# Generator function to generate Fibonacci series
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Decorate the Fibonacci generator function to measure its execution time
fibonacci_generator = measure_time(fibonacci_generator)

# Main function to test the Fibonacci generator
def main():
    n = int(input("Enter the number of terms in Fibonacci series: "))
    fib_series = list(fibonacci_generator(n))
    print("Fibonacci series:", fib_series)

if __name__ == "__main__":
    main()
