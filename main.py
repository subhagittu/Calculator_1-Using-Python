import tkinter as tk


def calculate():

    try:

        expression = entry.get()

        result = eval(expression)

        entry.delete(0, tk.END)

        entry.insert(tk.END, str(result))

    except Exception as e:

        entry.delete(0, tk.END)

        entry.insert(tk.END, "Error")



def appendthecharacter(character):

    current_text = entry.get()

    entry.delete(0, tk.END)

    entry.insert(tk.END, current_text + character)



def clear():

    entry.delete(0, tk.END)


window = tk.Tk()

window.title("Calculator")



entry = tk.Entry(window, width=30)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]


for button_text, row, col in buttons:

    button = tk.Button(window, text=button_text, width=10, height=3,command=lambda text=button_text: appendthecharacter(text))

    button.grid(row=row, column=col)


clear_button = tk.Button(window, text="C", width=10, height=3, command=clear)



clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)



calculate_button = tk.Button(window, text="=", width=10, height=3, command=calculate)


calculate_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)



window.mainloop()
