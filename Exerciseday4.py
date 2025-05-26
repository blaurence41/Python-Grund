"""
#Aufgabe 1 – Dictionaries und Strings

user = {
    "id": 42,
    "name": "Alice",
    "email": None,
    "active": True,
    "score": 0
}

#a) Finde alle Keys, deren Werte Falsy sind und packe sie programmatisch in eine Liste namens falsyVals
falsyVals = []
for key in user:
    if not user[key]:
        falsyVals.append(key)
print("falsyVals", falsyVals)

#ODER

falsyvals = [key for key, val in user.items() if not val]
print("falsyVals", falsyVals)

#b) Setze alle falsy Values im Dict programmatisch auf "unknown"

for key in user:
    if not user[key]:
        user[key] = "unknown"
print("user", user)

#ODER
for key in falsyVals:
    user[key] = "unknown"
print("user", user)

#c) Gib das angepasste Dictionary aus
#d) Verwandele alle Werte mit "unknown" im Dict programmatisch in Großschreibung: "UNKNOWN" ohne explizit "UNKNOWN" zu schreiben
for key in user:
    if user[key] == "unknown":
        user[key] = user[key].upper()
print("user", user)
"""
"""
#Aufgabe 2 – Reverse Mapping

colors = {
    "raspberry":        "red",
    "banana":           "yellow",
    "kiwi":             "green",
    "sky":              "blue",
    "lemon":            "yellow"
}
print("colors", colors)
#a) Erstelle programmatisch ein neues Dictionary, in dem Farben die Keys sind und Früchte die Values
newDict = {v: k for k, v in colors.items()}
print(newDict)

#oder
newDict = {}
for key, val in colors.items():
    newDict[val] = key

print("newDict: ", newDict)


#b) Was passiert, wenn mehrere Keys denselben Wert haben? (Teste durch Duplikate)
#Duplikate gelöscht, d.h. 1. gehandelte Duplikat gelöscht
"""
"""
#Aufgabe 3 – Listen + Dicts verschachtelt

users = [
    {"id": 1, "name": "Tom", "city": "Berlin"},
    {"id": 2, "name": "Sara", "city": "Hamburg"},
    {"id": 3, "name": "Alex", "city": "Berlin"},
    {"id": 4, "name": "Nina", "city": "Munich"},
]
print(type(users))
#dict(users)
#a) Gebe den Namen jedes Users programmatisch in der Konsole aus
for dict in users:
    print(dict["name"])
#b) Entferne programmatisch alle User die in Munich wohnen.
Munich = []
for u in users:
    if u["city"] == "Munich":
        Munich.append(u)
   
print(Munich)

#oder
users = [u for u in users if u["city"]!="Munich"]
print(users)

#oder

for u in users:
    if u["city"] == "Munich":
        currIndex = users.index(u)
        print(currIndex)
        #del users(currIndex)
print(users)

#c) Füge programmatisch allen Userdatensätzen den Key "suggest_friend" mit dem Wert None hinzu
users = [
    {"id": 1, "name": "Tom", "city": "Berlin"},
    {"id": 2, "name": "Sara", "city": "Hamburg"},
    {"id": 3, "name": "Alex", "city": "Berlin"},
    {"id": 4, "name": "Nina", "city": "Munich"},
]
for u in users:
    u["suggest_friend"] = None
    print(u)
#d) Füge für alle User, die in der selben Stadt wohnen, dem Key "suggest_friendfar" den Wert True hinzu und bei allen anderen Usern den Wert False

for i in users:
    for j in users:
        if i["id"] != j["id"]:
            if i["city"] == j["city"]:
                i["suggest_friend"] = True

print(users)
"""
"""
#Aufgabe 4 - Lists and Sets

userA = ["chess", "trading", "jogging", "chess", "music"]
userB = ["gaming", "jogging", "music", "travel", "music"]

#a) Gebe die Interessen von userA nur mit eindeutigen Einträgen in der Konsole aus
setA = set(userA)
setB = set(userB)
print(setA, "\n", setB)
#print(type(setA), type(setB))
#b) Erstelle ein Set in denen die Interessen aller Nutzer eindeutig aufgeführt sind
#listA = list(userA)
#listB = list(userB)
#print("listA:", listA, "\n", "listB:", listB)
bigset = set(userA + userB)
print("bigset", bigset)
#c) Erstelle eine Liste aus diesem Set und sortiere die Einträge alphabetisch
smalllist = list(bigset)
smalllist.sort()
print(smalllist)
#d) Erstelle eine Liste namens hobbyMatch in denen nur die gemeinsamen Interessen beider User ohne Duplikate aufgeführt sind
# Find intersection
hobbyMatch = list(setA & setB) # & operator reserved for sets
print("hobbyMatch", hobbyMatch)

#oder
mutualHobbies = []
for hobby in userA:
    if hobby in userB:
        mutualHobbies.append(hobby)
mutualHobbies = list(set(mutualHobbies))
print("mutualHobbies", mutualHobbies)
#oder
mutualHobbies = set(userA).intersection(userB)
print("mutualHobbies", mutualHobbies)

#e) Entferne das Hobby "jogging" aus der hobbyMatch Liste
hobbyMatch.remove("jogging")
print(hobbyMatch)

#f) Füge der hobbyMatch Liste den Eintrag "cats" hinzu
hobbyMatch.append("cats")
print(hobbyMatch)

#for Sets hobbymatch.add("cats")

"""
#Aufgabe 5 - Lists, Sets and Loops

cats = ["🐱", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾"]

#a) Konkateniere die Katzen rückwärtiger Reihenfolge zu einer String
cats.reverse()  # or reversed.cats or cats[::-1]
concat = ""
for char in cats:
    concat += char #fügt jeden Buchstaben zusammen
    print(concat)

#oder
catString = "".join(reversed(cats))
print("catString",catString)

#b) Erstelle eine Endlosschleife 
while True:
    shuffledsets ="".join(list(set(cats)))
    print(shuffledsets)
    break
 
#c) In jeder Iteration sollen für die Anzahl der Einträge in der obigen Liste zufällig Katzenemojis konkateniert werden

shuffledsets ="".join(list(set(cats)))
print(shuffledsets)

#oder
shuffledSets = list(set(cats))
catString = ""
for cat in shuffledSets:
    catString += cat
print(catString)