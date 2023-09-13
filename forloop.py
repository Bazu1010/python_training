# for i in range(0,15):
#     if i % 2 == 0:
#         print(i)

#Write a fore loop to print numbers from 1 to 5

# for i in range (1,6):
#     print(i)

# Sum all the elements in a list using a  for loop;

# numbers = [2,3,4,5,6,7,8,9]
# total = 0
# for i in numbers:
    
#     total = total + i
# print(total)

# 99% of loop will be used in accessing items inside a list/tuple:

# ls = tuple(range(30,51))

# res = []
# for i in ls:
#     if i % 2== 0:
#         res.append(i) 
#     else:
#         pass
# print(res)


#Print the first 10 odd numbers in a range 0 to 50
# odd_num = list(range(1,50))

# my_odd = []

# for i in odd_num:
#     if i % 2 != 0:
#          my_odd.append(i)
#          if len(my_odd) == 10:
#               break
# print(my_odd)


#print the first 10 odd numbers 
res_odd = []

count = 0
for i in range(0,51):
   
  if i % 2 != 0:
    print(i)
    count = count + 1
     
    if count == 10:
          break
    
    else:
       pass


        







