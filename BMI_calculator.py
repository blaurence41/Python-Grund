import tkinter as tk
import tkinter.messagebox

# Initiiere hier für die Varible 'app' Eine Tkinter Objektinstanz
app = tk.Tk()
# Gebe dem GUI Fenster für das Betriebssystem hier einen Titel
app.title("BMI Calculator")
# Stelle folgende Fensterparameter hier ein: 400px Breite, 300px Höhe, Position 600px von links, 200px von oben
app.geometry("400x300+600+200")
# Friere die Größe des Fenster hier ein
app.resizable(False, False)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def clearInputs():
    confirm = tkinter.messagebox.askyesnocancel(
        title = "Eingaben löschen",
        message = "Wirklich leeren?"
    )
    if confirm:
        entry_gewicht.delete(0, tkinter.END)
        entry_groesse.delete(0, tkinter.END)
        label_bmi_result["text"] = "0"                  #Setze den Text von 'label_bmi_result' hier = 0

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def calc_bmi():
    category = ""
    gewicht = float(entry_gewicht.get())       # Fetche das Gewicht aus dem jew. Entry Feld und caste damit die Berechnung gemacht werden kann
    groesse = float(entry_groesse.get())     # Fetche die Größe aus dem jew. Entry Feld und caste damit die Berechnung gemacht werden kann
    bmi = gewicht / ( (groesse / 100)  ** 2)

    
    if bmi < 18.5:                          # Ist der BMI unter 18.5 setze 'category' = "Untergewicht"
        category = "Untergewicht"

    elif bmi < 25.0:                            # Ist der BMI unter 25 setze 'category' = "Normalgewicht"
        category = "Normalgewicht"

    elif bmi < 30.0:                                # Ist der BMI unter 30 setze 'category' = "Übergewicht"
        category = "Übergewicht"

    else:                                               # Ansonsten setze 'category' = "Adipositas"
        category = "Adipositas"

    # Zeige im Text des Labels 'label_bmi_result' den BMI an 
    label_bmi_result["text"] = f"BMI {int(bmi * 100)/100}: {category}" 
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

frame = tkinter.Frame(app, relief="raised", bd=2)

label_gewicht = tkinter.Label(frame, text="Gewicht (kg):")      # Erstelle hier ein Label 'label_gewicht' mit dem Text "Gewicht (kg):" und dem 'frame' als Parent
entry_gewicht = tkinter.Entry(frame)                            # Erstelle hier ein Entry Element 'entry_gewicht' mit dem 'frame' als Parent


label_groesse = tkinter.Label(frame, text="Größe (cm):")        ## Erstelle hier ein Label 'label_groesse' mit dem Text "Größe (cm):" und dem 'frame' als Parent
entry_groesse = tkinter.Entry(frame)                            ## Erstelle hier ein Entry Element 'entry_groesse' mit dem 'frame' als Parent


label_result = tkinter.Label(frame, text="BMI:")                ## Erstelle hier ein Label 'label_result' mit dem Text "BMI:" und dem 'frame' als Parent
label_bmi_result = tkinter.Label(frame, text="")   # Erstelle hier ein Label Element 'label_bmi_result' mit dem 'frame' als Parent


btn_clear = tkinter.Button(frame, text="CLEAR", command=clearInputs)   # Erstelle hier einen Button 'btn_clear' mit dem Text "BMI:" und dem 'frame' als Parent   
btn_calc = tkinter.Button(frame, text="BMI:", command=calc_bmi)       ## Erstelle hier einen Button 'btn_calc' mit dem Text "BMI:" und dem 'frame' als Parent  

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Positioniere das 'frame' via pack() und kreiere einen Abstand zum oberen Rand von 10 Bildschirmeinheiten
frame.pack(pady=10)        # row=0 (Reihe1), column=0 (Spalte1) columnspan=2 (Feld verwendet zwei Spalten ab column=0) 
# Füge dem pack des 'frame' alle Children hinzu
label_gewicht.pack()
entry_gewicht.pack()
label_groesse.pack()
entry_groesse.pack()
label_result.pack()
label_bmi_result.pack()
btn_clear.pack(padx=(10, 10), pady=(10, 10))
btn_calc.pack(padx=(10, 10), pady=(10, 10))
# Für die Buttons erstelle einen Abstand von 10 Bildschirmeinheiten zu all ihren Außenseiten


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Sorge hier mit der richtigen Tkinter Methode dafür, dass die Tkinter Objektinstanz in einer Endlosschleife läuft
tk.mainloop() 