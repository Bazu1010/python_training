

# Put in a list the first 10 odd numbers between 10 to 50. 

lst = []
for i in range(10,51):

    if i % 2 != 0:
        
        lst.append(i)

        if len(lst) == 10:
             break
        
print(lst)

        
        


