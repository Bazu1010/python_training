#Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
#If the password is correct access is granted. After you show them a message , the account is blocked.

password = "admin@123"
 

i = 3
for i in range(i):
    my_pass = input("Enter password: ")
    
    
    if my_pass == password:
        print("Access granted")
        break
    elif my_pass != password:
        print("Wrong password")

        if i == 3:  
         
         
         print("Account Blocked")

 

   
    # if password == "admin@123":
    #     print("")
    #     x = x + 1
    # elif x < 4 and password != "admin@123":
    #     print("Wrong password, try again")
    # elif x == 4:
    #     print()

    


