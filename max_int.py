# Assignment 5: Algorithms and git

# 1. Fá notanda til að slá inn tölur (integer).
# 2. Láta kerfið greina það hvort um jákvæða eða neikvæða tölu er um að ræða (sem sleginn er inn af notanda).
# 3. Flokka jákvæðar tölur saman í lista.
# 4. Stoppa própram þegar slegið er inn neikvæða tölu.
# 5. Leita að hæstu jákvæða tölugildið sem slegið hefur verið inn.
# 6. Prenta út hæsta jákvæða töluna sem slegið var inn af notanda.:x

# Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.

number_int = int(input("Input a number: "))
# Búa til lista sem heldur útanum allar jákvæðar tölur sem slegnar eru inn.
max_int = []

# Check if the number typed is a positive number
while number_int >= 0:
  number_int = int(input("Input a number: "))
  # Add the typed number to the list of positive numbers
  max_int.extend([number_int])

  # If the number is negative, stop the program
  if number_int < 0:
    print("The maximum is",max(max_int))

