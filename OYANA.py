# Simple Calculator for Addition and Multiplication

def add(num1, num2):
    """Add two numbers"""
    return num1 + num2


def multiply(num1, num2):
    """Multiply two numbers"""
    return num1 * num2


def main():
    print("=== Simple Calculator ===\n")
    
    # Get input from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform operations
        addition_result = add(num1, num2)
        multiplication_result = multiply(num1, num2)
        
        # Display results
        print(f"\n{num1} + {num2} = {addition_result}")
        print(f"{num1} × {num2} = {multiplication_result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == "__main__":
    main()
 