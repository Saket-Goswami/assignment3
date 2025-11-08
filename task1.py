# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Taking user input
num = int(input("Enter a number: "))

# Calling the factorial function
fact = factorial(num)

# Displaying the result
print(f"\nFactorial of {num} is: {fact}")
