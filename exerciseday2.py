"""
#Aufgabe 1
a=7
b= 15

c= a + b
print(c) #22
d = a - b
print(d) # -8
e = a * b
print(e) # 105
f = a / b
print(f) # 0.4666666666666667

g = a % b
print(g) # 7
h = b // a
print(h) # 2

a = 3
b = 4
c = a ** b
print(c) # 81

a= 36
b = 0.5
c = a ** b
print(c) # 6.0

#Aufgabe2
a= 10
a+= 5
print(a) # 15
a *= 2
print(a) # 30
a -= 4  
print(a) # 26
a /= 2
print(a) # 13.0


#Aufgabe 3


#Vergleichsoperatoren (Vergleichen von Werten)(Resultat ist immer True oder falso (oder Error))
print(5 != 5)
print(8 >= 7)
print(2 <= 2)

print((5 != 5) and (8 >= 7)) #false
print((5 != 5) or (8 >= 7)) #true

print((5 != 5) and (2 <= 2)) #false
print((5 != 5) or (2 <= 2)) #true

print((2 <= 2) and (8 >= 7)) #true
print((2 <= 2) or (8 >= 7)) #true
"""
#Aufgabe 4 – Listen und Loops
numList = [1, 2, 3, 4, 5, 6]
mixedList = [8, "Hello", 8.5, True, 85, "Monday", 5.5, False, numList]

for item in mixedList:
    print(item, "\n")
    if type(item) == list: #Muss == sein, da es sich um einen Vergleich handelt
        print(type(item), item)
        listIndex = mixedList.index(item)
        print("listIndex", listIndex, "\n")
        for listItem in item:
            print(listItem, "\n")


"""
#Aufgabe 5 – Loops

calc = 0
while calc <= 30: #gibt die Zahlen von 0 bis 9 aus (10 exkl)
    calc += 1
    print(calc)
    if calc == 20:
        break
    print(calc)

quickList = list(range(1, 100001))
print(quickList, "\n")
print(len(quickList),"\n")
"""