class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers."""
        return a * b

    def divide(self, a, b):
        """Divides two numbers."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

def main():
    """Main function for the calculator program."""
    calc = Calculator()  # Create a Calculator object

    while True:  # Main loop for calculations
        try:
            num1 = float(input("Enter first number: "))  # Get first number
            num2 = float(input("Enter second number: "))  # Get second number
            operation = input("Choose operation (+, -, *, /): ")  # Get operation

            if operation == "+":  # Addition
                result = calc.add(num1, num2)
            elif operation == "-":  # Subtraction
                result = calc.subtract(num1, num2)
            elif operation == "*":  # Multiplication
                result = calc.multiply(num1, num2)
            elif operation == "/":  # Division
                result = calc.divide(num1, num2)
            else:
                print("Invalid operation. Please try again.")  # Invalid operation
                continue  # Go back to the beginning of the loop

            print(f"Result: {num1} {operation} {num2} = {result}")  # Print the result

        except ValueError:  # Handle invalid input (non-numerical)
            print("Invalid input. Please enter numerical values.")
        except ZeroDivisionError as e:  # Handle division by zero
            print(e)

        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()  # Ask for another calculation
        if another != "yes":  # If user doesn't want to continue
            print("Goodbye!")
            break  # Exit the loop

if __name__ == "__main__":
    main()  # Run the main function