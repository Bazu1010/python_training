
from datetime import datetime
today = datetime.now()

dob = input("Enter DOB (dd-mm-yy): ")

sdob =dob.split("-")

if len(sdob) != 3 or int(sdob[0])> 31 \
 or int(sdob[1]) > 12 or int(sdob[2]) < 1900 \
 or int (sdob[2]) > 2023 :
    print("Wrong Date Format")
else:
    y = today.year - int(sdob[2])
    m = today.month-int(sdob[1])
    d = today.day - int(sdob[0])

    if d < 0:
        m= m-1
        d = d+31

    if m < 0:
        y=y-1
        m=m+12


    print(f"{y} years {m} months {d} days old")

