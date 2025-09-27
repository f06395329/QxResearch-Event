from colorama import init, Fore, Back, Style


def main(message: str = "hello qxresearcher") -> None:
    """Print `message` in a couple of terminal colors (demo helper)."""
    init()
    print(Fore.GREEN, message)
    print(Back.RED, message)


if __name__ == "__main__":
    main()

```
All Variaton on Colors: 

Fore: BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE RESET
Back: BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE RESET
Style: DIM NORMAL BRIGHT RESET_ALL
  
```
