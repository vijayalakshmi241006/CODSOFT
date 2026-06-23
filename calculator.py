def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("=" * 30)
    print("    CODSOFT SIMPLE CALCULATOR    ")
    print("=" * 30)
    
    while True:
        try:
            # Input numbers
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue

        print("\nChoose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == '1':
            print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid operation choice.")

        # Ask to play/calculate again
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes' and again != 'y':
            print("\nThank you for using the CodSoft Calculator! Goodbye.")
            break

if __name__ == "__main__":
    calculator()
