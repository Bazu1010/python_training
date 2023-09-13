
#### MAPS

numbers = [1,2,3,4,5]
squared = []

for i in numbers:
 squared.append(i**2)

# print(squared)

def squared(i):
    return i**2

final  = map(squared, numbers)
print(list(final))


#### Example2

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

numss = map(int,str_nums)

print(list(numss))


