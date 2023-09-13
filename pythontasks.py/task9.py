

# Write a program called stars.
# It should prompt the user for a number, and it should print the number of stars till the number entered.

stars = int(input("Number of stars: "))
count=0
for i in range(1,stars+1):
    value=("*"*i)
    count=count+1
    if count==stars:
        value=value+("."*i)
    print(value)
