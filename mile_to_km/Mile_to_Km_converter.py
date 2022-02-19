from tkinter import *


def action():
    miles = float(input.get())
    km = round(miles * 1.609)
    label_int.config(text=f"{km}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=300)
window.config(padx=200, pady=100)

input = Entry(width=10)
input.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_instruction = Label(text="is equal to")
label_instruction.grid(column=0, row=1)

label_int = Label(text="0")
label_int.grid(column=1, row=1)

label_km = Label(text="km")
label_km.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=action)
button_calculate.grid(column=1, row=2)



window.mainloop()