 
#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. 
#Do this without using the the inbuilt max () function!


y = int(input("Num1: "))
x = int(input("Num2: "))
z = int(input("Num3: "))

if y > x and y > z:
    print(f"{y} is largest")
elif x > y and x > z:
    print(f"{x} is largest")

else:
    print(f"{z} is largest")