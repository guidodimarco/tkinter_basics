# Declaración de import (1)
import tkinter
from tkinter import messagebox


# Declaración de funciones (2)
def calcular():
    precio = 250
    peso = float(txt_peso.get())
    if peso > 10:
        precio = precio + 25 * (peso - 10)
    if es_articular.get():
        precio = precio * 0.85
    if es_urgente.get():
        precio = precio * 1.25
        
    mensaje = "A pagar ${p}".format(p=precio)
    messagebox.showinfo("a cobrar", mensaje)


# Inicio del programa principal(3)
main = tkinter.Tk()
main.title("Envío de paquetes")

lbl_peso = tkinter.Label(main, text="Peso (kg): ")
txt_peso = tkinter.Entry(main)

es_articular = tkinter.IntVar()
chk_particular = tkinter.Checkbutton(main, text="Particular", variable=es_articular)

es_urgente = tkinter.IntVar()
chk_urgente = tkinter.Checkbutton(main, text="Urgente", variable=es_urgente)

btn_calcular = tkinter.Button(main, text="Calcular", command=calcular)

lbl_peso.grid(row=0, column=0)
txt_peso.grid(row=0, column=1)
chk_particular.grid(row=1, columnspan=2)
chk_urgente.grid(row=2, columnspan=2)
btn_calcular.grid(row=3, column=0, columnspan=2)

main.mainloop()
