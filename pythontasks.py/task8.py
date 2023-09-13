 #Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”.
#  Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.

speed = int(input("Enter Speed: "))

points = 0

if speed <= 70:
    print("Okay speed")
elif speed > 70:
    points = round((speed - 70)/5)
    print(f"{points} Points")

if points >= 13:
   
    print("License suspended")
else:
    pass


