def calculation(num1, num2, action): # def for the calculation to be conducted.
    if action == "+":
        return num1 + num2
    
    elif action == "-":
        return num1 - num2
    
    elif action == "*":
        return num1 * num2
    
    elif action == "/":
        return num1 / num2

while True: # While loop for the 3 options below. 
    print("Option 1: Use calculator\n"
        "Option 2: View previous calculations\n"
        "Option 3: Exit\n")

    user_choice = input("Please select an option (1, 2 or 3): \n") # User input to perform one of the three options.

    if user_choice == "1": # If option 1 is selected then the user will have to input the 2 numbers and then the calculation action.
        try:
            num1 = int(input("Enter the first number (e.g 12): ")) # Rather number as variable
            num2 = int(input("Enter the second number (e.g 8): "))
            action = input("Enter the calculation symbol (+, -, *, or /): \n")
            if action not in ["+", "-", "*", "/"]:
                    print("Make sure to select either +, -, *, or /")
                    continue

            result = calculation(num1, num2, action)
            print()
            print(f"{num1} {action} {num2} = {result}")
            print()

            with open("equations.txt", "a") as equations_file: # Writing the calculation to the selected text file.
                equations_file.write(f"{num1} {action} {num2} = {result}\n")

        except Exception:
            print("Please make sure to follow the instructions.")

    elif user_choice == "2": # If option two is selected then the text file will be read en printed out for the user.
        try:
            with open("equations.txt", "r") as equations_file:
                old_equations = equations_file.readlines()
                if old_equations:
                    print("Calculation history:\n")
                    for equation in old_equations:
                        print(equation.strip())
                else:        
                    print("You haven't done any equations yet.")

        except FileNotFoundError as error:
            print("The file that you are trying to open does not exist.")
            print(error) 

    elif user_choice == "3": # Option 3 to exit the app.
        print("The calculator has been closed.")
        break

    else:
        print("Make sure to enter 1, 2 or 3.")


# Headline comment