
# 1. input() Function: 

- Purpose: Program ko wait karwata hai jab tak user keyboard se kuch type karke Enter na daba de.

- Result: User jo bhi type karta hai, input() usko return kar deta hai. Us data ko safe rakhne ke liye variable mein assign karna zaroori hai.

- Prompt Argument: Aap input("Enter your name: ") ki tarah brackets ke andar seedha message likh sakte hain, alag se print() likhne ki zaroorat nahi hoti.

  ---
# 2. Type Casting (Data Convert Karna)

- Sab se Badi Baat: input() function hamesha String (str) return karta hai, chahe aap number hi kyun na type karein.

- Problem: Agar aap string ko kisi mathematical operation (jaise **, /) mein use karenge, to Python TypeError dega.

- Solution: String ko numbers mein convert karne ke liye ye functions use karein:

- int() – Whole numbers (1, 2, 10) ke liye.

- float() – Decimal numbers (1.5, 3.14) ke liye.

### Example: age = int(input("Enter age: "))

---
# 3. String Operators ( + aur + )

In operators ke normal math ke alawa doosre kaam bhi hain:

### Concatenation (+): 

- Do strings ko aapas mein jodne ke liye.

- Example: "Hello " + "World" $\rightarrow$ ## "Hello World"

- Rule: Dono sides par string honi chahiye. String + Number error dega.

### Replication (*):

- Kisi string ko multiple times repeat karne ke liye.

- Example: "Hi" * 3 $\rightarrow$ ## "HiHiHi"

- Rule: Ek side string aur doosri side integer hona chahiye. Agar number $\le 0$ ho to empty string milti hai.
 
    ---
# 4. str() Function: 

- Numbers ko String BananaAgar aap kisi number ko string mein convert karna chahte hain taake use doosri strings ke sath concatenate kar sakein, to str() use hota hai.

- Example: "Your total is " + str(50) $\rightarrow$ "Your total is 50"
