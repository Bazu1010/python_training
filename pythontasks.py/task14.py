  ##### Write a program that takes input of 2 values and adds them. 
#####   The program should only accept numbers and floats only
#####   or otherwise display an error “invalid character entered” and take the user to re-enter the inputs 

val1 = float(input("Value 1: "))
val2 = float(input("Value 2: "))

total = val1 + val2

if total == val1 + val2:
    print(f"Total: {total}")
else:
    print("Invalid character entered")