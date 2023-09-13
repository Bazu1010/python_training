  


     # Write a program that displays a numbers 1 to 50 inside a list.
     # From the result above display the ones divisible by 7 or 5 inside a list.


numbers = list(range(1,51))

div_sev = []
div_fiv = []



for i in numbers:
  
   
    if i % 7 == 0:
      div_sev.append(i)

    elif i % 5 == 0:
      div_fiv.append(i)
       
    else:
       pass

    # lst = div_fiv+div_sev
    # print(lst)

    # OR

# for m in div_fiv:
#    div_sev.append(m)
# print(div_sev)

div_sev.extend(div_fiv)
print(div_sev)








        


