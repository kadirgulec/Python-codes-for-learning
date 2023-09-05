import tkinter as gui
window_python = gui.Tk()
# Textausgabe erzeugen

# 1. Beispiel
#label1 = gui.Label(window_python, text="Hallo Welt")

# 2. Beispiel
# label1 = gui.Label(window_python, text="Hallo Welt", fg="red")

# 3. Beispiel
#label2 = gui.Label(window_python,   text='Hallo Welt',
#                                    fg='#00ff00',
#                                    bg='orange',
#                                    font=('times', 25, 'bold', 'italic'))

#label1.pack()
#label2.pack()

# Grafik einbetten
bild1 = gui.PhotoImage(file="biene.png")
label2 = gui.Label(window_python, image=bild1).pack(side="right")

# Schaltfläche einbetten
# schaltf1 = gui.Button(window_python, text="Aktion durchführen")
# schaltf1.pack()

# Eingabefeld anzeigen
# eingabefeld_wert=gui.StringVar()
# eingabefeld=gui.Entry(window_python, textvariable=eingabefeld_wert)
# eingabefeld.pack()

# Verdecktes Eingabefeld anzeigen
eingabefeld=gui.Entry(window_python)
eingabefeld_wert=gui.StringVar()
eingabefeld["textvariable"] = eingabefeld_wert
eingabefeld["show"] = "*"
eingabefeld.pack()

# Programm ausführen
window_python.mainloop()
