#Tkinter

import tkinter as tk

#Background gets loaded
root = tk.Tk()
image = tk.PhotoImage(file="Rotterdamse_kaart.png")
label = tk.Label(image=image)
label.pack()

#Mouse position
x = root.winfo_pointerx()
y = root.winfo_pointery()

root.mainloop()