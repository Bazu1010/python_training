#Task in page 26 in the portal
 
 #1. Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the string class
# name = "  JOHn  ." to “john”

fname= " JOHn  ."




print(fname.strip()[:4].lower())

#Slice the string sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”

sentence_one = "The Dog Breed is German Shepherd"

print(sentence_one[8:23])

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”;

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"

print(sentence_two[16:30])

#Split the below sentence using a semicolon i.e ; And display length of the result.
#“The lazy dog; ran so fast; it hit the wall.” 

sentence= "The lazy dog; ran so fast; it hit the wall."

print(sentence.split(";").__len__())







