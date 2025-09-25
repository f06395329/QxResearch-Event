import random
import string
import tkinter as tk
from tkinter.font import Font


def generate_password(lbl: tk.Label) -> None:
    """Generate a short password and set it on the provided label."""
    parts = []
    for _ in range(2):
        parts.append(random.choice(string.ascii_letters))
        parts.append(random.choice(string.punctuation))
        parts.append(random.choice(string.digits))
    pwd = "".join(parts)
    lbl.config(text=pwd)


def main():
    root = tk.Tk()
    root.geometry("250x200")

    btn = tk.Button(root, text="Generate Password", command=lambda: generate_password(lbl))
    btn.place(relx=0.5, rely=0.2, anchor=tk.N)

    my_font = Font(family="Times New Roman", size=12)
    lbl = tk.Label(root, font=my_font)
    lbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()
