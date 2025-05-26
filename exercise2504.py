import random
import math

playersDB = {
    # name            # gold
    "GoblinHunter77":   214,
    "IronKnight":        65,
    "DarkElve":         377,
    "RogerOgre":        731,
    "RawDwarf1705":      99,
    "IceDragon":        287,
    "Astaroth":         605,
    "FallenAngel":     1001,
}


### Aufgabe 1
name = input("Please enter a username: ")
def _check_name(name):
    if name == "":
        print("Name cannot be empty")
        return False
    elif name in playersDB:
        print("Name is already used")
        return True
    elif name.isalnum() == False:
        print ("Name must contain only letters and numbers")
        return name.isalnum()
    else:
        print("Username accepted")
        return True
    # a) Prüfe ob der Name schon in 'playersDB' vorhanden ist.
    # b) Wenn ja dann gebe "Name is already used" in der Konsole aus und returne: False
    # c) Wenn user input leer, dann gebe "Name cannot be empty" in Konsole aus und returne: False
    # d) Optional: Wenn user input andere Zeichen enthält aus Kleinbuchstaben, Großbuchstaben oder Zahlen, dann return: False
    # e) Ansonsten returne: true
#input("Please enter a username: ")
#_check_name(name)


### Aufgabe 2
def add_player(name):
    name = input("Please enter a username: ")
    if _check_name(name) == True:
        new_player = {name: 25}
        playersDB.update(new_player)
        print(f"{name}: {playersDB[name]} added")
    else:
        print("No dice")
     # a) Erlaube einen user input für 'Please type your nickname:' und schreibe das Ergbenis in eine lokale variable: name
     # b) Frage als Bedingung in einem if statement die den Rückgabewert des Funktionaufrufes '_check_name(name)' ab.
     # c) Ist der Rückgabewert True, dann füge der playersDB einen neuen Eintrag hinzu
     # d) Der Eintrag soll als key die user eingabe eintragen und als wert: 25
     # e) Gebe den neuen Eintrag (key und value) in der Konsole aus
#add_player(name)


### Aufgabe 3
def _del_player(name):
    if _check_name(name) == "Name is already used":
        del playersDB[name]
    # a) Frage als Bedingung in einem if statement die den Rückgabewert des Funktionaufrufes '_check_name(name)' ab.
    # c) Ist der Rückgabewert True, dann entferne den player aus der playersDB 
    pass


### Aufgabe 4
def sum_gold():
    gold_list = list(playersDB.values())
    print(gold_list)
    all_gold = math.fsum(gold_list)
    print(all_gold)
    return all_gold
    # a) Summiere die Goldbestände aller player auf, und gebe das Ergebnis in der Konsole aus
    
#sum_gold()


### Aufgabe 5
def _average_gold():
    onlyindicesOfPlayersDB = [index_keys[0] for index_keys in enumerate(playersDB)]
    avg_gold= sum_gold()/(int(onlyindicesOfPlayersDB[-1]) + 1)
    print("avg_gold", avg_gold)
    return avg_gold
    # a) Berechne den Mittelwert der Goldbestände aller Player und gebe den Wert in der Konsole aus
    # b) Returne den Mittelwert auch
    pass
#_average_gold()


### Aufgabe 6
#name = input("Enter the name of the player whose gold you want to check: ")
def _read_gold(name):
    #name = input("Enter the name of the player whose gold you want to check: ")
    #nameandgold = [index_keys for index_keys in enumerate(playersDB[name])]
    gold = playersDB[name]
    print("Gold", gold)
    return gold
    # a) Lese den Goldbestand des players mit dem hier übergebenen namen und schreibe ihn in die lokale variable: gold
    # b) Gebe den Wert in der Variable 'gold' in der Konsole aus
    # c) Returne den Wert in der variable 'gold'
    
#_read_gold(name)

### Aufgabe 7
#sortby = input("What would you like to sort the player database by? Gold or Name?")
#desc = bool(input("For descending order type 'True', for ascending order 'False'"))
def sort_players(sortby = str, desc = bool):
    if desc == True or False:
        if sortby == "gold" or "Gold":
            gold_sorted_dict = dict(sorted(playersDB.items(), key=lambda item: item[1], reverse = desc))
            print(gold_sorted_dict)
        
        elif sortby == "name" or "Name":
            name_sorted_dict = (sorted(playersDB.items(), reverse = desc))
            print(name_sorted_dict)
        else:
            print("Input of string not accepted, please check)")    
    else:
            print("Input of bool not accepted, please check)")
    # Sortiere die playersDB neu, und zwar:
        # a) nach Goldbestand wenn für den Parameter 'sortby' das Argument "gold" übergeben wird
        # b) alphabetisch nach Name wenn für den Parameter 'sortby' das Argument "name" übergeben wird
        # c) absteigend wenn für den Parameter 'desc' das Argument True übergeben wird
        # d) aufsteigend wenn für den Parameter 'desc' das Argument False übergeben wird
    # Gebe die  neu sortierte playersDB auch in der Konsole aus
    
