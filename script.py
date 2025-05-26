

print("Hello, World")
print('Hello, World 2')

# Hello, World 3
"""
print("Hello, World 3")
print("Hello, World 4")
print("Hello, World 5")
"""

myvar1= 1
myvar2 = "Hello, World 6"

print(myvar1)
print(myvar2)
print(myvar1, myvar1, )

myvar1= 1+2
print(myvar1)

myvar1 = myvar1 + 1
print(myvar1)

myvar1 += 1
print(myvar1)

print(myvar1 + myvar1)

mydatatype1 = type(myvar1)

print(mydatatype1)

myfloat = 1.34
print(type(myfloat), myfloat)

myfloat -= myvar1
print(type(myfloat), myfloat)

myfloat = myfloat * 5
print(type(myfloat), myfloat)

myfloat = myfloat * 5
print(type(myfloat), myfloat)
myfloat += 0.5
print(type(myfloat), myfloat)

myint = int(myfloat)
print(type(myint), myint)

myint2 = 1
myint2 += 1

myCombinedText = "Text" +" " + str(myint2)
print(myCombinedText)

myCombinedText = "image" + str(myint2) + ".png"
print(myCombinedText)

input("Bitte nenne dein Alter: ")
alter = input("Bitte nenne dein Alter: ")
alter -= 10

print("Vor 10 Jahren warst du", alter)


myTryToDivideByZero = 1 / 0
print(myTryToDivideByZero)
