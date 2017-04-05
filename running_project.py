#Import Tkinter
from tkinter import *
from tkinter import messagebox


#Background gets loaded
root = Tk()

#Resizes the image
root.resizable(width=True, height=True)
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

image = PhotoImage(file="Rotterdamse_kaart.png")
larger_image = image.zoom(1)
label = Label(image=larger_image)

label.pack()

#Methods that run when button is pressed
def helloCallBack():
   print("Hello")

#Buttons


Button1 = Button(root, text ="Milieu", command = helloCallBack)
Button1.pack(side="left", fill='both', expand=True, padx=5, pady=5)


Button2 = Button(root, text ="Luchtkwaliteit", command = helloCallBack)
Button2.pack(side="left", fill='both', expand=True, padx=5, pady=5)

Button3 = Button(root, text ="Veiligheid", command = helloCallBack)
Button3.pack(side="left", fill='both', expand=True, padx=5, pady=5)

Button4 = Button(root, text ="Voorzieningen", command = helloCallBack)
Button4.pack(side="left", fill='both', expand=True, padx=5, pady=5)

Button5 = Button(root, text ="Tevredenheid", command = helloCallBack)
Button5.pack(side="left", fill='both', expand=True, padx=5, pady=5)

Button6 = Button(root, text ="Gemiddelde huurpprijs", command = helloCallBack)
Button6.pack(side="left", fill='both', expand=True, padx=5, pady=5)

Button7 = Button(root, text ="Gemiddelde koopprijs", command = helloCallBack)
Button7.pack(side="left", fill='both', expand=True, padx=5, pady=5)


#Mouse position
x = root.winfo_pointerx()
y = root.winfo_pointery()

root.mainloop()