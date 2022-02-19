from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 18, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# new_button
new_button = Button(text="new button", command=button_clicked)
new_button.grid(column=2, row=0)


window.mainloop()
