# Write a program to check whether a number is divisible by 7:

# any_num = int(input("Check number: "))

# if any_num % 7 == 0:

#     print(f"{any_num} is DIVISIBLE by 7" )

# else:
#     print(f"{any_num} is NOT divisible by 7")

    
    #Write a program to calculate electricity bill based on the following criteria;
    #First 50 units Kshs 20, next 50 units Ksh 40. More than 100 units Ksh 100.


units_consumed = int(input("Enter units consumed: "))

if units_consumed>0 and units_consumed <= 50:
    price= int(units_consumed)*20
    
elif units_consumed>50 and units_consumed <= 100:
    price = ((units_consumed-50)*40)+1000

elif units_consumed<0 :
    price = 0
else :
    price=((units_consumed-100)*100) + 3000
print(f"Your bill is {price}")
   




