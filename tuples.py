# TUPLES
daysoftheweek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturdsy","Sunday")

#daysoftheweek = "Monday","Tuesday","Wednesday","Thursday","Friday","Saturdsy","Sunday"

# print(len(daysoftheweek)) to find the length;
daysoftheweek =list(daysoftheweek)
daysoftheweek[3]="Thur"

daysoftheweek+tuple(daysoftheweek)
print(daysoftheweek)