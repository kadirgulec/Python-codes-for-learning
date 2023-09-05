import tkinter as gui

window_python = gui.Tk()

#ich werde es mit Grid machen
frame = gui.Frame(window_python)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=1)

hrn = gui.Label(frame, text="Nordern")
hrn.grid(row=0, column=1, sticky=gui.W+gui.E)
hrm = gui.Label(frame, text="Mitte")
hrm.grid(row=1, column=1, sticky=gui.W+gui.E)
hrs = gui.Label(frame, text="Süd")
hrs.grid(row=2, column=1, sticky=gui.W+gui.E)
hrw = gui.Label(frame, text="West")
hrw.grid(row=1, column=0, sticky=gui.W+gui.E)
hro = gui.Label(frame, text="Ost")
hro.grid(row=1, column=2, sticky=gui.W+gui.E)
hrnw = gui.Label(frame, text="NordWest")
hrnw.grid(row=0, column=0, sticky=gui.W+gui.E)
hrno = gui.Label(frame, text="NordOst")
hrno.grid(row=0, column=2, sticky=gui.W+gui.E)
hrsw = gui.Label(frame, text="SüdWest")
hrsw.grid(row=2, column=0, sticky=gui.W+gui.E)
hrso = gui.Label(frame, text="SüdOst")
hrso.grid(row=2, column=2, sticky=gui.W+gui.E)


frame.pack(fill='x')
window_python.mainloop()