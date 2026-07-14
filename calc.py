import tkinter as tk

def button_click(value):

    if value == "C":
        display.delete(0, tk.END)

    elif value == "⌫":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])
  
    elif value == "=":
        try:
            expression = display.get()

            expression = expression.replace("÷", "/")
            expression = expression.replace("×", "*")

            result = eval(expression)

            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "√":
        try:
            result = float(display.get()) ** 0.5

            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "x²":
        try: 
            result = float(display.get()) ** 2

            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    else:
        display.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")

display = tk.Entry(
    root, 
    font=("Arial", 24), 
    justify="right"
)

display.grid(
    row=0, 
    column=0, 
    columnspan=4, 
    sticky="nsew", 
    padx=10, 
    pady=10,
    ipady=10
)

buttons = [
    "⌫", "C", "√", "x²",
    "7", "8", "9", "÷",
    "4", "5", "6", "×",
    "1", "2", "3", "-",
    ".", "0", "=", "+"
]

for index, text in enumerate(buttons):
    row = index // 4 + 1
    col = index % 4

    button = tk.Button(
        root, 
        text=text, 
        font=("Arial", 18), 
        command=lambda value=text: button_click(value)
    )

    button.grid(
        row=row, 
        column=col, 
        sticky="nsew", 
        padx=2, 
        pady=2
    )

for row in range(6):
    root.grid_rowconfigure(row, weight=1)

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()