from win10toast import ToastNotifier
import time


def wait_until_and_notify(target_time: str = "00:36:00",
              title: str = "Alarm",
              message: str = "This is the message",
              check_interval: float = 1.0) -> None:
  """Wait until the system clock matches `target_time` (HH:MM:SS) then show a toast.

  This function sleeps `check_interval` seconds between checks to avoid busy-waiting.
  If `win10toast` cannot be initialized, the error is printed and the function exits.
  """
  try:
    notifier = ToastNotifier()
  except Exception as exc:  # pragma: no cover - runtime dependency
    print("win10toast unavailable or failed to initialize:", exc)
    return

  while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == target_time:
      print(current_time)
      notifier.show_toast(title, message)
      break
    time.sleep(check_interval)


def main() -> None:
  """Default entry point for the timer script."""
  # Reasonable defaults; callers can import and call `wait_until_and_notify` with custom args.
  wait_until_and_notify()


if __name__ == "__main__":
  main()
