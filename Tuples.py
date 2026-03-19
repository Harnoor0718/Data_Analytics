# a = ("apple", "mango", "banana")
# print(type(a))


# b = ("Ironman",)

a = ("OnePlus", "Vivo", "Realme", "Samsumg", "Nokia")
# print(a[1:3])
# print(a[2:])
# print(a[::2])
# print(a[::-1])

for i in a:
    print(i)

for i in range(0, len(a)):
    print(a[i])

i = 0
while i < len(a):
    print(a[i])
    i += 1