# # 1.Given a variable temperature with a value of 25°C, 
# #write an if statement to check if the temperature is above 30°C using the greater than (>) operator.

# temp = int(input("Current Temprature: "))

# if  temp > 30:
#     print(f"{temp}°C above 30°C")

# else:
#     print(f"{temp}°C is below 30°C")


# 2.Create a dictionary called stock with items as keys and their quantities as values.
#  Write an if-else statement to check if the quantity of "apples" is zero using the equality (==) operator.

# stock = {"kiwi": 0, "oranges": 14, "banana":47}

# if stock["kiwi"] == 0:
#     print("Kiwi out of stock")

# else:
#   print("In stock")


#3.Declare a list called even_numbers containing integers.
# Write an if statement to check if the first element of the list is an even number using the modulo (%) operator 

# even_numbers = [2,3,4,5,6,7,8,9,0] 

# if even_numbers[0] % 2 ==0:
#     print(f"{even_numbers[0]} is Even")
# else:
#     print(f"{even_numbers[0]} is ODD")


#4. Given a list prices containing prices of products.
# write a code snippet using if statements to check if any product's price is within the range $20 to $50 using the logical and operator.

# prices = [{"apple": 30,"kiwi":40,"orange":70}]

# prices[0][]

#4.	Imagine you have a list employees containing dictionaries with keys "name", "hours_worked", and "hourly_rate".
# Write a code snippet using  if statements to calculate the salary for an employee named "Alice" based on her hours worked and hourly rate.

# employees = [{ "name":"Ivy","hours_worked": 20,"hourly_rate": 5},
#               {"name": "Alice","hours_worked": 20,"hourly_rate": 5}]

#5.	Create a dictionary book_ratings with book titles as keys and their ratings as values.
# Write an if-elif-else statement to find out if a book "The Adventure" has a rating of 5 or is rated below 2.

# book_ratings = {"kim":{"height": 75,
#                        "weight":35},
                       
#                        "Mike":{"height": 55,
#                        "weight":89}}

# #check if mike's weight is below 80.

# if book_ratings["Mike"]["weight"] < 80:
#     print("Weight is below 80")
# else:
#     print("Weight above 80")

#6.	Suppose you have two sets: set_x and set_y.
# Write a code snippet using conditional statements to check if the symmetric difference between the two sets is not empty, using the ^ (symmetric difference) operator

x = {"apple","banana","cherry","John"}

y = {"Fred","John","Mike","banana"}

if x^y:
    symmetric = x^y
    print(symmetric)
else:
    print("Error")