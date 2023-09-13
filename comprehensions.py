# Write a program that checks the % of 7;

# lsc= []

# lsc = [x for x in range(10,50) if x%7==0 and x%5==0]
# print(lsc)


blogs = [{"id": 1, "title":"PCI","description":"starting..","status":0},
         {"id": 2, "title":"TSI","description":"starting..","status":0},
         {"id": 3, "title":"VS","description":"starting..","status":1},
         {"id": 4, "title":"K4","description":"starting..","status":0},
         {"id": 5, "title":"ZX","description":"starting..","status":1},]


### filter in the list only active blogs and lower the title for each of them
active_blogs =[blog for blog in blogs if blog["status"] ==1 ]
# print(active_blogs)

# def change_case(x):
#     w = x["title"].title()
#     x["title"] = w
#     return x

# clean_blog = list(map(change_case,active_blogs))
# print(clean_blog)



ls=[]

for blog in blogs:
    if blog["title"] == 1:
        blog["title"] = blog["title"].title()

    m = ls.append(blog)

    print(m)