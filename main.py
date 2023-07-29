from tkinter import *

root = Tk()
root.title('Operaciones Matematicas')
  
labelNumero1 = Label(root, text='Primer número')
labelNumero2 = Label(root, text='Segundo número')
labelNumero1.grid(row=1,column=0)
labelNumero2.grid(row=2,column=0)


myLabel1 = Label(root, text='Operaciones Matematicas')
myLabel1.grid(row=0,column=0)


numero1 = Entry(root, borderwidth=5)
numero1.grid(row=1, column=2)
numero2 = Entry(root, borderwidth=5)
numero2.grid(row=2, column=2)

res1 = Label(root, text='Suma=')
res1.grid(row=6, column=0)
res2 = Label(root, text='Resta=')
res2.grid(row=7, column=0)
res3 = Label(root, text='Multiplicacion=')
res3.grid(row=8, column=0)
res4 = Label(root, text='Division=')
res4.grid(row=9, column=0)






def myClick():
    if (numero1.get()):
        try:
            entry1 = int(numero1.get())
        except ValueError:
            print("Error: El valor ingresado no es un número válido.")
    else:
        print("Error: Debes ingresar un número.")
    
    if (numero2.get()):
        try:
            entry2 = int(numero2.get())
        except ValueError:
            print("Error: El valor ingresado no es un número válido.")
    else:
        print("Error: Debes ingresar un número.")
    suma = entry1+entry2
    mult = entry1*entry2
    div = entry1/entry2
    resta = entry1-entry2

    res1.config(text='Suma= {}'.format(suma))
    res2.config(text='resta= {}'.format(resta))
    res3.config(text='Multiplicación= {}'.format(mult))
    res4.config(text='Division= {}'.format(div))

    
def clearRes():
    res1.config(text='Suma=')
    res2.config(text='Resta=')
    res3.config(text='Multiplicacion=')
    res4.config(text='Division=')


resetButton = Button(root, text='Limpiar Resultados', background='white', fg='black', command=clearRes)
resetButton.grid(row=5, column=0)
myButton = Button(root, text='Operar', padx=50, background='black', fg='white' ,command=myClick)
myButton.grid(row=4, column=0, columnspan=3, padx=20, pady=30)


root.mainloop()