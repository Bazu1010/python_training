#DICTIONARY

person = { "name":"Kimani", "age":27, "phone": 702765976}

###  how to ACCESS the name of the person: 

# print(person["name"])
# print(person["phone"])

person = { "name":"Kimani", "age":27, "phone": 702765976 }
# print(person.keys())
# print(person.values())

# Add key "amount":900

person["amount"] = 900
print(person)

## Adding using .UPDATE()

# varname.update({"key" : value})


## REMOVE ITEMS 

#   var_name.pop("keyname")
#   del var_name["keyname"]

#   var_name.popitem()    removes the last inserted item


##  COPY DICTIONARY

# x = varname.copy()
#   print(x)


### ACCESSING ITEMS IN A NESTED DIC

# varname["key1"]["nestdkey2"]