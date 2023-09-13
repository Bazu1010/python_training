# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123”
#  if so then print  “Login is Successful” and if not print “Invalid username or password”.
# ONLY accept 3 tries after which it notifies you that you have been blocked.

email = "admin@mail.com"
password = "Admin@123"

email = (input("Enter your email: "))
password = (input("Enter your Password: "))

# FOR LOOP METHOD

if password == "Admin@123" and email == "admin@mail.com":
    print("access granted")

else:
    attempts = 1
    for attempts in range(attempts*3):
        email = (input("Enter your email: "))
        password = (input("Enter your Password: "))

        if password == "Admin@123" and email == "admin@mail.com":
            print("access granted")

        elif password != "Admin@123" or email != "admin@mail.com":
            print("Wrong password or email")
            attempts += attempts

    if attempts == 3:
          

          print("Account is blocked")
          
            
    else:
        pass

    # WHILE LOOP METHOD
# if password== "Admin@123" and email == "admin@mail.com":
#     print("access granted")

# else:
#     # print("Wrong password or email")
#  attempts = 0
#  while attempts<3:
#   email = (input("Enter your email: "))
#   password = (input("Enter your Password: "))

#   if password== "Admin@123" and email == "admin@mail.com":
#      print("access granted")
#      break
#   elif  password != "Admin@123" or email != "admin@mail.com":
#          print("Wrong password or email")
#          attempts += 1
#  else:
#        pass


# if attempts == 3:
#        print("Account is blocked")
# else:
#     pass
