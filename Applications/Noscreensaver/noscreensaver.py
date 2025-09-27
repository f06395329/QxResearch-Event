import pyautogui
import time


def main(interval_seconds: float = 40.0, x: int = 50, y: int = 400) -> None:
    """Small helper that periodically clicks to prevent screensaver.

    Default behavior preserves the original script: sleep 40s and click at (50, 400).
    The function is safe to import and can be stopped with Ctrl+C.
    """
    try:
        while True:
            time.sleep(interval_seconds)
            pyautogui.click(x, y)
    except KeyboardInterrupt:
        print("noscreensaver: stopped by user")


if __name__ == "__main__":
    main()