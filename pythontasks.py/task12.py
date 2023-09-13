
  # Write a program that prints the largest of 4 inputs taken in from a user. 
  # Assume that the user would not enter any two numbers which are the same.
num1 = (input("num1: "))==float
num2 = (input("num2: "))==float
num3 = (input("num3: "))==float
num4 = (input("num4: "))== float

if num1> num2 and num1>num3 and num1>num4:
    print(f"{num1} is the larest")
elif num2> num1 and num2>num3 and num2>num4:
    print(f"{num2} is the larest")
elif num3> num2 and num3>num2 and num3>num4:
    print(f"{num3} is the larest")
elif num4> num1 and num4>num2 and num4>num3:
    print(f"{num4} is the larest")
else:
    print("Please input a number")
