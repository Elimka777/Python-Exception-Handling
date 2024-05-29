#Task 1: Start
#Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
#Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.
def recipe():
    while True:
     try:
        original=float(input("Enter the number of servings the recipe is originally for: ")) 
        your_wish=float(input("Enter the number of servings they wish to make: "))
        return original, your_wish
     except ValueError:
         print("Oops! Please enter only digits.")
original_servings, desired_servings = recipe()
print(f"Original servings: {original_servings}, Desired servings: {desired_servings}")

#Task 2: Quantity Calculation
#Calculate the adjustment factor by dividing the desired servings by the original servings.
#Use a try block to catch any arithmetic errors that may occur during the calculation.

#Task 3: Serving Success
#If the calculation is successful, display the adjusted recipe quantities to the user.
#Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

def calculate():
        try:
            adjustment = desired_servings/original_servings
        except ArithmeticError as e: 
            print(f"Cannot adjust recipe: {e}")
            
        else:
            print(f"The calculation is successful! The adjusted recipe quantity is {adjustment:.2f}")
        finally:
            print("Thank you for using the recipe ratio adjuster application.")
calculate()