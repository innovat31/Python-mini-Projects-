# For basic mathematical operations with a single digit input
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def exponentiate(base, exp):
    return base ** exp

def modulus(a, b):
    return a % b

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    return math.factorial(n)

# Menu for operations
def menu():
    print("\n✅ Basic Math Operations Menu ✅")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulus")
    print("7. Factorial")
    print("0. Exit")

# Main program loop
while True:
    menu()
    choice = input("\nEnter the operation number (0 to Exit): ")

    if choice == "0":
        print("Exiting the program. Goodbye! 👋")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")
        elif choice == "5":
            print(f"Result: {exponentiate(a, b)}")
        elif choice == "6":
            print(f"Result: {modulus(a, b)}")

    elif choice == "7":
        n = int(input("Enter a non-negative integer for factorial: "))
        print(f"Result: {factorial(n)}")

    else:
        print("Invalid choice. Please select a valid option.")

    print("\n" + "="*40)
