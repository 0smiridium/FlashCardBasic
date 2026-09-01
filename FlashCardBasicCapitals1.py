import tkinter as tk


def on_click():
    print("Paris is the capital of France")


root = tk.Tk()
root.title("Capital City Quiz")
root.geometry("300x200")


button = tk.Button(root, text="What is the capital of France?", command=on_click)
button.pack(pady=50)


root.mainloop()
