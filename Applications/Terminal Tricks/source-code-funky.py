import pyfiglet


def main(text: str = "qxresearch", font: str = "alphabet") -> None:
    """Render `text` using pyfiglet with `font` (default: 'alphabet').

    This keeps the script import-safe and allows callers to reuse `main`.
    """
    word = pyfiglet.figlet_format(text, font=font)
    print(word)


if __name__ == "__main__":
    main()

```
Output:
                                       h
                                       h
 qqq  x x rrr eee  ss eee  aa rrr  ccc hhh
q  q   x  r   e e  s  e e a a r   c    h  h
 qqq  x x r   ee  ss  ee  aaa r    ccc h  h
   q
   qq


```
