
     ### CLASS

# x = int(input("value X: "))
# x=0
# def my_inc():
    
#     print("X1 is ", x)
#     x = x + 1

# my_inc()
# print("X2 is ", x)

  ## Classes are a colection of functions and variables that are related and can manipulate eachother.
 ##   A function inside a class is called a method // naming starts with a capital character
##    Representation of something in the real world
   ### A variable inside a class is called a property
##    Example student
 ##  Here you have all functions and properties
  ##  related to a student eg create_student(), email



# class Calculator():
#     x = 0
#     def my_inc(self):
#         self.x = self.x +1


class Person():
    name = ""
    gender = ""
    email = ""
    phone = 0
    details = []
    

    # Constructor= A special method used
    # to instantiate initial values

    def __init__(self,n,g,p,e):
        self.name = n
        self.gender = g
        self.email = e
        self.phone = p
        self.add()

        

    def add(self):
        self.details.append(self.name)
        self.details.append(self.email)
        self.details.append(self.phone)
        self.details.append(self.gender)

p1 = Person(input("Enter name: "),
            input("Enter Gender: "),
            input("Enter Email: "),
            input("Enter Phone: "))
            # i"John","Male", 702765976,"j@mail.com"

# print(p1.phone)
# print(type(p1))
p1.add()
print(p1.details)


# p2 = Person("Moha","Male","Mh@mail,com", 12345)
# print(p2.phone)
# print(type(p2))
# p2.add()
# print(p2.details)






