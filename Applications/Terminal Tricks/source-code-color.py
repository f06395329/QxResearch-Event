from colorama import init, Fore, Back, Style


def main():
	init()
	print(Fore.GREEN, "hello qxresearcher")
	print(Back.RED, "hello qxresearcher")

	# to get back to boring B&W: print(Style.RESET_ALL)


if __name__ == '__main__':
	main()

```
All Variaton on Colors: 

Fore: BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE RESET
Back: BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE RESET
Style: DIM NORMAL BRIGHT RESET_ALL
  
```
