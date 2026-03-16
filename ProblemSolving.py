# name = "Harnoor"
# age = 23
# address = "123 Main Street"

# print("Name:", name)
# print("Age:", age)
# print("Address:", address)

# x = 12
# y = 23
# temp = x
# x = y
# y = temp

# print("After swapping:")
# print("x:", x)  
# print("y:", y) 

# x = x + y
# y = x - y
# x = x - y

# print("After swapping:")
# print("x:", x)      
# print("y:", y)

# x = 3.9
# print(type(x))  

# x = int(x)
# print(type(x))
# a = int(input("Enter a number: "))
# print(float(a))

# n = int(input("Enter a number: "))
# if n > 0:
#     print("The number is positive.")
# elif n < 0:
#     print("The number is negative.")        
# else:       
#     print("The number is zero.")

# letter = input("Enter a letter: ")
# if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#     print("The letter is a vowel.")
# else:    print("The letter is a consonant.")

# num = int(input("Enter a number: "))
# if num>=0 and num<=9:
#     print("The number is a single-digit number.")
# elif num>=10 and num<=99:
#     print("The number is a two-digit number.")
# elif num>=100 and num<=999:
#     print("The number is a three-digit number.")
# elif num>=1000 and num<=9999:
#     print("The number is a four-digit number.")
# else:
#     print("The number is not a single-digit, two-digit, three-digit, or four-digit number.")

# for i in range(1, 11):
#     print(i)

# n = 7
# for i in range(1,11):
#     print(n, "X", i, "=", n*i) 

# n = 1
# a = 7

# while n <= 10:
#     print(a, "X", n, "=", a*n)
#     n += 1

# while True:
#     print("Menu:")
#     print("1. Option 1")
#     print("2. Option 2")
#     print("3. Option 3")    
#     print("4. Exit")    
#     choice = input("Enter your choice (1-4): ")
#     if choice == '1':
#         print("You selected Option 1.")
#     elif choice == '2':
#         print("You selected Option 2.")
#     elif choice == '3':
#         print("You selected Option 3.")
#     elif choice == '4':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")
# 
# for i in range(1, 4):
#     for j in range(1,11):
#         print(j, end = "  ") 
#     print()

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end= "  ")
#     print()
 
# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)


# sum = 0    
# for i in range(0, 51, 2):
#     sum += i
# print(sum)

# for i in range(1,21):
#     print(i, "=", i**2)


# i = 1
# sum = 0
# while i <= 20:
#     if i%2 != 0:
#         sum += i
#     i += 2
# print(sum)


# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)


# while True:
#     name = input("Enter your name: ")
#     total = 0
#     while True:
#         qty = int(input("Enter the quantity of items (or -1 to finish): "))
#         if qty == -1:
#             break
#         amount = float(input("Enter the amount for each item: "))
#         total += qty * amount
#     print("Total amount for", name, "is:", total)


# A = "Why fit in, When you are born to stand out!"

# print(len(A))
# print(A.count('o'))
# print(A.lower())
# print(A.upper())
# print(A.title())
# print(A.find("fit in"))

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end = " ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end = " ")
#     print()

# for i in range(1, 6):
#     for j in range(6, i, -1):
#         print(i, end = " ")
#     print()

# for i in range(1, 6):
#     for j in range(6, i, -1):
#         print(j, end = " ")
#     print()

# for i in range(1, 6):
#     for j in range(5,i,-1):
#         print(" ", end = " ")
#     for k in range(i):
#         print("*", end = " ")
#     print()


# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end = " ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()
# for i in range(5, 0, -1):
#     for  k in range(0, i-1):
#         print("*", end = " ")
#     print()

# for i in range(1, 11):
#     for j in range(1, i+1 ):
#         print(i*j, end = " ")
#     print()
  
# n = int(input("Enter the number of terms: "))
# n1 = 0
# n2 = 1
# if n == 1:
#     print(n1)
# else:
#     for i in range(1,n+1):
#         print(n1, end = " ")
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3

# n = int(input("Enter a number: "))
# if n < 0:
#     print("Negative numbers are not considered prime.")
# elif n == 0 or n == 1:
#     print("0 and 1 are not prime numbers.")
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n, "is a prime number.")  
#     else:
#         print(n, "is not a prime number.")

# n = int(input("Enter a number: "))

# rev = 0
# temp = n

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if temp == rev:
#     print(temp, "is a palindrome.")
# else:
#     print(temp, "is not a palindrome.")


# a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# b = a.split(".")
# print(b)

# a = input("Enter a  string: ")
# b = sorted(a)
# print(b)

# a = "Hello"
# b = a.replace("e","")
# print(b)

# Z = "F.R.I.E.N.D.S"
# B = Z.replace(".", "")
# print(B)

s = input("Enter a string: ")
# print(s[::-1])
# print(s.isdigit())
# print(s[::-1] == s)

# vowels = "aeiouAEIOU"
# count = 0
# for char in s:
#     if char in vowels:
#         count += 1
# print("Number of vowels in the string:", count)

# print(s.istitle())




