
# Convert any phonenumberinput to a number to start with +254… 

phone_num = input("Enter phone number: ")

if phone_num.startswith("07") and len(phone_num) == 10:
   y = "+254" + phone_num[1:]

elif phone_num.startswith("01") and len(phone_num) == 10:
    y = "+254" + phone_num[1:]
elif phone_num.startswith("7") and len(phone_num) == 9:
   y = "+254" + phone_num[0:]

elif phone_num.startswith("1") and len(phone_num) == 9:
   y = "+254" + phone_num[0:]

elif phone_num.startswith("254") and len(phone_num) == 12:
   y = "+" + phone_num[0:]
else: 
   pass
print(y)
 