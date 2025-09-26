import win10toast


def main():
	toaster = win10toast.ToastNotifier()
	toaster.show_toast("python", "success ! This is working!", duration=10)


if __name__ == '__main__':
	main()
