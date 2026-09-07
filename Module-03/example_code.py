# Example 1 
# Even/Odd Counter - Stop at 0

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

---
# Example 2
# Guess the secret number
# Scenario:
# Ek magician ne secret number 777 chhupa rakha hai. User se number input lena hai while loop use karte hue.
# Jab tak galat guess karega, loop chalta rahega. Sahi guess par free hoga!

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""
)

user_guess = int(input("Enter the secret number: "))

while user_guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_guess = int(input("Enter the secret number again: "))

print(user_guess)
print("Well done, muggle! You are free now.")

---
