# Declaración de import (1)
from tkinter import *
from tkinter import messagebox


# Declaración de funciones (2)
def on_closing():
    if messagebox.askokcancel("Salir", "¿Desea salir del programa?"):
        main.destroy()


def dele(x):
    x.delete(0, "end")


def rede():  # state='readonly'
    precio_total.configure(state='readonly')
    intereses.configure(state='readonly')
    valor_cuotas.configure(state='readonly')


def norme():  # state='normal'
    precio_total.configure(state='normal')
    intereses.configure(state='normal')
    valor_cuotas.configure(state='normal')


def limpiar():
    dele(num1)
    dele(num_cuotas)
    norme()
    dele(precio_total)
    dele(intereses)
    dele(valor_cuotas)
    rede()
    num1.focus()  # set cursor


def show_answer():
    n = int(num_cuotas.get())
    if n in range(1, 19):
        if n in range(1, 3):
            interes = 1
        elif n in range(3, 7):
            interes = 1.1
        elif n in range(7, 13):
            interes = 1.2
        elif n in range(13, 19):
            interes = 1.3

        norme()  # state='normal'

        # delete
        dele(precio_total)
        dele(intereses)
        dele(valor_cuotas)

        # insert value
        answer1 = int(num1.get()) * interes
        precio_total.insert(0, answer1)

        answer2 = answer1 - int(num1.get())
        intereses.insert(0, answer2)

        answer3 = answer1 / int(num_cuotas.get())
        valor_cuotas.insert(0, answer3)

        rede()  # state='readonly'

    else:
        messagebox.showinfo("Error", "Hasta 18 cuotas")


# Inicio del programa principal(3)
main = Tk()
main.title("Calcular precio en cuotas")

Label(main, text="Precio en una cuota:", anchor="w", width=20).grid(row=0, padx=6)
Label(main, text="Cantidad de cuotas:", anchor="w", width=20).grid(row=1)
Label(main, text="Valor de cada cuota:", anchor="w", width=20).grid(row=2)
Label(main, text="Intereses:", anchor="w", width=20).grid(row=3)
Label(main, text="Total a pagar:", anchor="w", width=20).grid(row=4)

num1 = Entry(main)
num_cuotas = Entry(main)
valor_cuotas = Entry(main)
intereses = Entry(main)
precio_total = Entry(main)

num1.focus()
rede()

num1.grid(row=0, column=1, padx=6)
num_cuotas.grid(row=1, column=1)
valor_cuotas.grid(row=2, column=1)
intereses.grid(row=3, column=1)
precio_total.grid(row=4, column=1)

Button(main, text='Calcular', command=show_answer, width=20).grid(row=5, columnspan=2, pady=4)
Button(main, text='Cerrar', command=on_closing, width=10).grid(row=6, column=0, pady=4)
Button(main, text='Limpiar', command=limpiar, width=10).grid(row=6, column=1, pady=4)


#main.protocol("WM_DELETE_WINDOW", on_closing)
main.mainloop()
