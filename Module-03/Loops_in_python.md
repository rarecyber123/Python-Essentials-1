
# While loop 

> Concept:
   > Real life mein hum kehte hain na "jab tak yeh kaam khatam nahi hota, karte raho", while loop bilkul waise hi kaam karta hai. Yeh kisi code block ko tab tak baar baar execute karta rehta hai jab tak di gayi condition True rehti hai.

- Rule: Agar condition shuru mein hi False ho jaye, toh loop ke andar ka code ek baar bhi nahi chalega.

- Indentation: Code block ko indent (space) dena zaroori hai.


  ## Syntax Sketch:

      while conditional_expression:
          instruction_one
          instruction_two
---
# An infinite loop

> Concept:
 > Agar aapki condition HAMESHA True hi rahe gi aur kabhi badle gi nahi, toh loop kabhi rukega nahi. Isko Infinite Loop ya endless loop kehte hain.

## How to stop?

Isko terminate karne ke liye terminal/console mein Ctrl-C press karte hain (jis se KeyboardInterrupt exception aati hai).

## Example 1

    while True:
    print("I'm stuck inside a loop.")

## Example 2

    # Store the current largest number here.
    largest_number = -999999999

    # Input the first value.
    number = int(input("Enter a number or type -1 to stop: "))

    # If the number is not equal to -1, continue.
    while number != -1:
     # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

    # Print the largest number.
    print("The largest number is:", largest_number)

---

# While Loop Practical Tricks 

- ### 1. Truth Value Shortcut: Python mein non-zero numbers ko True aur 0 ko False mana jata hai.

    - while number != 0: ko short mein while number: likh sakte hain.

    - if number % 2 == 1: ko if number % 2: likh sakte hain.

- ### 2. Counter Variable: Loop ko ek specific number of times chalane ke liye counter subtract ya add karte hain.

---

# Looping Code with For 

> Concept:
   > Agar aapko pehle se pata ho ke loop kitni baar chalana hai (maslan exact 10 ya 100 baar), toh while se counting sambhalna thoda boring aur lengthy ho jata hai. Wahan hum for loop aur range() function ka use karte hain.

- range(10): 0 se shuru karega aur 9 tak chalega (total 10 steps, upper bound include nahi hota).

- range(2, 8): 2 se shuru karega aur 7 tak chalega.

- pass keyword: Ek empty instruction hai jo tab use karte hain jab syntax ko body chahiye hoti hai par hume koi code nahi chalana hota.

#  Example 1 (Basic range()):

      for i in range(10):
    print("The value of i is currently", i)

# Example 2 (Start and Stop arguments):

      for i in range(2, 8):
    print("The value of i is currently", i)

---
