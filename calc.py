import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

label = tk.Label(root, text="Calculator", font=("Arial", 20))
label.pack(pady=20)

root.mainloop()