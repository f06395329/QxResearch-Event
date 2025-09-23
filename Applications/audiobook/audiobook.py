import pyttsx3


def read_book(path='book.txt'):
    """Read a text file aloud using pyttsx3."""
    engine = pyttsx3.init()
    with open(path, 'r', encoding='utf-8') as book:
        for line in book:
            engine.say(line)
            engine.runAndWait()


if __name__ == '__main__':
    read_book()
