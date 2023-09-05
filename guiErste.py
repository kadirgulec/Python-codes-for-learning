import tkinter as gui
window_python = gui.Tk()

#Größe des Fenster und Title
window_python.geometry("500x500")
window_python.title("Kadir Gülec")

header = gui.Frame(window_python,bg="black")
header.pack(side="left")
codingBild = gui.PhotoImage(file="codingBild.png")
codingBildLabel = gui.Label(header, image=codingBild).pack()

introduction = gui.Label(header, text="Hallo, ich bin Kadir und das ist mein erste GUI mit Python").pack(side="right")

schaltf1 = gui.Button(window_python, text="Meine Webseite")
schaltf1.pack()


window_python.mainloop()