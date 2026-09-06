
# 1. Comparison Operators

> Jab hume do values ko compare karna ho, toh hum special operators use karte hain. Inka jawab hamesha True ya False mein aata hai.

- Equal to (==): Check karta hai ke kya do values barabar hain.
    - Example: 2 == 2 $\rightarrow$ True
    - Example: 1 == 2 $\rightarrow$ False
    - Attention: = se value assign hoti hai (jaise x = 5), jabke == se comparison hota hai.

- Not equal to (!=): Check karta hai ke kya do values aapas mein barabar nahi hain.
    - Example: var = 0 $\rightarrow$ var != 0 $\rightarrow$ False

- Greater than (>) & Greater than or equal to (>=): Check karta hai ke value bari hai ya barabar hai.

    - Example: black_sheep > white_sheep

    - Example: centigrade_outside >= 0.0
 
- Less than (<) & Less than or equal to (<=): Check karta hai ke value choti hai ya barabar hai.

    - Example: current_velocity_mph < 85

      ---
  
# 2. Conditional Statements

> Sawaal ka jawab milne ke baad code ko batana hota hai ke aage kya karna hai.

- if Statement: Agar condition True ho, tabhi andar ka code chalta hai.

      if sheep_counter >= 120:

         sleep_and_dream()
  
        feed_the_sheepdogs()  # Yeh bina condition ke hamesha chalega

- if-else Statement: Agar condition True ho toh pehla block, warna else wala block chalta hai (Plan B).

       if the_weather_is_good:
          go_for_a_walk()
      else:
          go_to_a_theater()
      have_lunch()  # Dono soorato mein lunch hoga

  - Nested if-else: Ek if ke andar doosra if lagana.

         if the_weather_is_good:
          if nice_restaurant_is_found:
             have_lunch()
         else:
            eat_a_sandwich()
         else:
            go_shopping()

- elif Cascade: Jab ek se ziada conditions bari-bari check karni hon.

      if the_weather_is_good:
           go_for_a_walk()
      elif tickets_are_available:
            go_to_the_theater()
      elif table_is_available:
            go_for_lunch()
      else:
            play_chess_at_home()
