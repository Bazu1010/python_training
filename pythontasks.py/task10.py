  

# array/list below if we know that the stock is the last digit in every array/list.

prods = [["omo","30",300], ["milk","50",200],["bread","45",359], ["coffee","5",79]]

# sum = int(prods[0][2])+int(prods[1][2])+int(prods[2][2])+int(prods[3][2])
# print(sum)

sum=0
for i in prods:
   stock = (i[2])
   sum+=stock
print(sum)
