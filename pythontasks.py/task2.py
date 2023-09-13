 # Depending on whether the number is even or odd, display  either “odd” or “even” to the user.

number = int(input("Number: "))

if number % 2 == 0:
    print(f"{number} is Even")

else:
    print(f"{number} is Odd")

