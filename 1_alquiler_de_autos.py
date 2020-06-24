# Declaración de import (1)
import tkinter
from tkinter import messagebox


# Declaración de funciones (2)
def calcular():
    dias = float(txt_dias.get())
    kms_recorridos = float(txt_km.get())

    precio = (dias * 500) + (kms_recorridos * 45)

    mensaje = "A pagar ${p}".format(p=precio)
    messagebox.showinfo("A pagar", mensaje)


# Inicio del programa principal(3)
calcular_precio = tkinter.Tk()
calcular_precio.title("Calcular el importe a cobrar por el alquiler de autos")

lbl_dias = tkinter.Label(calcular_precio, text="Días", anchor="w", width=12)
txt_dias = tkinter.Entry(calcular_precio)

lbl_km = tkinter.Label(calcular_precio, text="KM recorridos", anchor="w", width=12)
txt_km = tkinter.Entry(calcular_precio)

btn_calcular = tkinter.Button(calcular_precio, text="Calcular", width=60, command=calcular)

lbl_dias.grid(row=0, column=0)
txt_dias.grid(row=0, column=1)

lbl_km.grid(row=1, column=0)
txt_km.grid(row=1, column=1)

btn_calcular.grid(row=2, columnspan=2)

calcular_precio.mainloop()
