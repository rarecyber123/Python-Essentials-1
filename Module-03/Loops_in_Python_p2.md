
# range(start, stop)

> Python start integer se ginti shuru karta hai aur stop - 1 par khatam kar deta hai (yani stop wala number include nahi hota).

## Code Example:

    for i in range(2, 6):
       print(i)

### Output 

    2
    3
    4
    5

- Start = 2: Ginti 2 se shuru hui.

- Stop = 6: Ginti 6 se pehle (yani 5 par) ruk gayi.

  ---

# range(start, stop, step)

# for loop aur range() ke 3 parameters

> Pehle humne dekha ke range() start aur stop ke sath kaise kaam karta hai, lekin isme ek teesa parameter bhi hota hai: step (increment/decrement).

- Formula: range(start, stop, step)

- Kaise kaam karta hai:

    - Start: Kahan se ginti shuru karni hai (default 0).

    - Stop: Kahan tak jana hai (is number se pehle ruk jata hai).

    - Step: Har dafa kitne numbers ka jump lena hai (default 1).

### Example:

    # 2 se shuru karo, 10 se pehle ruko, aur 2, 2 ka jump lo
    for i in range(2, 10, 2):
    print(i)

### Output: 2, 4, 6, 8
---

# break aur continue statements

> Kabhi kabhi humein loop ko uski normal condition se pehle roknay ya kisi specific turn ko skip karne ki zaroorat hoti hai.

- ### break (Emergency Stop):

  Jaise hi break chalta hai, loop foren khatam ho jata hai aur program loop ke bahar nikal aata hai.

- ### continue (Skip & Move Next):

  Yeh chalay hue current step ko adha chhod kar agli iteration (turn) par chala jata hai.

## Example:

    # break example
    for i in range(1, 6):
    if i == 3:
        break # 3 par pohnchte hi loop khatam
    print(i) # Output: 1, 2

    # continue example
    for i in range(1, 6):
    if i == 3:
        continue # 3 ko skip kar do
    print(i) # Output: 1, 2, 4, 5

---

# Stuck in a Loop (break)

> Is lab mein ek endless loop (while True) banana hota hai jo user se baar baar word maangta hai jab tak user sahi secret word "chupacabra" enter na kar de.

## Example Code

    while True:
    word = input("Secret word enter karo: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break # Secret word milte hi infinite loop se exit!

---

# The Ugly Vowel Eater (continue)

> Is lab ka maksad continue statement ki practice hai. User ek word enter karta hai, program har character ko uppercase mein convert karta hai, aur agar koi vowel (A, E, I, O, U) aata hai to use skip kar deta hai.

## Example Code

    user_word = input("Enter a word: ").upper()

    for letter in user_word:
    if letter in "AEIOU":
        continue # Vowel mila, to print kiye bina agle letter par jao
    print(letter)

## Example Output:

Agar user "PYTHON" likhta hai, to output hoga: P, Y, T, H, N (O skip ho gaya).

---







