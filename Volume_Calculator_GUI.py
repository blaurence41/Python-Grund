#Volume Calculator

import tkinter as tk
import tkinter.messagebox as msg  #Messagebox müssen wir extra importieren um diese verwenden zu können

#Sinnvoll da tkinter Library relativ umfangreich und man nicht immer alles vverwenden will (ressourcen)

app = tk.Tk()

app.title("Volumenrechner")
app.geometry("400x400+512+200")
app.resizable(False, False)

###############################################################

def clearInputs():
    _msg = msg.askyesnocancel(
        title = "Clear Inputs",
        message = "Are you sure?"
    )
    if _msg:
        hoehe_input.delete(0, tk.END)
        breite_input.delete(0, tk.END)
        tiefe_input.delete(0, tk.END)
        label_result["text"] = ""

def calcVol():
    h = hoehe_input.get()
    b = breite_input.get()
    t = tiefe_input.get()
    volume = int(h) * int(b) * int(t)
    label_result["text"] = str(volume)


##############################################################

#Parent
frame = tk.Frame(app, relief = "groove", bd = 2)

### Children

label_hoehe = tk.Label(frame, text = "Höhe: ")
hoehe_input = tk.Entry(frame)

label_breite = tk.Label(frame, text = "Breite: ")
breite_input = tk.Entry(frame)

label_tiefe = tk.Label(frame, text = "Tiefe: ")
tiefe_input = tk.Entry(frame)

button_clear = tk.Button(frame, text = "CLEAR", command = clearInputs)
button_calcVol = tk.Button(frame, text = "Get Vol.", command = calcVol)

label_result_caption = tk.Label(frame, text="Result: ")
label_result = tk.Label(frame)


####################################################

frame.pack(pady=10)

label_hoehe.pack()
hoehe_input.pack()
label_breite.pack()
breite_input.pack()
label_tiefe.pack()
tiefe_input.pack()
button_clear.pack(side = "left", padx=10, pady=10)
button_calcVol.pack(side = "right", padx=10, pady=10)
label_result.pack()
label_result_caption.pack

################################################################

app.mainloop()