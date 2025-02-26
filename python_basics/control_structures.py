# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Ask the user for an integer input
user_input = int(input("Enter an integer: "))

# Check if the input number is even or odd using the function
result = check_even_odd(user_input)
print(f"The number {user_input} is {result}.")

# Generate a list of even numbers from 1 to 50 using a for loop
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("List of even numbers from 1 to 50:", even_numbers)

# Print numbers from 10 down to 1 in reverse order using a while loop
counter = 10
while counter > 0:
    print(counter)
    counter -= 1
