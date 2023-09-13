 # Write a program which accepts email as form input or from terminal. 
 # Validate the email by checking if it's a valid email. 

vemail = input("Email: ")

if len(vemail.strip()) > 6 and (vemail.index("@")> 1) and "@" in vemail and (vemail.count(".") <=2) and (vemail.index(".") - vemail.index("@")> 2) and (vemail.index(".") < -1) :
    print("Valid Email")

else:
    print("NOT a valid email")

