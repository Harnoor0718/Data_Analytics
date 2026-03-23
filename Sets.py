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

a = {"Ironman", "Hulk", "Thor", "Captain America"}
b = {"Superman", "Batman", "Wonder-Woman"}
c = {"Hulk", "Thor"}

print(a.isdisjoint(c))
print(c.issubset(a))
print(c.issuperset(a))