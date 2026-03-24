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


# a = {"Ironman", "Hulk", "Thor", "Captain America"}
# b = {"Superman", "Batman", "Wonder-Woman"}
# c = {"Hulk", "Thor", "SpiderMan"}

# # Union 
# print(a.union(b))

# # Difference
# print(a.difference(b))

# # Difference Update
# a.difference_update(c)
# print(a)

# # Intersection
# x  = a.intersection(c)
# print(x)

# a.intersection_update(c)
# print(a)

# y = a.symmetric_difference(c)
# print(y)

# To find max and min in set 
a = {12, 13, 56, 99, 34}
print(max(a))
print(min(a))

# To find common elements in three lists using sets
a1 = [1, 5, 8, 9]
a2 = [3, 4, 5]
a3 = [3, 4, 5, 8, 9]
print(set(a1) & set(a2) & set(a3))

# To find diff bw two sets
a = {1, 5, 8, 9}
b = {3, 4, 5}
print(a.difference(b))

# To remove an item from a set if it is present in set
a = {1, 5, 8, 9}
a.discard(8)
print(a)

# To check if a set is a subset of another set
a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 4}
print(a.issubset(b))






