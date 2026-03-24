a = {"Harnoor", "Arun", "Sahil", "Ram", "Aditi"}
# print(a)
# print(type(a))

# for x in a:
#     print(x)

# a.add("Richa")
# print(a)

# # Pop - random value pop
# a.pop()
# print(a)

# a.remove("Ram")
# print(a)

# a.discard("Harnoor")
# print(a)

# b = a.copy()
# print(b)


# print(a.isdisjoint(c))
# print(c.issubset(a))
# print(c.issuperset(a))


a = {"Ironman", "Hulk", "Thor", "Captain America"}
b = {"Superman", "Batman", "Wonder-Woman"}
c = {"Hulk", "Thor", "SpiderMan"}

# Union 
print(a.union(b))

# Difference
print(a.difference(b))

# Difference Update
a.difference_update(c)
print(a)

# Intersection
x  = a.intersection(c)
print(x)

a.intersection_update(c)
print(a)

y = a.symmetric_difference(c)
print(y)





