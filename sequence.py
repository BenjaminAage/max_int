# Assignment 5: Algorithms and git
# Algorithm written for sequence.

# Design an algorithm that generates the first n numbers in the following sequence; 1,2,3,6,11,20,37, ___, ___, ___,.....

# 1. Fá notanda til að skrifa inn lengd raðar af tölum (e. sequence).
# 2. Láta kerfi skrifa út muninn milli tveggja talna.
#       Munur milli 0 og 1, er 1 + munurinn milli 1 og 2.
#       Dæmi: 3+((1–0)+(2–1)+(3–2)) = 6 +((2–1)+(3–2)+(6–3)) = 11....
# 3. Prenta út niðurstöður á númerum, miðað við lengd raðar sem notandi stimplar inn.


# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line

num0 = 0
num1 = 1
num2 = 2
sum = num0 + num1 + num2
counter = 0

if n <= 0:
  print("Not possible")
elif n == 1:
  print(n)
elif n >= 2:
  while counter < n:
    num0 = num1
    num1 = num2
    num2 = sum
    sum = num0 + num1 + num2
    print(num0)
    counter += 1


