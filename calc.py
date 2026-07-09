import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")

display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

for index, text in enumerate(buttons):
    row = index // 4 + 1
    col = index % 4

    button = tk.Button(root, text=text, font=("Arial", 18))
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

for row in range(5):
    root.grid_rowconfigure(row, weight=1)

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()