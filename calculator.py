print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("SUM:", num1 + num2)
    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("DIFF:", num1 - num2)
    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("PRODUCT:", num1 * num2)
    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0 or num1 == 0:
            print("Error! Division by zero.")
        else:
            print("DIV:", num1 / num2)
    else:
        print("Enter valid option")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'y':
        break
print("THANKS FOR USING CALCULATOR")