#sort_players(sortby, bool)

### Aufgabe 8
def add_bonus():
    averageGold = _average_gold()
    for key, value in playersDB.items():
        if value > averageGold:
            playersDB[key] *= 1.1
            playersDB[key] = math.ceil(playersDB[key])
            #playersDB[key] = int(playersDB[key])
    print(playersDB)
    # a) Rufe die Funktion '_average_gold()' auf und schreibe den Rückgabewert in die lokale Variable: averageGold
    # b) Erhöhe den Goldbestand jener player um 10% deren Goldbestand mindestens dem Wert in averageGold entspricht 
    # c) Runde die Werte ganzahlig mit math.ceil auf und caste sie danach in einer Integer
    # d) Gebe das die ganze playersDB in der Konsole aus
#add_bonus()


### Aufgabe 9
#fromPlayer = input("Enter a player to transfer gold FROM: ")
#toPlayer= input("Enter a player to transfer gold TO: ")
#amount = int(input("Enter an amount of gold:"))
def _transfer_amount(fromPlayer, toPlayer, amount):
    if amount > _read_gold(fromPlayer):
        print("Gold amount too high")
        pass
    else:
        playersDB[fromPlayer] -= amount
        playersDB[toPlayer] += amount
    print(playersDB)


    # a) Rufe die Funktion '_read_gold(fromPlayer)' auf und schreibe den Rückgabewert in die lokale variable: amount
    # b) Subtrahiere den Wert in 'amount' vom Kontostand den fromPlayers
    # c)  Subtrahiere den Wert in 'amount' zum Kontostand den toPlayers
    # HINWEIS: fromPlayer und toPlayer repräsentiert die Spielernamen, also den jeweiligen key in playersDB
#_transfer_amount(fromPlayer, toPlayer)


### Aufgabe 10: Bonus
def last_man_standing():
    while len(playersDB) >= 1:
        if len(playersDB) == 1:
            print("WINNER", playersDB)
            break    
        playersList = list(playersDB.keys())
        challenger1 = random.choice(playersList)
        challenger2 = random.choice(playersList)
        while challenger2 == challenger1:
            challenger2 = random.choice(playersList)
        challengeList = [challenger1, challenger2]
        winner = random.choice(challengeList)
        loser = challengeList[not winner]
        _transfer_amount(loser, winner, int(_read_gold(loser)))
        _del_player(loser)
        print(playersDB)
        challengeList.clear
        
    # a) Importiere ganz oben im Skript die random Library
    # b) Initiiere hier in der Funktion eine Endlosschleife
    # c) Wähle in jeder iteration mit Hilfe der random Library zwei Zufällige und unterschiedliche Namen aus der playersDB aus
    # d) Schreibe die namen der beiden zufälligen player in eine leere liste (lokale Variable)
    # e) Wähle per Zufallsprinzip einen player namen aus dieser Liste aus.
        # ==> Optional: Auswahlwahrscheinlichkeit, soll auf Verhätnis der Goldbestände stattfinden basieren (mehr Gold = höhere Wahrscheinlichkeit)
    # f) Der zufällig gewählte player soll gesamtes gold des anderen players erhalten => _transfer_amount(fromPlayer, toPlayer)
    # g) Der nicht zufällig gewählte player soll aus der playersDB gelöscht werden => _del_player(name)
    # h) Unterbreche die die endlos-Schleife sobald nur noch ein player in der playersDB steht
    # i) Gebe den namen und den Goldbestand dieses player dann in der Konsole aus
    # j) Bonus (Optional): Wandele den Goldbestand 1:1 in echte Bitcoin um ^^ 😺😺😺
#last_man_standing()


### Aufgabe 11: Bonus
def main():
    add_player(name)
    sum_gold()
    sort_players(sortby = "name", desc = True)
    add_bonus()   
    last_man_standing()
    # a) Rufe nur innerhalb dieser 'main()' Funktion jene der obigen Funktion nacheinander auf die nicht mit _ beginnen
    # HINWEIS: Funktionen die mit _ beginnen sollen wie in den obigen Aufgaben beschrieben nur innerhalb jener Funktionen aufgerufen werden, die nicht mit _ beginnen

# b) Rufe hier die 'main()' Funktion auf
main()

### Aufgabe 12: Bonus
# a) Etabliere in jeder Funktion ein nach eigenem Ermessen ein geeignetes Error Handling
# b) Lagere die playersDB in eine 'playersDB.json' Datei aus
# c) Erstelle eine 'readDB()' und eine 'writeDB()' Funktion, die entsprechend aus der 'playersDB.json' lesen und schreiben können
# d) Passe alle von dieser Änderung betroffenen Funktionen so an, dass Datenbankinterkationen nur noch via readDB() bzw. writeDB() stattfinden
# e) Erstelle 2 weitere Funktionen Deiner Wahl um dem Skript Mehrwert zu verleihen