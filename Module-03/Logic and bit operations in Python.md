
# Logical Operators

> Logical operators evaluate whole conditions rather than individual bits. Zero is treated as False, and any non-zero value is treated as True.

- ### and (Conjunction): Returns True only when both conditions are true.

    - Example: counter > 0 and value == 100

- ### or (Disjunction): Returns True if at least one condition is true.

    - Example: (x == y) or not (x == y)

- ### not (Unary Negation): Flips True to False and False to True.

     - Example: not (var <= 0)
 
---
# De Morgan’s Laws

These laws help simplify inverted logical expressions:

- not (p and q) == (not p) or (not q)

- not (p or q) == (not p) and (not q)
---

# Bitwise Operators

Bitwise operators modify individual bits of integer values (they do not work on floats).

- ### & (Bitwise AND): Returns 1 only if both bits are 1.

  - Example: 15 & 22 gives 6

- ### | (Bitwise OR): Returns 1 if at least one bit is 1.

  - Example: x = 4, y = 1 $\rightarrow$ x | y gives 5

-### ^ (Bitwise XOR): Returns 1 if exactly one bit is 1 (exclusive choice).

  - Example: x = 4 $\rightarrow$ x ^ 5 gives 1
    
- ### ~ (Bitwise NOT): Inverts all bits (bitwise complement).

  - Example: ~4 gives -5 (using two's complement arithmetic)
---
# Bit Shift Operators

Shifting moves all binary digits left or right by a specified number of positions:

- << (Left Shift): Shifts bits to the left, effectively multiplying by $2^{\text{bits}}$.

    - Example: 17 << 2 gives 68 ($17 \times 2^2$)

- >> (Right Shift): Shifts bits to the right, effectively performing floor division by $2^{\text{bits}}$.

    - Example: 17 >> 1 gives 8 ($17 // 2^1$) 
---














