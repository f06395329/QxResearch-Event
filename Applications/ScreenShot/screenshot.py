import tkinter as tk
from tkinter import messagebox
import pyautogui
from pathlib import Path
from datetime import datetime


def take_screenshot(save_dir: str | Path | None = None) -> Path:
    """Take a screenshot and save it to save_dir (current dir by default).

    Returns the Path to the saved file.
    """
    if save_dir is None:
        save_dir = Path.cwd()
    else:
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = save_dir / f"screenshot_{ts}.png"
    img = pyautogui.screenshot()
    img.save(str(out))
    return out


def main(save_prefix: str | None = None):
    win = tk.Tk()
    win.title("LoopGlitch Screenshoter")

    def callback():
        saved = take_screenshot()
        messagebox.showinfo("Saved", f"Screenshot saved to:\n{saved}")

    button = tk.Button(win, text="Screenshot This !", command=callback)
    button.grid(row=0, column=0, padx=20, pady=20)

    win.mainloop()


if __name__ == '__main__':
    main()
