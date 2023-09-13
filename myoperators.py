# cars = ["ford","BMW","Jeep"]

# print("toyota" not in cars)

#Write a program that checks whether a person can vote or not:
  
# age = 77

# if age >= 18 :    

#     print("Old enough to vote")

# else:

#     print("Wewe ni mtoto enda ukalale")

#Take three inputs from a user, separately. Print the largest of the numbers.

inp1 = int(input("input1: "))
inp2 = int(input("input2: "))
inp3 = int(input("input3: "))

if inp1>inp2 and inp1>inp3:
    print("Input 1 greatest")   #When you want to display the value in the result, at the print(f"{varinput} is greatest")
elif inp2>inp1 and inp2>inp3:
    print(f"{inp2} is greatest")

else: print(f"{inp3} is greatest")



