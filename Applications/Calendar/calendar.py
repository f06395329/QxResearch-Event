import tkinter as tk
import calendar


def main():
    win = tk.Tk()
    win.title("GUI Calendar")

    def show_calendar():
        year_str = year.get()
        month_str = month.get()
        try:
            year_int = int(year_str)
            month_int = int(month_str)
            cal = calendar.month(year_int, month_int)
        except Exception:
            cal = "Invalid input."
        textfield.delete(0.0, tk.END)
        textfield.insert(tk.INSERT, cal)

    label1 = tk.Label(win, text='{Year} ')
    label1.grid(row=0, column=0)
    label2 = tk.Label(win, text='{Month} ')
    label2.grid(row=0, column=1)

    year = tk.Spinbox(win, from_=1947, to=2150, width=24)
    year.grid(row=1, column=0, padx=16)
    month = tk.Spinbox(win, from_=1, to=12, width=3)
    month.grid(row=1, column=1)

    button = tk.Button(win, text="{GO}", command=show_calendar)
    button.grid(row=1, column=2)

    textfield = tk.Text(win, height=10, width=30, foreground='brown')
    textfield.grid(row=3, columnspan=3)

    win.mainloop()


if __name__ == '__main__':
    main()
