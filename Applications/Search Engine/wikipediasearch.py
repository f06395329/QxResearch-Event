from tkinter import *
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def make_app():
    win = Tk()
    win.title("Wikipedia Search")

    topframe = Frame(win)
    entry = Entry(topframe)
    entry.pack()

    bottomframe = Frame(win)
    scroll = Scrollbar(bottomframe)
    scroll.pack(side=RIGHT, fill=Y)
    answer = Text(bottomframe, width=50, height=20, yscrollcommand=scroll.set, wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()

    def get_data():
        query = entry.get().strip() or "Python (programming language)"
        answer.delete(1.0, END)
        try:
            answer_value = wikipedia.summary(query)
            answer.insert(INSERT, answer_value)
        except DisambiguationError as exc:
            answer.insert(INSERT, f"Disambiguation error: {exc}")
        except PageError:
            answer.insert(INSERT, "Page not found on Wikipedia")
        except Exception:
            answer.insert(INSERT, "ERROR! Invalid input or poor internet connection")

    button = Button(topframe, text="search", command=get_data)
    button.pack()
    topframe.pack(side=TOP)

    return win


def main():
    win = make_app()
    win.mainloop()


if __name__ == "__main__":
    main()
