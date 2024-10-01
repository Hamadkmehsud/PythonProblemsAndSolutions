# Function to generate and print the Fibonacci series up to 'num' terms
def fibonacci_series(num):
    n = 0  # First Fibonacci number
    m = 1  # Second Fibonacci number
    if num < 1:
        print(n)  # If num is 0 or less, just print 0 (or an empty sequence)
    elif num == 1:
        print(n)  # If num is 1, print only the first Fibonacci number (0)
    else:
        print(n, m, end=' ')  # Print the first two numbers, 0 and 1, on the same line
        for i in range(2, num):  # Start from 2 because 0 and 1 are already printed
            o = m
            m = m + n  # Update m to the next Fibonacci number
            n = o  # Update n to the previous Fibonacci number
            print(m, end=' ')  # Print the next Fibonacci number on the same line
# Get user input for the number of Fibonacci terms
input_user = int(input('Enter how many Fibonacci numbers to generate: '))
fibonacci_series(input_user)
print()
def fibonacci(n):
    if n <= 0:
        return 0  # Base case: Fibonacci of 0 is 0
    elif n == 1:
        return 1  # Base case: Fibonacci of 1 is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
# Function to generate and print Fibonacci series up to 'num' terms
def fibonacci_series(num):
    for i in range(num):
        print(fibonacci(i), end=' ')  # Print Fibonacci numbers on the same line
# Get user input for the number of Fibonacci terms
input_user = int(input('Enter how many Fibonacci numbers to generate: '))
# Call the Fibonacci function with user input
fibonacci_series(input_user)