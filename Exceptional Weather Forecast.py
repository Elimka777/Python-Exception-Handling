#Task 1: Start
#Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.
#Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

#Task 2: Temperature Conversion
#Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
#Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

#Task 3: User Experience
#Implement an else block that prints the converted temperature in a user-friendly format.
#Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
def numeric():
    while True:
        try:
            digit_input = float(input('Enter the temperature in Fahrenheit: '))
            return digit_input
        except ValueError:
            print("Oh no! That doesn't look like a number. Please try again:")

def temp_conversion():
    try:
        # Call the numeric function and store the result in num
        num = numeric()
        print(f"Thank you! You entered the temperature {num}°F.")

        # Convert Fahrenheit to Celsius
        conversion = (num - 32) * 5 / 9  
    except Exception as e:
        print(f"An error occurred during the conversion: {e}")
    else:
        print(f"The temperature in Celsius is: {conversion:.2f}°C.")
    finally:
        print("Thank you for using the weather forecast application.")

temp_conversion()