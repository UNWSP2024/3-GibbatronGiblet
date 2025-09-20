# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.
dog_cost = 0
toppings_cost = 0

dog_type = str(input("Would you like a hot dog or a chili dog? Type Hot/Chili:"))
if dog_type == "Hot":
    dog_cost = 3.50
elif dog_type == "Chili":
    dog_cost = 4.50
else:
    print("Please enter a valid choice.")

cheese = 0.5
peppers = 0.75
grilled_onions = 1.00

toppings_choice = str(input('''What toppings would you like? You can add none(0), cheese(1), peppers(2), grilled onions(3),
      or a combination of the last three. You may only have one of each topping. Type your choices in numerical order (e.g. 0 or 123 or 3):'''))
if toppings_choice == '0': #no toppings
    toppings_cost = 0
elif toppings_choice == '1': #cheese
    toppings_cost = cheese
elif toppings_choice == '2': #peppers
    toppings_cost = peppers
elif toppings_choice == '3': #grilled onions
    toppings_cost = grilled_onions
elif toppings_choice == '12': #cheese & peppers
    toppings_cost = cheese + peppers
elif toppings_choice == '23': #cheese & grilled onions
    toppings_cost = cheese + grilled_onions
elif toppings_choice == '13': #peppers & grilled onions
    toppings_cost = peppers + grilled_onions
elif toppings_choice == '123': #everything
    toppings_cost = cheese + peppers + grilled_onions
else:
    print("Please enter a valid choice.")

subtotal = dog_cost + toppings_cost
sales_tax = 0.07 * (dog_cost + toppings_cost)
total_cost = sales_tax + dog_cost + toppings_cost

print("Your subtotal is $" + f'{subtotal:.2f}')
print("Your sales tax is $" + f'{sales_tax:.2f}')
print("Your total is $" + f'{total_cost:.2f}')

# Written by Logan Gibson on 9/10/25
# This program is titled "Celsius to Fahrenheit Conversion"
