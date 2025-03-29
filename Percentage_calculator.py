# Percentage calculator using python

def calculate_percentage_of_number(value, percentage):
    """Calculates the percentage of a number."""
    return (value * percentage) / 100

def calculate_percentage_relation(part, whole):
    """Finds what percentage one number is of another."""
    if whole != 0:
        return (part / whole) * 100
    else:
        return "Error: Cannot divide by zero."

def increase_by_percentage(value, percentage):
    """Increases a number by a given percentage."""
    return value * (1 + percentage / 100)

def decrease_by_percentage(value, percentage):
    """Decreases a number by a given percentage."""
    return value * (1 - percentage / 100)

def menu():
    """Displays the menu options."""
    print("\n✅ Percentage Calculator Menu ✅")
    print("1. Find the percentage of a number")
    print("2. Find what percentage one number is of another")
    print("3. Increase a number by a percentage")
    print("4. Decrease a number by a percentage")
    print("0. Exit")

# Main program loop
while True:
    menu()
    choice = input("\nEnter the operation number (0 to Exit): ")

    if choice == "0":
        print("Exiting the program. Goodbye! 👋")
        break

    elif choice == "1":
        value = float(input("Enter the number: "))
        percentage = float(input("Enter the percentage: "))
        print(f"{percentage}% of {value} is {calculate_percentage_of_number(value, percentage):.2f}")

    elif choice == "2":
        part = float(input("Enter the part: "))
        whole = float(input("Enter the whole: "))
        result = calculate_percentage_relation(part, whole)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{part} is {result:.2f}% of {whole}")

    elif choice == "3":
        value = float(input("Enter the number: "))
        percentage = float(input("Enter the percentage to increase by: "))
        print(f"{value} increased by {percentage}% is {increase_by_percentage(value, percentage):.2f}")

    elif choice == "4":
        value = float(input("Enter the number: "))
        percentage = float(input("Enter the percentage to decrease by: "))
        print(f"{value} decreased by {percentage}% is {decrease_by_percentage(value, percentage):.2f}")

    else:
        print("Invalid choice. Please select a valid option.")

    print("\n" + "="*40)
