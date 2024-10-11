class Factorial:
    def __init__(self, n):
        self.n = n

    def calculate_factorial(self):
        if self.n == 0:
            return 1
        else:
            return self.n * Factorial(self.n-1).calculate_factorial()

# Create an instance of the Factorial class
factorial_obj = Factorial(5)

# Calculate the factorial
result = factorial_obj.calculate_factorial()

print(f"The factorial of 5 is: {result}")
