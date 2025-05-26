#Aufgabe 1 Casting

x = "4.8"
y = True

#a) Warum funktioniert int(x) nicht direkt?
#Weil es ein Float ist und kein int.
#print(x)
#b) Wie kannst du trotzdem einen int-Wert aus x erhalten?
#print(int(float(x))) #4

#c) Was ist das Ergebnis von float(y) und warum?
#print(float(y)) #1.0
# Weil True == 1

#Aufgabe 2 Casting

data = 123

#a) Was ergibt list(data) und warum?
#list(data) #TypeError: 'int' object is not iterable
#b) Wie bekommst du aus data eine Liste mit nur einem Integer 123 als Element?
#lst= [data]
#(print(lst))

#oder
#lst= data,
#lst = list(lst)
#print(type(lst), lst)

      
#c) Wie bekommst du aus data folgende Liste aus ints: [1, 2, 3]?
#strList = list(str(data))
#print(type(strList), strList)

#lst = []
#for i in range(len(strList)):
    #lst.append(int(strList[i]))
#print(lst)

#ODER

#a, b, c = str(data)
#a=int(a)
#b=int(b)
#c=int(c)
#lst= [a, b, c]
#print(lst)

#ODER

#lst= []
#for item in (str(data)):
   # lst.append(int(item))
#print(lst)

#ODER

#lst = [int(item) for item in str(data)] 
#print(lst)

#Aufgabe 3 – Casting

#values = [None, "False", "", 0, [], 'None', {}, False]

#a) Welche dieser Werte ergeben False, wenn du sie mit bool() castest?
#"False" = True
# 'None' = True
#b) Iteriere über die Liste und gebe in jeder Iteration den jeweiligen wert und Datentyp des Wertes aus
#for item in values:
#   print(item, type(item), "\n")
    
#c) Was passiert bei int(True) und int(False)?
#int(True) == 1
#int(False) == 0

#Aufgabe 4 Casting
#val = None

#a) Was passiert bei str(val) und warum?
#print(str(val)) #prints "None", as it becomes text
#b) Was bei int(val) und warum?
#print(int(val)) # Error, da nicht string, byte like oder Nummer
#c) Warum ist bool(val) False?
# None hat kein Wert - es heißt Nichts
"""
#Aufgabe 5 - Tuples
val = (5)

#a) Füge ein zeichen hinzu, um aus dem int ein Tuple zu machen
val = (5, )
#b) Erstelle ein Tuple in dem Du einer Variablen innerhalb von zwei Zeichen einen Wert zuweist.
myTuple = 1, 
print(myTuple)
"""
"""
#Aufgabe 6: Tuples

data = ("Python", 2025, True)

#a) Entpacke das Tuple und gebe die entpackten Werte in der Konsole aus.
#lengthOfTuple = len(data)
a, b, c = data
print(a, b, c)
#b) Gebe die Anzahl der Werte im Tuple mit der richtige Python-native Funktion in der Konsole aus.
print(len(data))
#c) Erstelle programmatisch eine Liste aus dem Tuple mit Werten in umgekehrter Reihenfolge
a = list(data)
print(a)
a.reverse()
print(a)

#ODER
b = list(data)
print(b [::-1])
#d) Nenne drei Methoden, die auf Listen ber nicht auf Tuples existieren:
#.reverse
#.pop
#.remove

#e) Finde programmatisch heraus ob der Wert True im Tuple existiert.
if True in data:
    print("True is present", "\n", "Index:", data.index(True))
else:
    print("No True present")
#f) Wenn der Wert True im Tuple existiert, dann finde programmatisch den Index davon heraus
"""

#Aufgabe 7: Bonus

data = ["1", "zwei", "3", "vier", "5", 6.0, True, [1]]

#a) Iteriere durch die Liste.
for item in data:
    print(item, "\n")
#b) Versuche, jeden Wert als int zu casten (try/except)
for item in data:
    try: int(item)
    except Exception as e:
        print(item, "Fehler:", type(e), e)
    if item in data == int:
        print(list(item)) 
    
#c) Sammle nur die gültigen Zahlen in einer neuen Liste.
lst = []
for item in data:
    try:
        lst.append(int(item))
    except:
        pass
#d) Sammele die Datentypen aller items von data in einer weiteren neuen Liste.
typesList = []
for item in data:
    typesList.append(type(item))
    try:
        lst.append(int(item))
    except:
        pass
#d) Caste beide neuen Listen je als ein Tuple und gebe beide Tuple in der Konsole aus
intTuple = tuple (lst)
typesTuple= tuple(typesList)
print(intTuple)
print(typesTuple)